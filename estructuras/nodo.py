"""Nodo enlazado: pieza base de pilas, colas y listas del proyecto."""


class Nodo:
    """Guarda un dato y una referencia al siguiente nodo.

    Complejidad: crear un nodo es O(1).
    """

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
        