# main.py
from config.rutas import RUTA_ELEMENTOS
from repositorios.cargadores import CargadorJson
from fabricas.fabrica_elemento import ElementoFabrica

#Prueba de CargadorJson
cargador = CargadorJson(RUTA_ELEMENTOS)
datos = cargador.cargar()
print(type(datos))
print(type(datos[0]))

elemento = ElementoFabrica.crear_desde_diccionario(datos[0])
print(type(elemento))