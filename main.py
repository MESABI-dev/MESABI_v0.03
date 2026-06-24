import json #se importa el archivo con los elementos

with open("elements_proof.json", "r") as file: #con with se abre y cierra el archivo pero se ejecua lo que esta identado a el 
    data = json.load(file) #se carga en data el contenido del archivo .json

element_name = input("ingrese el nombre del elemento: ")    #se pide al usuario el nombre de un elemento para usarlo como clave

for element in data: #para cada elemento en data se verifica si es igual al nommbre ingresado por el usuario
    if element_name == element["name"]: #si es igual se ejcuta una cadena de print para mostrar la informacion del elemento
        element_info = element #se guarda la informacion del elemento en una nueva variable, porque creo que la variable element es una variable temporal que cambia
        print(f"Nombre: {element_name}")
        print(f"Símbolo: {element_info['symbol']}")
        print(f"Número atómico: {element_info['atomic_number']}")
        print(f"Densidad: {element_info['density']} g/cm³")#aqui quiero resaltar que me gusta haber aprendido lo del f string ya que me parece algo muy interesante
        break
else:
    print("Elemento no encontrado.") #lo demas no lo he explicado porque se me hace algo simple
