"""Cola (FIFO) construida con nodos enlazados, sin usar list."""
from estructuras.nodo import Nodo


class ColaVaciaError(Exception):
    """Se intentó leer o quitar un elemento de una cola vacía."""


class Cola:
    """Cola: el primero que entra es el primero que sale.

    Complejidad de las operaciones públicas:
        encolar() O(1) · desencolar() O(1) · frente() O(1)
        esta_vacia() O(1) · tamano() O(1) · vaciar() O(1) amortizado
    """

    def __init__(self):
        self._primero = None   # nodo del frente; None si está vacía
        self._ultimo = None    # nodo del final; permite encolar en O(1)
        self._tamano = 0

    def esta_vacia(self):
        """Verdadero si no hay elementos. O(1)."""
        return self._tamano == 0

    def tamano(self):
        """Cantidad de elementos. O(1)."""
        return self._tamano

    def encolar(self, dato):
        """Pone un elemento al final de la cola. O(1)."""
        nodo = Nodo(dato)
        if self._ultimo is None:
            self._primero = nodo
        else:
            self._ultimo.siguiente = nodo
        self._ultimo = nodo
        self._tamano += 1

    def frente(self):
        """Devuelve el elemento del frente sin quitarlo. O(1).

        Lanza ColaVaciaError si la cola está vacía.
        """
        if self._primero is None:
            raise ColaVaciaError("La cola está vacía")
        return self._primero.dato

    def desencolar(self):
        """Quita y devuelve el elemento del frente. O(1).

        Lanza ColaVaciaError si la cola está vacía.
        """
        if self._primero is None:
            raise ColaVaciaError("La cola está vacía")
        nodo = self._primero
        self._primero = nodo.siguiente
        if self._primero is None:
            self._ultimo = None
        self._tamano -= 1
        return nodo.dato

    def vaciar(self):
        """Quita todos los elementos. O(1) amortizado.

        Solo suelta las referencias; Python libera los nodos sin uso.
        """
        self._primero = None
        self._ultimo = None
        self._tamano = 0
