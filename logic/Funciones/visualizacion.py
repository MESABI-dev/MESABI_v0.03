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

from Funciones.estadisticas import(
    categoria_mas_elementos
)

def listar_elementos(data):
    elementos = []
    for element in data:
            elementos.append(element)
    return elementos

def listar_densidades(data):
    densidades = []
    for element in data:
        densidades.append(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Densidad: {element['density']}")
    return densidades

def listar_masas(data):
    masas = []
    for element in data:
        masas.append(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Masa: {element['atomic_mass']}")
    return masas

def listar_grupos(data):
    grupos = []
    for element in data:
        grupos.append(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Grupo: {element['group']}")
    return grupos

def listar_categorias(data):
    categorias = []
    for element in data:
        categorias.append(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Categoría: {element['category']}")
    return categorias

def listar_periodos(data):
    periodos = []
    for element in data:
        periodos.append(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Periodo: {element['period']}")
    return periodos

def texto_elemento(element):
    if element:
        return f"""
Nombre: {element['name']}
Símbolo: {element['symbol']}
Número atómico: {element['number']}
Masa atómica: {element['atomic_mass']}
Densidad: {element['density']}kg/m^3
Categoría: {element['category']}
"""

def texto_resumen(resumen):
    if resumen:
        return f"""        
Cantidad: {resumen['cantidad']}
Masa promedio: {resumen['masa_promedio']}
Densidad promedio: {resumen['densidad_promedio']}
"""

def texto_distribucion_categoria(conteo_diccionario):
    texto_reporte = "=== DISTRIBUCION POR CATEGORIAS ===\n\n"
    for categoria, cantidad in conteo_diccionario.items():
        texto_reporte += f"{categoria}: {cantidad} elementos\n"
    return texto_reporte

def texto_categoria_ganadora(nombre_categoria, cantidad):
    if nombre_categoria:
        return f"""
=========================================
      REPORTE: CATEGORÍA DOMINANTE       
=========================================
La categoría con mayor presencia en la 
tabla periódica es: 
{nombre_categoria.upper()}

Cuenta con un total de: {cantidad} elementos.
=========================================
"""
    else:
        return "Error: No se pudo determinar la categoría dominante."
    
def mostrar_lista(elementos):
    texto_final = ""
    for e in elementos:
        if e:
            texto_final += texto_elemento(e)
    return texto_final     

def texto_elemento_nombre(element):
    if element:
        return f"""
Nombre: {element['name']}, Símbolo: {element['symbol']}
"""
    
def mostrar_lista_nombre(elementos):
    texto_final = ""
    for e in elementos:
        if e:
            texto_final += texto_elemento_nombre(e)
    return texto_final     

def texto_comparacion(comparacion):
    if not comparacion:
        return "Error entrada inválida"
    return f"""
============================================================
                         Comparacion                        
============================================================
Elementos | [{comparacion['simbolo_1']}] {comparacion['nombre_1']} | [{comparacion['simbolo_2']}] {comparacion['nombre_2']}
------------------------------------------------------------
Numero atomico | {comparacion['numero_atomico_1']} | {comparacion['numero_atomico_2']}
Masa Atomica | {comparacion['masa_atomica_1']} | {comparacion['masa_atomica_2']}
Densidad | {comparacion['densidad_1']}g/cm³ | {comparacion['densidad_2']}g/cm³
Punto de fusión | {comparacion['punto_de_fusion_1']}°K | {comparacion['punto_de_fusion_2']}°K
Estado | {comparacion['estado_1']} | {comparacion['estado_2']}
Categoria | {comparacion['categoria_1']} | {comparacion['categoria_2']}
Grupo | {comparacion['grupo_1']} | {comparacion['grupo_2']}
Periodo | {comparacion['periodo_1']} | {comparacion['periodo_2']}
============================================================

"""    