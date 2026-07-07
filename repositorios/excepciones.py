class MesabiError(Exception):
    """Clase base para todas las excepciones de Mesabi."""
    pass
class ElementoNoEncontradoError(MesabiError):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mensaje = f"Elemento '{self.nombre}' no encontrado en la base de datos."
        super().__init__(self.mensaje)

class ArchivoNoEncontradoError(MesabiError):
    def __init__(self, ruta: str):
        self.ruta = ruta
        self.mensaje =  f"Archivo {self.ruta} no encontrado."
        return super().__init__(self.mensaje)