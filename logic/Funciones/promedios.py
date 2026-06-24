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

def densidad_promedio(data):
    suma_densidades = 0
    elementos = len(data)
    for element in data:
        suma_densidades += element["density"]
    return suma_densidades / elementos

def masa_atomica_promedio(data):
    suma_masa = 0
    contador = 0
    for element in data:
        if element["atomic_mass"]:
            suma_masa += element["atomic_mass"]
            contador += 1
    return suma_masa / contador       

def masa_promedio_categoria(data, categoria):
    suma_masa = 0
    contador = 0
    categoria = categoria.lower().strip()
    
    for element in data:
        if element["category"].lower() == categoria:
            if element["atomic_mass"]:
                suma_masa += element["atomic_mass"]
                contador += 1
    if contador == 0:
        return 0            
    return suma_masa / contador    

def masa_promedio_periodo(data, periodo): 
    suma_masa = 0
    contador = 0
    periodo = int(periodo)
    
    for element in data:
        if element["period"] == periodo:
            if element["atomic_mass"]:
                suma_masa += element["atomic_mass"]
                contador += 1
    if contador == 0:
        return 0            
    return suma_masa / contador

def masa_promedio_grupo(data, grupo):
    suma_masa = 0
    contador = 0
    grupo = int(grupo)

    for element in data:
        if element["group"] == grupo:
            if element["atomic_mass"]:
                suma_masa += element["atomic_mass"]
                contador += 1
    if contador == 0:
        return 0            
    return suma_masa / contador

def densidad_promedio_periodo(data, periodo):
    suma_densidad = 0
    contador = 0
    periodo = int(periodo)

    for element in data:
        if element["period"] == periodo:    
            if element["density"]:
                suma_densidad += element["density"]
                contador += 1
    if contador == 0:
        return 0
    return suma_densidad / contador  

def densidad_promedio_categoria(data, categoria):
    suma_densidad = 0
    contador = 0
    categoria = categoria.lower().strip()

    for element in data:
        if element["category"].lower() == categoria:    
            if element["density"]:
                suma_densidad += element["density"]
                contador += 1
    if contador == 0:
        return 0
    return suma_densidad / contador 

def densidad_promedio_grupo(data, grupo):
    suma_densidad = 0
    contador = 0
    grupo = int(grupo)

    for element in data:
        if element["group"] == grupo:    
            if element["density"]:
                suma_densidad += element["density"]
                contador += 1
    if contador == 0:
        return 0
    return suma_densidad / contador      