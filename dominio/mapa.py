"""Mapa de la ciudad: matriz densa de celdas (filas x columnas)."""

LIBRE = "."
OBSTACULO = "#"
META = "E"
COMIDA = "C"
AGUA = "A"
SIMBOLOS_VALIDOS = (LIBRE, OBSTACULO, META, COMIDA, AGUA)


class PosicionInvalidaError(Exception):
    """La posición pedida está fuera del mapa."""


class Mapa:
    """Rejilla de filas x columnas; cada celda guarda un símbolo del terreno.

    Complejidad de las operaciones públicas:
        dentro() O(1) · obtener() O(1) · poner() O(1)
    Crear un mapa es O(filas x columnas).
    """

    def __init__(self, filas, columnas):
        if filas < 1 or columnas < 1:
            raise ValueError("El mapa necesita al menos 1 fila y 1 columna")
        self.filas = filas
        self.columnas = columnas
        # Soporte interno declarado en plan.md: list como contenedor de
        # tamaño fijo. No se usa append ni pop.
        self._celdas = [[LIBRE] * columnas for _ in range(filas)]

    def dentro(self, f, c):
        """Verdadero si (f, c) está dentro del mapa. O(1)."""
        return 0 <= f < self.filas and 0 <= c < self.columnas

    def obtener(self, f, c):
        """Símbolo de la celda (f, c). O(1).

        Lanza PosicionInvalidaError si está fuera del mapa.
        """
        if not self.dentro(f, c):
            raise PosicionInvalidaError(f"Posición fuera del mapa: ({f}, {c})")
        return self._celdas[f][c]

    def poner(self, f, c, simbolo):
        """Pone un símbolo en la celda (f, c). O(1).

        Lanza PosicionInvalidaError si está fuera del mapa y ValueError
        si el símbolo no es válido.
        """
        if not self.dentro(f, c):
            raise PosicionInvalidaError(f"Posición fuera del mapa: ({f}, {c})")
        if simbolo not in SIMBOLOS_VALIDOS:
            raise ValueError(f"Símbolo desconocido: {simbolo}")
        self._celdas[f][c] = simbolo

    def es_transitable(self, f, c):
        """Verdadero si (f, c) está dentro del mapa y no es obstáculo. O(1)."""
        return self.dentro(f, c) and self._celdas[f][c] != OBSTACULO
