from __future__ import annotations
from dataclasses import dataclass
from modelos.Validadores import ValidadorElemento
@dataclass(slots=True)
class Elemento:
    numero_atomico: int

    simbolo: str
    nombre: str

    masa_atomica: float

    apariencia: str | None

    categoria: str
    fase: str

    periodo: int
    grupo: int | None
    bloque: str

    columna_tabla: int
    fila_tabla: int

    densidad: float | None
    punto_fusion: float | None
    punto_ebullicion: float | None
    calor_molar: float | None

    configuracion_electronica: str
    configuracion_electronica_semantica: str

    capas_electronicas: list[int]

    afinidad_electronica: float | None
    electronegatividad: float | None

    energias_ionizacion: list[float]

    descubierto_por: str | None
    nombrado_por: str | None

    descripcion: str
    
def __post_init__(self):
    ValidadorElemento.validar(self)