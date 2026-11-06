"""Historial de acciones del jugador: deshacer y rehacer con dos pilas."""
from estructuras.pila import Pila, PilaVaciaError


class Historial:
    """Recuerda las acciones para poder revertirlas y reaplicarlas.

    Usa dos pilas: *hechas* (se pueden deshacer; la cima es la más reciente)
    y *deshechas* (se pueden rehacer; la cima es la última deshecha).

    Complejidad de las operaciones públicas:
        registrar() O(1) · cantidad() O(1)
        hay_deshacer() O(1) · hay_rehacer() O(1)
    """

    def __init__(self):
        self._hechas = Pila()
        self._deshechas = Pila()

    def registrar(self, accion):
        """Guarda una acción ya aplicada como la más reciente. O(1)."""
        self._hechas.apilar(accion)
        self._deshechas.vaciar()

    def cantidad(self):
        """Número de acciones que se pueden deshacer. O(1)."""
        return self._hechas.tamano()

    def hay_deshacer(self):
        """Verdadero si hay al menos una acción para deshacer. O(1)."""
        return not self._hechas.esta_vacia()

    def hay_rehacer(self):
        """Verdadero si hay al menos una acción para rehacer. O(1)."""
        return not self._deshechas.esta_vacia()

    def deshacer(self):
        """Devuelve la acción más reciente y la pasa a 'deshechas'. O(1).

        Si no hay nada que deshacer devuelve None y no cambia el estado (CA-18).
        """
        try:
            accion = self._hechas.desapilar()
        except PilaVaciaError:
            return None
        self._deshechas.apilar(accion)
        return accion

    def rehacer(self):
        """Devuelve la última acción deshecha y la vuelve a 'hechas'. O(1).

        Si no hay nada que rehacer devuelve None y no cambia el estado (CA-18).
        """
        try:
            accion = self._deshechas.desapilar()
        except PilaVaciaError:
            return None
        self._hechas.apilar(accion)
        return accion
