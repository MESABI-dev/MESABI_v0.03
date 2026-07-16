import json
from excepciones.excepciones import (ElementoNoEncontradoError, ArchivoNoEncontradoError)
from modelos.elemento import Elemento
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
