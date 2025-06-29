from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpBinary, PULP_CBC_CMD

def resolver_instancia(data):
    empleados = data["Employees"]
    escritorios = data["Desks"]
    grupos = data["Groups"]
    dias = data["Days"]
    desks_e = data["Desks_E"]
    empleados_g = data["Employees_G"]
    dias_e = data["Days_E"]

    # Variables de decisión
    prob = LpProblem("Asignación_Escritorios", LpMaximize)
    x = {(e, d, h): LpVariable(f"x_{e}_{d}_{h}", cat=LpBinary)
        for e in empleados for d in desks_e.get(e, []) for h in dias_e.get(e, []) if h in dias}

    # Función objetivo: Maximizar número total de asignaciones válidas
    prob += lpSum(x[e, d, h] for (e, d, h) in x)

    # Restricción 1: Un empleado usa solo un escritorio por día
    for e in empleados:
        for h in dias:
            prob += lpSum(x[e, d, h] for d in desks_e.get(e, []) if (e, d, h) in x) <= 1

    # Restricción 2: Un escritorio no puede ser usado por más de un empleado por día
    for d in data["Desks"]:
        for h in dias:
            prob += lpSum(x[e, d, h] for e in empleados if (e, d, h) in x) <= 1

    # Restricción 3: Cada empleado debe asistir al menos un día (idealmente 2 o 3)
    for e in empleados:
        prob += lpSum(x[e, d, h] for d in desks_e.get(e, []) for h in dias_e.get(e, []) if (e, d, h) in x) >= 1
        prob += lpSum(x[e, d, h] for d in desks_e.get(e, []) for h in dias_e.get(e, []) if (e, d, h) in x) <= 3

    # Resolución del modelo
    prob.solve(PULP_CBC_CMD(msg=False))

    # Interpretación de resultados
    resultados = {
        "totales": {
            "empleados": len(empleados),
            "escritorios": len(data["Desks"]),
            "grupos": len(grupos),
            "zonas": len(data["Zones"])
        },
        "dias_reunion": {},
        "dias_empleados": {},
        "zonas_grupo": {},
        "asignaciones": {}
    }

    # Asignación por empleado y día
    asistencia = {e: set() for e in empleados}
    asignaciones = {e: {} for e in empleados}
    for (e, d, h), var in x.items():
        if var.varValue == 1:
            asignaciones[e][h] = d
            asistencia[e].add(h)

    resultados["asignaciones"] = asignaciones
    resultados["dias_empleados"] = {e: sorted(list(asistencia[e])) for e in empleados}

    # Día óptimo de reunión por grupo (máximo número de coincidencias)
    for g in grupos:
        miembros = empleados_g.get(g, [])
        conteo = {h: sum(1 for e in miembros if h in asistencia[e]) for h in dias}
        dia_optimo = max(conteo, key=conteo.get)
        resultados["dias_reunion"][g] = dia_optimo

    # Zonas por grupo (heurística simple basada en escritorios más usados)
    escritorios_usados = {e: list(asignaciones[e].values()) for e in empleados}
    zonas_grupo = {}
    for g in grupos:
        zonas = []
        for e in empleados_g[g]:
            usados = escritorios_usados.get(e, [])
            for zona, lista in data["Desks_Z"].items():
                if any(d in lista for d in usados):
                    zonas.append(zona)
        zona_mayoritaria = max(set(zonas), key=zonas.count) if zonas else "Z0"
        zonas_grupo[g] = zona_mayoritaria
    resultados["zonas_grupo"] = zonas_grupo

    return resultados