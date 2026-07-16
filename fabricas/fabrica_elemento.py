from typing import Any
from dataclasses import dataclass
class ElementoFabrica:
    @classmethod
    def crear_desde_diccionario(cls, diccionario: dict[str, Any]) -> Elemento:
        return Elemento(
            numero_atomico = diccionario["number"],

            simbolo = diccionario["symbol"],
            nombre = diccionario["name"],

            masa_atomica = diccionario["atomic_mass"],

            apariencia = diccionario["appearance"],

            categoria = diccionario["category"],
            fase = diccionario["phase"],

            periodo = diccionario["period"],
            grupo = diccionario["group"],
            bloque = diccionario["block"],

            columna_tabla = diccionario["ypos"],
            fila_tabla = diccionario["xpos"],

            densidad = diccionario["density"],
            punto_fusion = diccionario["melt"],
            punto_ebullicion = diccionario["boil"],
            calor_molar = diccionario["molar_heat"],

            configuracion_electronica = diccionario["electron_configuration"],
            configuracion_electronica_semantica = diccionario["electron_configuration_semantic"],

            capas_electronicas = diccionario["shells"],

            afinidad_electronica = diccionario["electron_affinity"],
            electronegatividad = diccionario["electronegativity_pauling"],

            energias_ionizacion = diccionario["ionization_energies"],

            descubierto_por = diccionario["discovered_by"],
            nombrado_por = diccionario["named_by"],
            descripcion = diccionario["summary"],

        ) 

    @classmethod
    def crear_varios(cls, lista_de_diccionarios: list[dict[str, Any]]) -> list[Elemento]:
        lista_elementos = []
        for diccionario in lista_de_diccionarios:
            elemento = cls.crear_desde_diccionario(diccionario)
            lista_elementos.append(elemento)
        return lista_elementos    

  