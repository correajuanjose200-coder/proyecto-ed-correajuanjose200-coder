"""Mapa de la ciudad: matriz densa de celdas (filas x columnas)."""
import random

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
        es_transitable() O(1) · contar() O(filas x columnas)
        proporcion_obstaculos() O(filas x columnas)
        generar() O(filas x columnas) en promedio
        dibujar() O(filas x columnas + marcas)
    Crear un mapa es O(filas x columnas).
    """

    def __init__(self, filas, columnas):
        if filas < 1 or columnas < 1:
            raise ValueError("El mapa necesita al menos 1 fila y 1 columna")
        self.filas = filas
        self.columnas = columnas
        self.inicio = None   # celda de inicio de Pedro (la fija generar)
        self.meta = None     # celda del aeropuerto (la fija generar)
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

    def contar(self, simbolo):
        """Cuántas celdas tienen ese símbolo. O(filas x columnas).

        Lanza ValueError si el símbolo no es válido.
        """
        if simbolo not in SIMBOLOS_VALIDOS:
            raise ValueError(f"Símbolo desconocido: {simbolo}")
        total = 0
        for fila in self._celdas:
            for celda in fila:
                if celda == simbolo:
                    total += 1
        return total

    def proporcion_obstaculos(self):
        """Fracción de celdas que son obstáculo, entre 0 y 1. O(filas x columnas)."""
        return self.contar(OBSTACULO) / (self.filas * self.columnas)

    @classmethod
    def generar(cls, filas, columnas, semilla):
        """Crea un mapa listo para jugar. O(filas x columnas) en promedio.

        Pedro empieza en la esquina (0, 0) y el aeropuerto queda en la
        esquina opuesta. Primero se abre un corredor libre entre ambos
        (CA-02) y los obstáculos se colocan solo fuera de él. Con la misma
        semilla se obtiene el mismo mapa.

        Lanza ValueError si filas o columnas son menores que 20.
        """
        if filas < 20 or columnas < 20:
            raise ValueError("El mapa debe medir al menos 20x20")
        azar = random.Random(semilla)
        mapa = cls(filas, columnas)
        mapa.inicio = (0, 0)
        mapa.meta = (filas - 1, columnas - 1)

        # 1) Corredor: camino que solo baja o avanza a la derecha.
        reservada = [[False] * columnas for _ in range(filas)]
        f, c = 0, 0
        reservada[f][c] = True
        while (f, c) != mapa.meta:
            if f == filas - 1:
                c += 1
            elif c == columnas - 1:
                f += 1
            elif azar.random() < 0.5:
                f += 1
            else:
                c += 1
            reservada[f][c] = True

        # 2) Obstáculos: el 20 % de las celdas, solo fuera del corredor.
        objetivo = int(filas * columnas * 0.20)
        puestos = 0
        while puestos < objetivo:
            f = azar.randrange(filas)
            c = azar.randrange(columnas)
            if not reservada[f][c] and mapa.obtener(f, c) == LIBRE:
                mapa.poner(f, c, OBSTACULO)
                puestos += 1

        # 3) Meta y objetos: 3 comidas y 3 aguas en celdas libres.
        mapa.poner(mapa.meta[0], mapa.meta[1], META)
        for simbolo in (COMIDA, AGUA):
            puestos = 0
            while puestos < 3:
                f = azar.randrange(filas)
                c = azar.randrange(columnas)
                if mapa.obtener(f, c) == LIBRE and (f, c) != mapa.inicio:
                    mapa.poner(f, c, simbolo)
                    puestos += 1
        return mapa

    def dibujar(self, marcas=()):
        """Devuelve el mapa como texto, una línea por fila.

        O(filas x columnas + marcas). `marcas` es una secuencia de
        (fila, columna, símbolo), por ejemplo Pedro y los zombis, que se
        dibujan encima del terreno sin modificar el mapa.

        Lanza PosicionInvalidaError si una marca está fuera del mapa.
        """
        # Copia temporal del terreno (soporte interno): el mapa no cambia.
        copia = [fila[:] for fila in self._celdas]
        for f, c, simbolo in marcas:
            if not self.dentro(f, c):
                raise PosicionInvalidaError(f"Marca fuera del mapa: ({f}, {c})")
            copia[f][c] = simbolo
        return "\n".join("".join(fila) for fila in copia)
