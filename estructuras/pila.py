"""Pila (LIFO) construida con nodos enlazados, sin usar list."""
from estructuras.nodo import Nodo


class PilaVaciaError(Exception):
    """Se intentó leer o quitar un elemento de una pila vacía."""


class Pila:
    """Pila: lo último que entra es lo primero que sale.

    Complejidad de las operaciones públicas:
        apilar() O(1) · desapilar() O(1) · cima() O(1)
        esta_vacia() O(1) · tamano() O(1) · vaciar() O(1) amortizado
    """

    def __init__(self):
        self._cima = None      # nodo de arriba; None si la pila está vacía
        self._tamano = 0       # contador para que tamano() sea O(1)

    def esta_vacia(self):
        """Verdadero si no hay elementos. O(1)."""
        return self._tamano == 0

    def tamano(self):
        """Cantidad de elementos. O(1)."""
        return self._tamano

    def apilar(self, dato):
        """Pone un elemento arriba de la pila. O(1)."""
        self._cima = Nodo(dato, self._cima)
        self._tamano += 1

    def cima(self):
        """Devuelve el elemento de arriba sin quitarlo. O(1).

        Lanza PilaVaciaError si la pila está vacía.
        """
        if self._cima is None:
            raise PilaVaciaError("La pila está vacía")
        return self._cima.dato

    def desapilar(self):
        """Quita y devuelve el elemento de arriba. O(1).

        Lanza PilaVaciaError si la pila está vacía.
        """
        if self._cima is None:
            raise PilaVaciaError("La pila está vacía")
        nodo = self._cima
        self._cima = nodo.siguiente
        self._tamano -= 1
        return nodo.dato
    def vaciar(self):
        """Quita todos los elementos. O(1) amortizado.

        Solo suelta la referencia a la cima; Python libera los nodos
        que quedaron sin uso (ver plan.md, 'vaciar deshechas').
        """
        self._cima = None
        self._tamano = 0
