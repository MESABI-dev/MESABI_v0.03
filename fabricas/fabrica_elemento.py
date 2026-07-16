from repositorios.cargadores import datos

class ElementoFabrica:
    @classmethod
    def crear_desde_diccionario(cls, datos: list) -> dict:
        return cls(
            numero_atomico = datos["number"],

            simbolo = datos["symbol"],
            nombre = datos["name"],

            masa_atomica = datos["atomic_mass"],

            apariencia = datos["appearance"],

            categoria = datos["category"],
            fase = datos["phase"],

            periodo = datos["period"],
            grupo = datos["group"],
            bloque = datos["block"],

            columna_tabla = datos["ypos"],
            fila_tabla = datos["xpos"],

            densidad = datos["density"],
            punto_fusion = datos["melt"],
            punto_ebullicion = datos["boil"],
            calor_molar = datos["molar_heat"],

            configuracion_electronica = datos["electron_configuration"],
            configuracion_electronica_semantica = datos["electron_configuration_semantic"],

            capas_electronicas = datos["shells"],

            afinidad_electronica = datos["electron_affinity"],
            electronegatividad = datos["electronegativity_pauling"],

            energias_ionizacion = datos["ionization_energies"],

            descubierto_por = datos["discovered_by"],
            nombrado_por = datos["named_by"],
            descripcion = datos["summary"],

        ) 
