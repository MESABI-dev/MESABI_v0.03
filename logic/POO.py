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
class Aleacion:    
    def __init__(self, nombre):
       self.nombre = nombre
       self.componentes = []
    def agregar_elemento(self, elemento_objeto, porcentaje):
       if not isinstance(elemento_objeto, Elemento):
          print("Error")
          return False
       self.componentes.append({
          "elemento": elemento_objeto,
          "porcentaje": float(porcentaje),
       })
       return True  
    def validar_composicion(self):
       total = sum(comp["porcentaje"] for comp in self.componentes)
       return total == 100
    def obtener_reporte(self):
       reporte = f"=== Ficha de aleación: {self.nombre} ===\n"
       reporte += "Composicion química: \n"
       for c in self.componentes:
          objetos_elemento = c["elemento"]
          porcentaje = c["porcentaje"]       
          reporte += f"[{objetos_elemento.simbolo}] {objetos_elemento.nombre}: {porcentaje}%\n"  
       reporte += f"Suma total verificada: {sum(comp['porcentaje'] for comp in self.componentes)}%\n"
       return reporte
    def obtener_elemento(self, elemento_deseado):
       for e in self.componentes:
          elemento = e["elemento"]
          if elemento == elemento_deseado or elemento.simbolo == elemento_deseado:
             return elemento
       
hierro = Elemento("Hierro", "Fe", 26, 55.845, 7.874)
oro = Elemento("Oro", "Au", 79, 196.967, 19.300)
titanio = Elemento("Titanio", "Ti", 22, 47.867, 4.506)  
carbono = Elemento("Carbono", "C", 6 , 12.011, 2.267)
cobre = Elemento("Cobre","Cu", 29 , 63.546, 8.960)
estano = Elemento("Estaño","Sn", 50 , 118.710, 7.310)

acero = Aleacion("Acero Carbono Estándar")
acero.agregar_elemento(hierro, 98.5)
acero.agregar_elemento(carbono, 1.5)

bronce = Aleacion("Bronce de Fundición")
bronce.agregar_elemento(cobre, 88.0)
bronce.agregar_elemento(estano, 12.0)

#acero.obtener_elemento("iron")

print(acero.obtener_reporte())
print("\n")
print(bronce.obtener_reporte()) 