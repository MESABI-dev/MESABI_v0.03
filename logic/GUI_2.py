import tkinter as tk

from logic.Funciones.Funciones import (
    buscar_por_nombre,
    buscar_por_nombre_parcial,
    listar_elementos,
    data
)

def buscar():
    
    nombre = entrada.get().strip() 

    elemento = buscar_por_nombre(data, nombre)

    if elemento:
        
        texto = f"Nombre: {elemento.get('name', 'N/A')}\nSímbolo: {elemento.get('symbol', 'N/A')},\nNúmero atómico: {elemento.get('number', 'N/A')}\nMasa atómica: {elemento.get('atomic_mass', 'N/A')}\nDensidad: {elemento.get('density', 'N/A')}\nCategoría: {elemento.get('category', 'N/A')}   "
    else:
        texto = "Elemento no encontrado"

    resultado.config(text=texto)


def mostrar_listar_elementos():
    if data:
        texto = "Elementos:\n" + "\n".join([f"{element['name']} ({element['symbol']})" for element in data])
        resultado_listado.config(text=texto)
    else:
        resultado_listado.config(text="No hay elementos para mostrar.")


ventana = tk.Tk()
ventana.title("MESABI_v0.02")
ventana.geometry("400x350")
ventana.configure(background="#ff6f00") 



instruccion = tk.Label(ventana, text="Ingrese el nombre del elemento:", bg="#ff6f00", fg="white", font=("Arial", 10, "bold"))
instruccion.pack(pady=5)


entrada = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada.pack(pady=5)


boton_1 = tk.Button(
    ventana,
    text="Buscar elemento   ",
    font=("Arial", 12, "bold"),
    bg="darkorange",
    fg="white",
    command=buscar
)

boton_1.pack(pady=15, ipadx=10, ipady=5) 


boton_2 = tk.Button(
    ventana,
    text="Listar elementos",
    font=("Arial", 12, "bold"),
    bg="darkorange",
    fg="white",
    command=mostrar_listar_elementos
)
boton_2.pack(pady=15, ipadx=10, ipady=5)


resultado = tk.Label(ventana, text="", bg="#ff6f00", fg="white", font=("Arial", 12, "bold"))
resultado.pack(pady=20)

resultado_listado = tk.Label(ventana, text="", bg="#ff6f00", fg="white", font=("Arial", 10))
resultado_listado.pack(pady=20)

ventana.mainloop()