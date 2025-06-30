import json
from pathlib import Path

def cargar_instancia_desde_menu(seleccion, ruta):
    with open(ruta / f"instance{seleccion}.json", "r", encoding="utf-8") as f:
        return json.load(f)

def cargar_instancia_personalizada(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
