class Elemento:
    def __init__(self, nombre, simbolo, numero_atomico, masa, densidad):
        self.nombre = nombre
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
        self.masa = masa
        self.densidad = densidad

    def obtener_texto(self):
        return (
            f"===== Ficha Técnica: {self.nombre.upper()} =====\n"
            f"Símbolo: {self.simbolo}\n"
            f"Número atómico: {self.numero_atomico}\n"
            f"Masa atómica: {self.masa}\n"
            f"Densidad: {self.densidad}g/cm³\n"
        )
    def comparar(self, otro_elemento):
        if not isinstance(otro_elemento, Elemento):
         return "Error"
        if self.densidad > otro_elemento.densidad:
           ganador_densidad = self.nombre
           diferencia_densidad = self.densidad - otro_elemento.densidad
           frase_densidad = f"{ganador_densidad} es mas denso por {diferencia_densidad:.3f} g/cm³."
        elif self.densidad < otro_elemento.densidad:
           ganador_densidad = otro_elemento.nombre
           diferencia_densidad = otro_elemento.densidad - self.densidad
           frase_densidad = f"{ganador_densidad} es más denso por {diferencia_densidad:.3f} g/cm³." 
        else:
           frase_densidad = "Ambos elementos tienen la misma densidad"
        reporte = (
           f"=== Comparación: {self.nombre} - {otro_elemento.nombre} ===\n"
           f"1.Densidades: {self.simbolo}({self.densidad}) - {otro_elemento.simbolo}({otro_elemento.densidad})\n"
           f"Resultado: {frase_densidad}\n"
           f"2.El mas pesado (Masa):"
           f"{self.nombre if self.masa > otro_elemento.masa else otro_elemento.nombre}\n"
           f"=================================================="
        )   
        return reporte
    
hierro = Elemento("Hierro", "Fe", 26, 55.845, 7.874)
oro = Elemento("Oro", "Au", 79, 196.967, 19.300)
titanio = Elemento("Titanio", "Ti", 22, 47.867, 4.506)    
print(titanio.obtener_texto())
print("\n")

resultado_1 = hierro.compar8ar(oro)
print(resultado_1)
print("\n")

resultado_2 = titanio.comparar(oro)
print(resultado_2) 
print("\n")