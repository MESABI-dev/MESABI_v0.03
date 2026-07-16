import json
from excepciones.excepciones import ArchivoJsonInvalido, ArchivoNoEncontradoError
from config.rutas import RUTA_ELEMENTOS
from pathlib import Path

class CargadorJson:
    def __init__(self, ruta_json: Path | str):
        self._ruta_json = Path(ruta_json)
    def cargar(self) -> list[dict]:
        try:
            with open(self._ruta_json, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            raise ArchivoNoEncontradoError(self._ruta_json)
        except json.JSONDecodeError:
            raise ArchivoJsonInvalido(self._ruta_json)
        return datos
    
"""   
cargador = CargadorJson(RUTA_ELEMENTOS)
datos = cargador.cargar()
print(type(datos))
print(type(datos[0]))
"""