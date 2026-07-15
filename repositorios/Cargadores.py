import json
from Excepciones.excepciones import ArchivoJsonInvalido, ArchivoNoEncontradoError
from Config.rutas import RUTA_ELEMENTOS

class CargadorJson:
    def __init__(self, ruta_json):
        self._ruta_json : str = ruta_json
    def cargar(self) -> list[dict]:
        try:
            with open(self._ruta_json, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            raise ArchivoNoEncontradoError(self._ruta_json)
        except json.JSONDecodeError:
            raise ArchivoJsonInvalido(self._ruta_json)
        return datos
cargador = CargadorJson(RUTA_ELEMENTOS)
datos = cargador.cargar()
