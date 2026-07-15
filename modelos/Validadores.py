#from Elemento import Elemento
from Excepciones.excepciones import ValorInvalidoError
class Elemento: # Clase Elemento para Probar wey
   def __init__(self, nombre):
      self.nombre = nombre

class ValidadorElemento:
    @classmethod 
    def validar(cls, elemento: Elemento) -> None:
        cls._validar_nombre(elemento)
        cls._validar_simbolo(elemento)
        cls._validar_numero_atomico(elemento)
        cls._validar_masa_atomica(elemento)
        cls._validar_densidad(elemento)
        cls._validar_punto_fusion(elemento)
        cls._validar_estado(elemento)
        cls._validar_categoria(elemento)
        cls._validar_grupo(elemento)
        cls._validar_periodo(elemento)
    @staticmethod    
    def _validar_nombre(elemento: Elemento) -> None:
         if not isinstance(elemento.nombre, str):
            raise ValorInvalidoError("nombre", elemento.nombre)
         if not elemento.nombre.strip():
            raise ValorInvalidoError("nombre", elemento.nombre)
    @staticmethod   
    def _validar_simbolo(elemento: Elemento) -> None:
        if not isinstance(elemento.simbolo, str):
            raise ValorInvalidoError("simbolo", elemento.simbolo)
        if not elemento.simbolo.strip():
            raise ValorInvalidoError("simbolo", elemento.simbolo)
    @staticmethod
    def _validar_numero_atomico(elemento: Elemento) -> None:
        if not isinstance(elemento.numero_atomico, int):
            raise ValorInvalidoError("numero_atomico", elemento.numero_atomico)
        if elemento.numero_atomico < 1 or elemento.numero_atomico > 119:
            raise ValorInvalidoError("numero_atomico", elemento.numero_atomico)
        



          
         

Elemento(nombre="")
ValidadorElemento._validar_nombre(Elemento(nombre="4s"))