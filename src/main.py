import json
from src.optimizer.model.model import resolver_instancia

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

def main():
    ruta = "data"
    while True:
        print("\n MENÚ DE OPCIONES ")
        for i in range(1, 11):
            print(f"  {i}. Resolver Instance{i}.json")
        print("  A. Agregar nueva instancia desde otra ruta")
        print("  0. Salir")

        seleccion = input("\n Selecciona una opción: ").strip().upper()

        if seleccion == "0":
            print(" ¡Hasta luego!")
            break
        elif seleccion == "A":
            path = input(" Escribe la ruta completa del archivo .json: ").strip()
            try:
                with open(path, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    resultado = resolver_instancia(datos)
                    mostrar_resultado(f"Instancia personalizada ({path})", resultado)
            except Exception as e:
                print(f" Error al cargar la instancia: {e}")
        elif seleccion.isdigit() and 1 <= int(seleccion) <= 10:
            try:
                with open(f"{ruta}/Instance{seleccion}.json", "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    resultado = resolver_instancia(datos)
                    mostrar_resultado(f"Instance {seleccion}", resultado)
            except FileNotFoundError:
                print(f" El archivo Instance{seleccion}.json no se encontró.")
        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
