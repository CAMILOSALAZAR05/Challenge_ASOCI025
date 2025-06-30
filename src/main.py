from pathlib import Path
from src.optimizer.model.model import resolver_instancia
from src.utils.loader import cargar_instancia_desde_menu, cargar_instancia_personalizada
from src.utils.display import mostrar_resultado

def main():
    ruta = Path(__file__).resolve().parent.parent / "data"
    while True:
        print("\n MENÚ DE OPCIONES ")
        for i in range(1, 11):
            print(f"  {i}. Resolver instance{i}.json")
        print("  A. Agregar nueva instancia desde otra ruta")
        print("  0. Salir")

        seleccion = input("\n Selecciona una opción: ").strip().upper()

        if seleccion == "0":
            print(" ¡Hasta luego!")
            break
        elif seleccion == "A":
            path = input(" Escribe la ruta completa del archivo .json: ").strip()
            try:
                datos = cargar_instancia_personalizada(path)
                resultado = resolver_instancia(datos)
                mostrar_resultado(f"Instancia personalizada ({path})", resultado)
            except Exception as e:
                print(f" Error al cargar la instancia: {e}")
        elif seleccion.isdigit() and 1 <= int(seleccion) <= 10:
            try:
                datos = cargar_instancia_desde_menu(seleccion, ruta)
                resultado = resolver_instancia(datos)
                mostrar_resultado(f"Instance {seleccion}", resultado)
            except FileNotFoundError:
                print(f" El archivo instance{seleccion}.json no se encontró.")
        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
