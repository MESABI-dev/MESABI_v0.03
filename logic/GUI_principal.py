import tkinter as tk

from Funciones.busquedas import (
    buscar_por_nombre,
    buscar_por_simbolo,
    buscar_por_numero_atomico,
    buscar_por_categoria,
    buscar_por_grupo,
    buscar_por_periodo,
    buscar_por_nombre_parcial,
    buscar_por_estado,
    comparar_elementos,
    data
)

from Funciones.visualizacion import (
    texto_elemento,
    mostrar_lista,
    mostrar_lista_nombre,
    listar_elementos,
    texto_resumen,
    texto_distribucion_categoria,
    texto_categoria_ganadora,
    texto_comparacion
)

from Funciones.max_min import(
    elemento_mas_denso,
    elemento_menos_denso,
    elemento_mayor_masa,
    elemento_menor_masa,
)

from Funciones.estadisticas import(
    resumen_categoria,
    resumen_periodo,
    distribucion_categorias,
    categoria_mas_elementos,
)

#=======================================================================Funciones busqueda==============================================================#

def mostrar_resultado(texto):
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, texto)

def buscar():
    nombre = entrada_busqueda.get().strip()
    elemento = buscar_por_nombre(data, nombre)   
    if elemento:
        texto = texto_elemento(elemento)
    else:
        texto = ("Entrada inválida")    
    mostrar_resultado(texto)

def buscar_simbolo():
    simbolo = entrada_busqueda.get().strip()
    elemento = buscar_por_simbolo(data, simbolo)
    if elemento:
        texto = texto_elemento(elemento)
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto)

def buscar_numero_atomico():
    numero_atomico = entrada_busqueda.get().strip()
    elemento = buscar_por_numero_atomico(data, numero_atomico)
    if elemento is not None:
        texto = texto_elemento(elemento)
    else:
        texto = ("Entrada inválida")      
    mostrar_resultado(texto)

def buscar_categoria():
    categoria = entrada_busqueda.get().strip()
    elementos = buscar_por_categoria(data, categoria)
    if elementos is not None:   
        texto = mostrar_lista(elementos)
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto)

def buscar_grupo():
    grupo = entrada_busqueda.get().strip()
    elementos = buscar_por_grupo(data, grupo)
    if elementos is not None:
        texto = mostrar_lista(elementos)
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto)   

def buscar_periodo():
    periodo = entrada_busqueda.get().strip()
    elementos = buscar_por_periodo (data, periodo)
    if elementos is not None:
        texto = mostrar_lista(elementos)         
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto)    

def busqueda_parcial():
    nombre = entrada_busqueda.get().strip()
    elementos = buscar_por_nombre_parcial(data, nombre)
    if elementos is not None:
        texto = mostrar_lista(elementos)
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto)    

def buscar_estado():
    estado = entrada_busqueda.get().strip()
    elementos = buscar_por_estado(data, estado)
    if elementos is not None:
        texto = mostrar_lista(elementos)
    else:
        texto = ("Entrada inválida")
    mostrar_resultado(texto) 

#==================================================================funciones operaciones================================================================#

def listar():
        elemento = listar_elementos(data)
        if elemento is not None:
            texto = mostrar_lista_nombre(elemento)
        else:
            texto = ("Entrada inválida")   
        mostrar_resultado(texto)

def elemento_mas_denso_texto():
    elemento = elemento_mas_denso(data)
    if elemento is not None:
        texto = texto_elemento(elemento)
    else:
        texto = ("Error")
    mostrar_resultado(texto)

def elemento_menos_denso_texto():
    elemento = elemento_menos_denso(data)
    if elemento is not None:
        texto = texto_elemento(elemento)
    else:
        texto = ("Error")
    mostrar_resultado(texto)

def elemento_mayor_masa_texto():
    elemento = elemento_mayor_masa(data)
    if elemento is not None:
        texto = texto_elemento(elemento)
    else:
        texto = ("Error")
    mostrar_resultado(texto) 

def elemento_menor_masa_texto():
    elemento = elemento_menor_masa(data)
    if elemento is not None:
        texto = texto_elemento(elemento)
    else:
        texto = ("Error")
    mostrar_resultado(texto)

#==================================================================funciones estadisticas================================================================#
def resumir_categoria():
    categoria = entrada_busqueda.get().strip()
    resumen = resumen_categoria(data, categoria)
    if resumen is not None:
        texto = texto_resumen(resumen)
    else:
        texto = ("error")    
    mostrar_resultado(texto)

def resumir_periodo():
    periodo = entrada_busqueda.get().strip()
    resumen = resumen_periodo(data, periodo)
    if resumen is not None: 
        texto = texto_resumen(resumen)
    else:
        texto = ("error")
    mostrar_resultado(texto)    

def mostrar_distribucion():
    resultado_conteo = distribucion_categorias(data)
    texto_final = texto_distribucion_categoria(resultado_conteo)
    mostrar_resultado(texto_final)

def categoria_ganadora():
    nombre_categoria, cantidad = categoria_mas_elementos(data)
    texto_reporte = texto_categoria_ganadora(nombre_categoria, cantidad)
    mostrar_resultado(texto_reporte)

def mostrar_texto_comparacion():
    nombre_1 = entrada_elemento1.get().strip()
    nombre_2 = entrada_elemento2.get().strip()
    if not nombre_1 or not nombre_2:
        mostrar_resultado("Error")
        return
    elemento_1 = buscar_por_nombre(data, nombre_1) or buscar_por_simbolo(data, nombre_1)
    elemento_2 = buscar_por_nombre(data, nombre_2) or buscar_por_simbolo(data, nombre_2)
    if not elemento_1 or not elemento_2:
        mostrar_resultado("Error")
        return
    comparacion = comparar_elementos(elemento_1, elemento_2)
    texto_comparar = texto_comparacion(comparacion)
    mostrar_resultado(texto_comparar)
#=======================================================================Programa========================================================================#
ventana=tk.Tk()
ventana.title("MESABI_v0.03")
ventana.geometry("750x650") 
ventana.configure(bg="#00F7FF")
ventana.resizable(True, True)

ventana.rowconfigure(0, weight=1) 
ventana.rowconfigure(1, weight=1) 

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

frame_busqueda = tk.Frame(ventana, borderwidth=2, relief="solid", bg="#00BFFF")
frame_operaciones = tk.Frame(ventana, borderwidth=2, relief="solid", bg="#00A6FF")
frame_comparacion = tk.Frame(ventana, borderwidth=2, relief="solid", bg="#0088FF")
frame_resultados = tk.Frame(ventana, borderwidth=2, relief="solid", bg="#004CFF")

frame_busqueda.grid(row=0, column=0, sticky="nsew", padx=6, pady=6)
frame_operaciones.grid(row=0, column=1, sticky="nsew", padx=6, pady=6)

frame_comparacion.grid(row=1, column=0, sticky="nsew", padx=6, pady=6)
frame_resultados.grid(row=1, column=1, sticky="nsew", padx=6, pady=6)

frame_busqueda.columnconfigure(0, weight=1)
frame_busqueda.columnconfigure(1, weight=1)

frame_operaciones.columnconfigure(0, weight=1)
frame_operaciones.columnconfigure(1, weight=1)

frame_resultados.rowconfigure(1, weight=1) 
frame_resultados.columnconfigure(0, weight=1) 

#Label
label_busqueda =  tk.Label(frame_busqueda, text="BUSQUEDA") 
label_operaciones = tk.Label(frame_operaciones, text= "OPERACIONES")
label_comparacion = tk.Label(frame_comparacion, text="COMPARACION", justify="center")
label_resultado =  tk.Label(frame_resultados, text="RESULTADO", justify="center")

label_busqueda.grid(row=0,column=0,columnspan=2)
label_operaciones.grid(row=0, column=0, columnspan=2)
label_comparacion.grid(row=0, column=0, columnspan=2)
label_resultado.grid(row=0, column=0, columnspan=2)

#Scrollbar
scroll_vertical = tk.Scrollbar(frame_resultados, orient="vertical")
resultado_text = tk.Text(frame_resultados, yscrollcommand=scroll_vertical.set)
scroll_vertical.config(command=resultado_text.yview)
resultado_text.grid(row=1, column=0, sticky="nsew")
scroll_vertical.grid(row=1, column=1, sticky="ns")

#=======================================================================Busqueda========================================================================#

#Entry
entrada_busqueda = tk.Entry(frame_busqueda)
entrada_elemento1 = tk.Entry(frame_comparacion)
entrada_elemento2 = tk.Entry(frame_comparacion)

#Buttons
boton_busqueda = tk.Button(frame_busqueda, text="Buscar", command=buscar, width=30)
boton_busqueda_simbolo = tk.Button(frame_busqueda, text="Buscar por simbolo", command=buscar_simbolo, width=30)
boton_busqueda_numero_atomico = tk.Button(frame_busqueda, text="Buscar por numero atomico", command=buscar_numero_atomico, width=30)
boton_busqueda_categoria = tk.Button(frame_busqueda,text="Buscar por categoria",command=buscar_categoria,width=30)
boton_busqueda_grupo = tk.Button(frame_busqueda,text="Buscar por grupo",command=buscar_grupo,width=30)
boton_busqueda_periodo = tk.Button(frame_busqueda,text="Buscar por periodo",command=buscar_periodo,width=30)
boton_busqueda_parcial = tk.Button(frame_busqueda,text="Buscar por nombre parcial",command=busqueda_parcial,width=30)
boton_busqueda_estado= tk.Button(frame_busqueda,text="Buscar por estado",command=buscar_estado,width=30)

#======================================================================Operaciones======================================================================#
boton_listar_elementos = tk.Button(frame_operaciones,text="Listar elementos",command=listar,width=30)
boton_mas_denso = tk.Button(frame_operaciones,text="Elemento mas denso",command=elemento_mas_denso_texto,width=30)
boton_menos_denso = tk.Button(frame_operaciones,text="Elemento menos denso",command=elemento_menos_denso_texto, width=30)
boton_mayor_masa = tk.Button(frame_operaciones,text="Elemento mayor masa",command=elemento_mayor_masa_texto,width=30)
boton_menor_masa = tk.Button(frame_operaciones,text="Elemento menor masa",command=elemento_menor_masa_texto,width=30)
boton_resumen_categoria = tk.Button(frame_operaciones,text="Resumen categoría",command=resumir_categoria, width=30)
boton_resumen_periodo = tk.Button(frame_operaciones,text="Resumen periodo",command=resumir_periodo, width=30)
boton_distribucion_categoria= tk.Button(frame_operaciones,text="Distribucion categorias",command=mostrar_distribucion, width=30)
boton_categoria_mas_elementos = tk.Button(frame_operaciones,text="Categoria mas elementos",command=categoria_ganadora, width=30)

#==================================================================Comparacion==========================================================================#
boton_comparacion = tk.Button(frame_comparacion,text="Comparar",command=mostrar_texto_comparacion,width=30)
#===================================================================Configuracion botones===============================================================#
#Entry.grid()
entrada_busqueda.grid(row=1,column=0,columnspan=2)
entrada_elemento1.grid(row=1, column=0, columnspan=2)
entrada_elemento2.grid(row=2, column=0, columnspan=2)

#Button.grid()
boton_busqueda.grid(row=2,column=0)
boton_busqueda_simbolo.grid(row=2,column=1)
boton_busqueda_numero_atomico.grid(row=3,column=0)
boton_busqueda_categoria.grid(row=3,column=1)
boton_busqueda_grupo.grid(row=4, column=0)
boton_busqueda_periodo.grid(row=4, column=1)
boton_busqueda_parcial.grid(row=5, column=0)
boton_busqueda_estado.grid(row=5, column=1)

boton_listar_elementos.grid(row=1,column=0,columnspan=2)
boton_mas_denso.grid(row=2,column=0)
boton_menos_denso.grid(row=2,column=1)
boton_mayor_masa.grid(row=3,column=0)
boton_menor_masa.grid(row=3,column=1)
boton_resumen_categoria.grid(row=4, column=0)
boton_resumen_periodo.grid(row=4, column=1)
boton_distribucion_categoria.grid(row=5, column=0)
boton_categoria_mas_elementos.grid(row=5, column=1)

boton_comparacion.grid(row=0, column=0)

ventana.mainloop()