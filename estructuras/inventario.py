"""Inventario: lista enlazada simple con referencia al último nodo."""
from estructuras.nodo import Nodo


class InventarioLlenoError(Exception):
    """Se intentó agregar o insertar con el inventario lleno."""


class PosicionInventarioError(Exception):
    """La posición pedida no existe en el inventario."""


class Inventario:
    """Objetos de Pedro en orden de recogida, con capacidad máxima.

    Las posiciones cuentan desde 0. Con n ≤ capacidad (5 por defecto):
        agregar() O(1) · insertar() O(n) · quitar() O(n) · listar() O(n)
        tamano() O(1) · esta_vacio() O(1) · esta_lleno() O(1)
    """

    def __init__(self, capacidad=5):
        """Crea un inventario vacío. Lanza ValueError si capacidad < 1. O(1)."""
        if capacidad < 1:
            raise ValueError("La capacidad debe ser al menos 1")
        self._capacidad = capacidad
        self._primero = None   # primer nodo; None si está vacío
        self._ultimo = None    # último nodo; permite agregar en O(1)
        self._tamano = 0

    def tamano(self):
        """Cantidad de objetos. O(1)."""
        return self._tamano

    def esta_vacio(self):
        """Verdadero si no hay objetos. O(1)."""
        return self._tamano == 0

    def esta_lleno(self):
        """Verdadero si el tamaño alcanzó la capacidad. O(1)."""
        return self._tamano >= self._capacidad

    def agregar(self, objeto):
        """Pone un objeto al final. O(1).

        Lanza InventarioLlenoError si está lleno.
        """
        if self.esta_lleno():
            raise InventarioLlenoError("El inventario está lleno")
        nodo = Nodo(objeto)
        if self._ultimo is None:
            self._primero = nodo
        else:
            self._ultimo.siguiente = nodo
        self._ultimo = nodo
        self._tamano += 1

    def insertar(self, posicion, objeto):
        """Pone un objeto en la posición dada (0 a tamano()). O(n).

        Lanza InventarioLlenoError si está lleno y PosicionInventarioError
        si la posición está fuera de rango.
        """
        if self.esta_lleno():
            raise InventarioLlenoError("El inventario está lleno")
        if posicion < 0 or posicion > self._tamano:
            raise PosicionInventarioError(f"Posición inválida: {posicion}")
        if posicion == self._tamano:      # incluye el inventario vacío
            self.agregar(objeto)
            return
        if posicion == 0:
            self._primero = Nodo(objeto, self._primero)
        else:
            anterior = self._nodo_en(posicion - 1)
            anterior.siguiente = Nodo(objeto, anterior.siguiente)
        self._tamano += 1

    def quitar(self, posicion):
        """Quita y devuelve el objeto de la posición dada (0 a tamano()-1). O(n).

        Lanza PosicionInventarioError si está vacío o la posición no existe.
        """
        if posicion < 0 or posicion >= self._tamano:
            raise PosicionInventarioError(f"Posición inválida: {posicion}")
        if posicion == 0:
            nodo = self._primero
            self._primero = nodo.siguiente
            if self._primero is None:
                self._ultimo = None
        else:
            anterior = self._nodo_en(posicion - 1)
            nodo = anterior.siguiente
            anterior.siguiente = nodo.siguiente
            if nodo is self._ultimo:
                self._ultimo = anterior
        self._tamano -= 1
        return nodo.dato

    def listar(self):
        """Entrega los objetos en orden de recogida, sin modificarlos. O(n)."""
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def _nodo_en(self, posicion):
        """Nodo en la posición dada (ya validada). O(n)."""
        actual = self._primero
        for _ in range(posicion):
            actual = actual.siguiente
        return actual