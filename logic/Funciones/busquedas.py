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

def buscar_por_nombre(data, nombre):
    nombre = nombre.lower().strip()
    for element in data:
        if element["name"].lower() == nombre:
            return element
    return None

def buscar_por_nombre_parcial(data, nombre):
    nombre = nombre.lower().strip()
    resultados = []
    for element in data:
        if nombre in element["name"].lower():
            resultados.append(element)
    return resultados

def buscar_por_simbolo(data, simbolo):
    simbolo = simbolo.lower().strip()
    for element in data:
        if element["symbol"].lower() == simbolo:
            return element
    return None   

def buscar_por_periodo(data, periodo):
    resultados = []
    periodo = int(periodo)
    for element in data:
        if element["period"] == periodo:
            resultados.append(element)

    return resultados

def buscar_por_categoria(data, categoria):
    categoria = categoria.lower().strip()
    resultados = []
    for element in data:
        if element["category"].lower() == categoria:
            resultados.append(element)
    return resultados

def buscar_por_numero_atomico(data, numero_atomico):
    numero_atomico = int(numero_atomico)
    for element in data:
       if element["number"] == numero_atomico:
          return element
    return None
   
def buscar_por_grupo(data, grupo):
    grupo = int(grupo)
    resultados = []
    for element in data:
      if element["group"] == grupo:
       resultados.append(element)
    return resultados

def buscar_por_estado(data, estado):
    estado = estado.lower().strip()
    resultados = []
    for element in data:
        if element["phase"].lower() == estado:
            resultados.append(element)
    return resultados      

    elemento_1 = buscar_por_nombre()   
    elemento_2 = buscar_por_nombre()   

def comparar_elementos(elemento_1, elemento_2):
  
    comparacion = {
        "nombre_1": elemento_1.get("name"),
        "nombre_2": elemento_2.get("name"),

        "simbolo_1": elemento_1.get("symbol"),
        "simbolo_2": elemento_2.get("symbol"),

        "numero_atomico_1": elemento_1.get("number"),
        "numero_atomico_2": elemento_2.get("number"),

        "masa_atomica_1": elemento_1.get("atomic_mass"),
        "masa_atomica_2": elemento_2.get("atomic_mass"),

        "densidad_1": elemento_1.get("density"),
        "densidad_2": elemento_2.get("density"),

        "punto_de_fusion_1": elemento_1.get("melt"),
        "punto_de_fusion_2": elemento_2.get("melt"),

        "estado_1": elemento_1.get("phase"),
        "estado_2": elemento_2.get("phase"),

        "categoria_1": elemento_1.get("category"),
        "categoria_2": elemento_2.get("category"),

        "grupo_1": elemento_1.get("group"),
        "grupo_2": elemento_2.get("group"),

        "periodo_1": elemento_1.get("period"),
        "periodo_2": elemento_2.get("period"),

    }
    return comparacion    