class Material:
    def __init__(self, nombre, densidad, estado):
        self.nombre = nombre
        self.densidad = densidad
        self.estado = estado
    def obtener_reporte(self):
        return (
            f"===== MATERIAL =====\n"
            f"Nombre: {self.nombre.upper()}\n"
            f"Densidad: {self.densidad}g/cm³\n"
            f"Estado: {self.estado}\n"
        )
class Elemento(Material):
    def __init__(self, nombre, densidad, estado, simbolo, numero_atomico):
        super().__init__(nombre, densidad, estado)
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
    def obtener_reporte(self):
        reporte_padre = super().obtener_reporte()
        reporte_hijo =(
            f"simbolo: {self.simbolo}\n"
            f"Numero atomico: {self.numero_atomico}\n"  
        )
        return reporte_padre + reporte_hijo

class Aleacion(Material):
    def __init__(self, nombre, densidad=0.0, estado="Solido"):
        super().__init__(nombre, densidad, estado) 
        self.componentes = []

    def agregar_componente(self, elemento_objeto, porcentaje):
        self.componentes.append({
            "elemento": elemento_objeto,
            "porcentaje": float(porcentaje)
        })    

    def obtener_reporte(self):   
        suma_porcentajes = sum(comp['porcentaje'] for comp in self.componentes)
        if suma_porcentajes != 100.0:
            return f"Error: La aleación '{self.nombre}' no cumple con los porcentajes (Suma actual: {suma_porcentajes}%)."

        reporte_material = super().obtener_reporte()
        reporte_componentes = "Componentes:\n"
        
        for c in self.componentes:
            objeto_elemento = c["elemento"]
            porcentaje = c["porcentaje"]       
            reporte_componentes += f"  - [{objeto_elemento.simbolo}] {objeto_elemento.nombre}: {porcentaje}%\n"  
        
        reporte_componentes += f"Suma total verificada: {suma_porcentajes}%\n"
        return reporte_material + reporte_componentes

hierro = Elemento("Hierro", 55.845, "Solido", "Fe", 26)
oro = Elemento("Oro", 196.967, "Solido", "Au", 79)
titanio = Elemento("Titanio", 47.867, "Solido", "Ti", 22)  
carbono = Elemento("Carbono",12.011, "Solido", "C", 6)
cobre = Elemento("Cobre", 63.546, "Solido", "Cu", 29)
estaño = Elemento("Estaño", 118.710, "Solido", "Sn", 50)

acero = Aleacion("Acero Carbono Estándar")
acero.agregar_componente(hierro, 98.5,)
acero.agregar_componente(carbono, 1.5,)

bronce = Aleacion("Bronce de Fundición")
bronce.agregar_componente(cobre, 88.0,)
bronce.agregar_componente(estaño, 12.0,)

random = Aleacion ("RANDOM")
random.agregar_componente(oro, 67,)
random.agregar_componente(carbono, 15,)
random.agregar_componente(titanio, 17.5,)
random.agregar_componente(cobre, .5,)

materiales = [
    hierro, oro, acero, titanio, cobre, bronce, estaño, carbono, random
]

for m in materiales:
    print(m.obtener_reporte())
   
#No deberia modificar ningna clase
