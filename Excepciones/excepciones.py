from typing import Any
class MesabiError(Exception):
    """Clase base para todas las excepciones de Mesabi."""
    pass

class ValidacionError(MesabiError):
    """Errores relacionados con la validacion de datos"""

class ArchivosError(MesabiError):   #=====Temporal vaya mierda=====
    """Errores relacionados con archivos"""

class ValorInvalidoError(ValidacionError):
    """Se lanza cuando un valor no cumple las reglas de validación."""
    def __init__(self, campo: str, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(
            f"El valor {valor} no es válido para el campo {campo}."
        )

class ArchivoNoEncontradoError(ArchivosError):
    def __init__(self, ruta: str):
        self.ruta = ruta
        super().__init__(f"Archivo {ruta} no encontrado")

class ArchivoJsonInvalido(ArchivosError):
    def __init__(self, ruta: str):
        self.ruta = ruta
        super().__init__(f"El Archivo {ruta} no es válido")        