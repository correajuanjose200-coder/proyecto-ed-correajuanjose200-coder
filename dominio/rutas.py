"""Rutas de los zombis: BFS sobre un grafo implícito (componente 05)."""
from dominio.mapa import PosicionInvalidaError
from estructuras.cola import Cola

# Orden fijo de vecinos: arriba, abajo, izquierda, derecha (da determinismo).
_VECINOS = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Ruta:
    """Resultado de una búsqueda: pasos, primer paso y celdas exploradas."""

    def __init__(self, distancia, siguiente, exploradas):
        self.distancia = distancia
        self.siguiente = siguiente
        self.exploradas = exploradas


def buscar_ruta(mapa, origen, destino):
    """Camino más corto de origen a destino con BFS. O(V + E) = O(filas*columnas).

    Lanza PosicionInvalidaError si algún extremo está fuera del mapa.
    Devuelve None si no hay camino. No modifica el mapa.
    """
    for f, c in (origen, destino):
        if not mapa.dentro(f, c):
            raise PosicionInvalidaError(f"posición fuera del mapa: ({f}, {c})")
    if not mapa.es_transitable(*origen) or not mapa.es_transitable(*destino):
        return None

    # Soporte interno: matriz de padres. None = celda aún no descubierta.
    padre = [[None] * mapa.columnas for _ in range(mapa.filas)]
    padre[origen[0]][origen[1]] = origen
    frontera = Cola()
    frontera.encolar(origen)
    exploradas = 1

    while not frontera.esta_vacia() and padre[destino[0]][destino[1]] is None:
        f, c = frontera.desencolar()
        for df, dc in _VECINOS:
            nf, nc = f + df, c + dc
            if (mapa.dentro(nf, nc) and padre[nf][nc] is None
                    and mapa.es_transitable(nf, nc)):
                padre[nf][nc] = (f, c)
                exploradas += 1
                frontera.encolar((nf, nc))

    if padre[destino[0]][destino[1]] is None:
        return None

    # Se camina de destino hacia origen contando pasos; la última celda
    # visitada antes de llegar al origen es el primer paso.
    distancia = 0
    siguiente = None
    paso = destino
    while paso != origen:
        siguiente = paso
        paso = padre[paso[0]][paso[1]]
        distancia += 1
    return Ruta(distancia, siguiente, exploradas)
