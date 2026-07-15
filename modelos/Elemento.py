from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True)
class Elemento:
    nombre: str
    simbolo: str
    numero_atomico: int

    masa_atomica:float  #g/mol
    densidad: float | None  #g/cm³
    punto_de_fusion: float | None   #°K

    categoria: CategoriaElemento
    estado: EstadoMateria
    grupo: GrupoElemento
    periodo: PeriodoElemento
    
def __post_init__(self):
    ValidadorElemento.validar(self)