import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGIC_DIR = os.path.dirname(BASE_DIR)

file_path = os.path.join(
    LOGIC_DIR,
    "Periodic_table.json"
)

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

def elemento_mas_denso(data):
    elemento_mas_denso = data[0]
    for element in data:
        if element["density"] is not None:
            if element["density"] > elemento_mas_denso["density"]:
                elemento_mas_denso = element
    return elemento_mas_denso

def elemento_menos_denso(data):
    menos_denso = data[0]
    for element in data:
        if element["density"] is not None:
            if element["density"] < menos_denso["density"]:
                 menos_denso = element
    return menos_denso 

def elemento_mayor_masa(data):
    mayor_masa = data[0]
    for element in data:
        if element["atomic_mass"] is not None:
            if element["atomic_mass"] > mayor_masa["atomic_mass"]:
                 mayor_masa = element
    return mayor_masa

def elemento_menor_masa(data):
    menos_masa = data[0]
    for element in data:
        if element["atomic_mass"] is not None:
            if element["atomic_mass"] < menos_masa["atomic_mass"]:
                menos_masa = element
    return menos_masa

def elemento_mayor_numero_atomico(data):
    mayor_numero_atomico = data[0]
    for element in data:
        if element["number"] > mayor_numero_atomico["number"]:
            mayor_numero_atomico = element
    return mayor_numero_atomico        

def elemento_menor_numero_atomico(data):
    menor_numero_atomico = data[0]
    for element in data:
        if element["number"] < menor_numero_atomico["number"]:
            menor_numero_atomico = element
    return menor_numero_atomico

def elemento_mas_denso_categoria(data, categoria):
    categoria = categoria.lower().strip()
    elemento_mas_denso = None
    for element in data:
        if element["category"].lower() == categoria:
            if elemento_mas_denso == None or element["density"] > elemento_mas_denso["density"]:
                elemento_mas_denso = element
    return elemento_mas_denso

def elemento_mas_pesado_periodo(data, periodo):
    periodo = int(periodo)
    elemento_mas_pesado = None
    for element in data:
        if element["period"] == periodo:
            if elemento_mas_pesado == None or element["atomic_mass"] > elemento_mas_pesado["atomic_mass"]:
                elemento_mas_pesado = element
    return elemento_mas_pesado

def elemento_mas_ligero_grupo(data, grupo):
    grupo = int(grupo)
    elemento_mas_ligero = None
    for element in data:
        if element["group"] == grupo:
            if elemento_mas_ligero == None or element["atomic_mass"] < elemento_mas_ligero["atomic_mass"]:
                elemento_mas_ligero = element
    return elemento_mas_ligero    