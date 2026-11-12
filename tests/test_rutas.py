"""Pruebas de rutas de los zombis (componente 05)."""
import pytest

from dominio.mapa import AGUA, COMIDA, OBSTACULO, Mapa, PosicionInvalidaError
from dominio.rutas import buscar_ruta


def _mapa(filas, columnas, obstaculos=()):
    m = Mapa(filas, columnas)
    for f, c in obstaculos:
        m.poner(f, c, OBSTACULO)
    return m


def _manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# --- casos triviales (R-01) ---

def test_misma_celda_distancia_cero():
    """CA-R5: origen y destino iguales dan distancia 0, sin siguiente y 1 explorada."""
    r = buscar_ruta(_mapa(5, 5), (2, 2), (2, 2))
    assert r.distancia == 0
    assert r.siguiente is None
    assert r.exploradas == 1


def test_mapa_de_una_celda():
    """CA-R5: en un mapa 1x1 la ruta de la celda a sí misma mide 0."""
    r = buscar_ruta(Mapa(1, 1), (0, 0), (0, 0))
    assert r.distancia == 0


def test_celdas_vecinas_distancia_uno():
    """CA-R2: si el destino es vecino, el primer paso es el destino."""
    r = buscar_ruta(_mapa(5, 5), (2, 2), (2, 3))
    assert r.distancia == 1
    assert r.siguiente == (2, 3)


def test_origen_fuera_del_mapa_lanza_error():
    """CA-R6: un origen fuera del mapa lanza PosicionInvalidaError."""
    with pytest.raises(PosicionInvalidaError):
        buscar_ruta(_mapa(5, 5), (-1, 0), (2, 2))
    with pytest.raises(PosicionInvalidaError):
        buscar_ruta(_mapa(5, 5), (5, 0), (2, 2))


def test_destino_fuera_del_mapa_lanza_error():
    """CA-R6: un destino fuera del mapa lanza PosicionInvalidaError."""
    with pytest.raises(PosicionInvalidaError):
        buscar_ruta(_mapa(5, 5), (2, 2), (0, 5))
    with pytest.raises(PosicionInvalidaError):
        buscar_ruta(_mapa(5, 5), (2, 2), (-1, -1))


def test_origen_en_obstaculo_da_none():
    """CA-R6: si el origen es un obstáculo no hay camino."""
    assert buscar_ruta(_mapa(5, 5, [(0, 0)]), (0, 0), (4, 4)) is None


def test_destino_en_obstaculo_da_none():
    """CA-R6: si el destino es un obstáculo no hay camino."""
    assert buscar_ruta(_mapa(5, 5, [(4, 4)]), (0, 0), (4, 4)) is None


# --- camino más corto y primer paso (R-02) ---

def test_mapa_libre_distancia_es_manhattan():
    """CA-R1: sin obstáculos la distancia es la de Manhattan."""
    r = buscar_ruta(_mapa(5, 5), (0, 0), (4, 4))
    assert r.distancia == 8


def test_pasillo_de_una_fila():
    """CA-R1: en un mapa de una fila la distancia es la diferencia de columnas."""
    r = buscar_ruta(Mapa(1, 5), (0, 0), (0, 4))
    assert r.distancia == 4
    assert r.siguiente == (0, 1)


def test_rodeo_alrededor_de_un_muro():
    """CA-R1: con un muro, la distancia es la del rodeo (12), no la de Manhattan (4)."""
    muro = [(0, 2), (1, 2), (2, 2), (3, 2)]   # hueco solo en la fila 4
    r = buscar_ruta(_mapa(5, 5, muro), (0, 0), (0, 4))
    assert r.distancia == 12


def test_siguiente_esta_a_un_paso_y_acerca_al_destino():
    """CA-R2 / CA-19: el primer paso es vecino y desde él quedan distancia-1 pasos."""
    m = _mapa(5, 5, [(0, 2), (1, 2), (2, 2), (3, 2)])
    origen, destino = (0, 0), (0, 4)
    r = buscar_ruta(m, origen, destino)
    assert _manhattan(origen, r.siguiente) == 1
    resto = buscar_ruta(m, r.siguiente, destino)
    assert resto.distancia == r.distancia - 1


def test_siguiente_nunca_es_obstaculo_ni_sale_del_mapa():
    """CA-R3 / CA-20: el primer paso es transitable y está dentro del mapa."""
    m = _mapa(5, 5, [(0, 1), (1, 0), (1, 1)])
    assert buscar_ruta(m, (0, 0), (4, 4)) is None   # (0,0) quedó encerrada
    m2 = _mapa(5, 5, [(0, 1)])
    r = buscar_ruta(m2, (0, 0), (0, 2))
    assert m2.es_transitable(*r.siguiente)
    assert r.siguiente == (1, 0)


def test_objetos_y_meta_son_transitables():
    """CA-R3: comida, agua y meta se pueden pisar al calcular la ruta."""
    m = Mapa(1, 4)
    m.poner(0, 1, COMIDA)
    m.poner(0, 2, AGUA)
    m.poner(0, 3, "E")
    r = buscar_ruta(m, (0, 0), (0, 3))
    assert r.distancia == 3


# --- sin camino (R-03) ---

def test_muro_completo_da_none():
    """CA-R4 / CA-21: con una columna entera de obstáculos no hay camino."""
    muro = [(f, 2) for f in range(5)]
    assert buscar_ruta(_mapa(5, 5, muro), (0, 0), (0, 4)) is None


def test_destino_encerrado_da_none():
    """CA-R4 / CA-21: un destino rodeado de obstáculos no se puede alcanzar."""
    rodeo = [(1, 2), (3, 2), (2, 1), (2, 3)]
    assert buscar_ruta(_mapa(5, 5, rodeo), (0, 0), (2, 2)) is None


def test_pasillo_bloqueado_en_mapa_de_una_fila():
    """CA-R4: un obstáculo en un pasillo de una fila corta el camino."""
    assert buscar_ruta(_mapa(1, 5, [(0, 2)]), (0, 0), (0, 4)) is None


# --- determinismo, exploradas y mapa intacto (R-04) ---

def test_mismas_entradas_mismo_resultado():
    """CA-R7: dos llamadas iguales dan la misma ruta (aun con empates)."""
    m = _mapa(6, 6, [(2, 2), (3, 3)])
    a = buscar_ruta(m, (0, 0), (5, 5))
    b = buscar_ruta(m, (0, 0), (5, 5))
    assert (a.distancia, a.siguiente, a.exploradas) == (b.distancia, b.siguiente, b.exploradas)


def test_exploradas_entre_uno_y_las_transitables():
    """CA-R7: exploradas nunca baja de 1 ni supera las celdas transitables."""
    m = _mapa(6, 6, [(2, 2), (3, 3), (1, 4)])
    transitables = 36 - m.contar(OBSTACULO)
    r = buscar_ruta(m, (0, 0), (5, 5))
    assert 1 <= r.exploradas <= transitables


def test_la_busqueda_no_modifica_el_mapa():
    """CA-R8: el mapa dibujado es igual antes y después de buscar."""
    m = _mapa(6, 6, [(2, 2), (3, 3)])
    antes = m.dibujar()
    buscar_ruta(m, (0, 0), (5, 5))
    buscar_ruta(m, (0, 0), (2, 2))
    assert m.dibujar() == antes


# --- mapas generados (R-05) ---

def test_hay_ruta_en_mapas_generados():
    """CA-02 / CA-R9: en mapas generados con distintas semillas siempre hay ruta."""
    for semilla in range(20):
        m = Mapa.generar(20, 20, semilla)
        r = buscar_ruta(m, m.inicio, m.meta)
        assert r is not None
        assert r.distancia >= _manhattan(m.inicio, m.meta)