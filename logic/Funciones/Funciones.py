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

#======================================================================BUSQUEDA========================================================================#
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
        if element.get("period") == periodo:
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
      if element.get("group") == grupo:
       resultados.append(element)
    return resultados

def buscar_por_estado(data, estado):
    estado = estado.lower().strip()
    resultados = []
    for element in data:
        if element["phase"].lower() == estado:
            resultados.append(element)
    return resultados  
#======================================================================MOSTRAR========================================================================#

def listar_elementos(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}") 

def listar_densidades(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Densidad: {element['density']}")  

def listar_masas(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Masa: {element['atomic_mass']}") 

def listar_grupos(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Grupo: {element['group']}")  

def listar_categorias(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}, Categoría: {element['category']}")  

def listar_periodos(data):
    for element in data:
        print(f"Nombre: {element['name']}, Símbolo: {element['symbol']}"f", Periodo: {element['period']}")                           

def mostrar_elemento(element):

    print(f"Nombre: {element['name']}")
    print(f"Símbolo: {element['symbol']}")
    print(f"Número atómico: {element['number']}")
    print(f"Masa atómica: {element['atomic_mass']}")
    print(f"Densidad: {element['density']}")
    print(f"Categoría: {element['category']}")

#==================================================================MAXIMOS Y MINIMOS====================================================================#

def elemento_mas_denso(data):
    elemento_mas_denso = data[0]
    for element in data:
        if element["density"] > elemento_mas_denso["density"]:
            elemento_mas_denso = element
    return elemento_mas_denso

def elemento_menos_denso(data):
    menos_denso = data[0]
    for element in data:
        if element["density"] < menos_denso["density"]:
            menos_denso = element
    return menos_denso 

def elemento_mayor_masa(data):
    mayor_masa = data[0]
    for element in data:
        if element["atomic_mass"] > mayor_masa["atomic_mass"]:
            mayor_masa = element
    return mayor_masa

def elemento_menor_masa(data):
    menos_masa = data[0]
    for element in data:
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
#======================================================================PROMEDIOS========================================================================#

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

#======================================================================CONTADORES=======================================================================#

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

#=====================================================================ESTADISTICAS======================================================================#

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
    conteo = distribucion_categorias(data)

    categoria_ganadora = None

    for categoria in conteo:
        if categoria_ganadora is None:
            categoria_ganadora = categoria
        elif conteo[categoria] > conteo[categoria_ganadora]:
            categoria_ganadora = categoria

    return categoria_ganadora           

#======================================================================PROGRAMA========================================================================#

if __name__ == "__main__":
 while True:  

     print("//////////MESABI//////////")

     print("1. Buscar por nombre")
     print("2. Buscar por simbolo")
     print("3. Listar elementos")
     print("4. Salir")
     print("5. Busqueda por periodo")

     opcion = input("Seleccione una opcion:")

     if opcion == "1":
      nombre = input("Ingrese el nombre del elemento:")
      element = buscar_por_nombre(data, nombre)
      if element:
        mostrar_elemento(element)
      else:
        print("Elemento no encontrado.")


     elif opcion == "2":
      simbolo = input("Ingrese el simbolo del elemento:")
      element = buscar_por_simbolo(data, simbolo)
      if element:
        mostrar_elemento(element)
      else: 
        print("Elemento no encontrado.")


     elif opcion == "3":
      listar_elementos(data)



     elif opcion == "4":
        print("Saliendo del programa...")
        break

     elif opcion == "5":
        periodo = int(input("Ingrese el periodo deseado: "))

        resultado = buscar_por_periodo(data, periodo)
        if resultado:
             print(f"Elementos en el periodo {periodo}:")
             for element in resultado:
                 mostrar_elemento(element)
        else:
            print("No se encontraron elementos en ese periodo.")

     else:  
      print("Opcion invalida")



        




