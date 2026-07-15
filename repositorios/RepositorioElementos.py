import json
from Excepciones.excepciones import (ElementoNoEncontradoError, ArchivoNoEncontradoError)
from modelos.Elemento import Elemento
class CargadorJson:
    def __init__(self, ruta_json):
        self.ruta_json = ruta_json
    def cargar(self) -> list[Elemento]:
        try:
            with open(self.ruta_json, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            raise ArchivoNoEncontradoError(self.ruta_json)
        except json.JSONDecodeError:
            raise ArchivoNoEncontradoError(self.ruta_json)
        lista_elementos = []  
        for dato in datos:
            elemento = Elemento.desde_diccionario(dato)
            lista_elementos.append(elemento)
        return lista_elementos
class RepositorioElementos:
    def __init__(self, elementos: list[Elemento]):
        self._elementos = elementos 
    def buscar_por_nombre(self, nombre: str) -> Elemento:
        for elemento in self._elementos:
            if elemento.nombre.lower() == nombre.lower():
                return elemento
        raise ElementoNoEncontradoError(nombre)
    def buscar_por_simbolo(self, simbolo: str) -> Elemento:
        for elemento in self._elementos:
            if elemento.simbolo.lower() == simbolo.lower():
                return elemento
        raise ElementoNoEncontradoError(simbolo)
    def obtener_todos_los_elementos(self) -> list[Elemento]:
        return self._elementos
