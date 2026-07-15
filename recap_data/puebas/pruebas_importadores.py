from recap_data.importadores.base_importador import Importador


class ImportadorPrueba(Importador):

    def abrir(self):
        print("Abriendo...")

    def obtener_registros(self):
        yield {
            "nombre": "AISI 4140",
            "densidad": 7.85
        }

        yield {
            "nombre": "AISI 1045",
            "densidad": 7.86
        }

    def convertir_registro(self, registro):
        return registro

    def cerrar(self):
        print("Cerrando...")

    
    
