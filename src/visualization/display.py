
def mostrar_resultado(nombre, res):
    print(f"\n Resultado para {nombre} ")
    tot = res["totales"]
    print(f"Empleados: {tot['empleados']}")
    print(f"Escritorios: {tot['escritorios']}")
    print(f"Grupos: {tot['grupos']}")
    print(f"Zonas: {tot['zonas']}")

    print("\n Días de reunión por grupo:")
    for g, d in res["dias_reunion"].items():
        print(f"  - Grupo {g}: {d}")

    print("\n Días de asistencia por empleado:")
    for e, dias in res["dias_empleados"].items():
        print(f"  - {e}: {dias}")

    print("\n Zona asignada por grupo:")
    for g, z in res["zonas_grupo"].items():
        print(f"  - Grupo {g}: Zona {z}")

    print("\n Asignación por empleado y día:")
    for e, dias in res["asignaciones"].items():
        print(f"  - {e}:")
        for d, desk in dias.items():
            print(f"      {d}: {desk}")