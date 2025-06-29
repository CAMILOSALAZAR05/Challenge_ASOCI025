import json
import os

def cargar_instancia(nombre_archivo):
    ruta_datos = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
    ruta_completa = os.path.join(ruta_datos, nombre_archivo)

    try:
        with open(ruta_completa, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_completa}")