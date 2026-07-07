from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Iterator


class Importador(ABC):
    def importar(self) -> Iterator[Any]:
        self.abrir(self.archivo)
        try:
            for registro in self.obtener_registros():
                yield self.convertir_registro(registro)
        finally:
            self.cerrar()

    @abstractmethod
    def abrir(self) -> None :
        pass

    @abstractmethod
    def obtener_registros(self) -> Iterator[Dict[str, Any]]:
        pass

    @abstractmethod
    def convertir_registro(self, registro: Dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def cerrar(self) -> None:
        pass