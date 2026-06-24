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

from Funciones.promedios import (masa_promedio_categoria, masa_promedio_periodo, densidad_promedio_categoria, densidad_promedio_periodo)    

def cantidad_por_categoria(data, categoria):
    categoria = categoria.lower().strip()
    cantidad = 0
    for element in data:
        if element["category"].lower() == categoria:
            cantidad += 1
    return cantidad
      
def cantidad_por_periodo(data, periodo):
    cantidad = 0
    periodo = int(periodo)
    for element in data:
        if element["period"] == periodo:
            cantidad += 1
    return cantidad

def cantidad_por_grupo(data, grupo):
    grupo = int(grupo)
    cantidad = 0
    for element in data:
        if element["group"] == grupo:
            cantidad += 1
    return cantidad          

def resumen_categoria(data, categoria):
    cantidad = cantidad_por_categoria(data, categoria)
    masa_promedio = masa_promedio_categoria(data, categoria)
    densidad_prom = densidad_promedio_categoria(data, categoria)

    resumen = {
        "cantidad": cantidad,
        "masa_promedio": masa_promedio,
        "densidad_promedio": densidad_prom
        }
    return resumen

def resumen_periodo(data, periodo):
    cantidad = cantidad_por_periodo(data, periodo)
    masa_promedio = masa_promedio_periodo(data, periodo)
    densidad_prom = densidad_promedio_periodo(data, periodo)

    resumen = {
        "cantidad": cantidad,
        "masa_promedio": masa_promedio,
        "densidad_promedio": densidad_prom
        }
    return resumen

def distribucion_categorias(data):
    conteo = {}
    for element in data: 
        categoria = element["category"]
        if categoria in conteo:
            conteo[categoria] += 1
        else:
            conteo[categoria] = 1
    return conteo        

def categoria_mas_elementos(data):
    conteo = {}
    for element in data: 
        categoria = element["category"]
        conteo[categoria] = conteo.get(categoria, 0) + 1

    categoria_ganadora = None
    max_cantidad = -1
    
    for categoria, cantidad in conteo.items():
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            categoria_ganadora = categoria
            
    return categoria_ganadora, max_cantidad     
