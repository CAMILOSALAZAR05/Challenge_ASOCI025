import sys
import os

# Añadir la carpeta raíz al path para imports relativos
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.data.loader import cargar_instancia
from src.model.optimizer import resolver_instancia # type: ignore
from src.visualization.display import mostrar_resultado

def main():
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
                import json
                with open(path, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    resultado = resolver_instancia(datos)
                    mostrar_resultado(f"Instancia personalizada ({path})", resultado)
            except Exception as e:
                print(f" Error al cargar la instancia: {e}")

        elif seleccion.isdigit() and 1 <= int(seleccion) <= 10:
            try:
                from src.data.loader import cargar_instancia
                datos = cargar_instancia(f"Instance{seleccion}.json")
                resultado = resolver_instancia(datos)
                mostrar_resultado(f"Instance {seleccion}", resultado)
            except FileNotFoundError as e:
                print(e)
        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()