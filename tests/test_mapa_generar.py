"""Pruebas de Mapa.generar (M-04): CA-01, CA-02 y CA-04."""
import pytest

from dominio.mapa import Mapa

SEMILLAS = range(30)


def _hay_camino(m):
    """Ayudante de prueba: busca con DFS un camino transitable de inicio a meta."""
    pendientes = [m.inicio]
    visitadas = [[False] * m.columnas for _ in range(m.filas)]
    visitadas[m.inicio[0]][m.inicio[1]] = True
    while pendientes:
        f, c = pendientes.pop()
        if (f, c) == m.meta:
            return True
        for df, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nf, nc = f + df, c + dc
            if m.es_transitable(nf, nc) and not visitadas[nf][nc]:
                visitadas[nf][nc] = True
                pendientes.append((nf, nc))
    return False


def _iguales(a, b):
    """Ayudante de prueba: dos mapas son iguales si todas sus celdas coinciden."""
    if a.filas != b.filas or a.columnas != b.columnas:
        return False
    for f in range(a.filas):
        for c in range(a.columnas):
            if a.obtener(f, c) != b.obtener(f, c):
                return False
    return True


def test_generar_rechaza_dimensiones_menores_que_20():
    """CA-01: un mapa de menos de 20x20 lanza ValueError."""
    with pytest.raises(ValueError):
        Mapa.generar(19, 20, 1)
    with pytest.raises(ValueError):
        Mapa.generar(20, 19, 1)
    with pytest.raises(ValueError):
        Mapa.generar(5, 5, 1)


def test_generar_tamano_y_obstaculos_maximo_25_por_ciento():
    """CA-01: mide 20x20 y los obstáculos no pasan del 25 % (30 semillas)."""
    for semilla in SEMILLAS:
        m = Mapa.generar(20, 20, semilla)
        assert m.filas == 20
        assert m.columnas == 20
        assert m.proporcion_obstaculos() <= 0.25


def test_generar_siempre_hay_camino_de_pedro_a_la_meta():
    """CA-02: existe un camino transitable de inicio a meta (30 semillas)."""
    for semilla in SEMILLAS:
        assert _hay_camino(Mapa.generar(20, 20, semilla))


def test_generar_inicio_y_meta():
    """CA-02: Pedro empieza en la esquina superior izquierda y la meta E en la opuesta."""
    m = Mapa.generar(20, 20, 7)
    assert m.inicio == (0, 0)
    assert m.meta == (19, 19)
    assert m.obtener(0, 0) == "."
    assert m.obtener(19, 19) == "E"


def test_generar_hay_comida_y_agua():
    """CA-04: hay al menos una comida y un agua en celdas libres (30 semillas)."""
    for semilla in SEMILLAS:
        m = Mapa.generar(20, 20, semilla)
        assert m.contar("C") >= 1
        assert m.contar("A") >= 1
        assert m.obtener(0, 0) == "."


def test_generar_misma_semilla_mismo_mapa():
    """La misma semilla produce exactamente el mismo mapa."""
    assert _iguales(Mapa.generar(20, 20, 5), Mapa.generar(20, 20, 5))


def test_generar_semillas_distintas_mapas_distintos():
    """Semillas distintas producen mapas distintos."""
    assert not _iguales(Mapa.generar(20, 20, 1), Mapa.generar(20, 20, 2))


def test_generar_mapa_no_cuadrado():
    """CA-01 y CA-02: también funciona con 20x30."""
    m = Mapa.generar(20, 30, 3)
    assert m.filas == 20
    assert m.columnas == 30
    assert m.meta == (19, 29)
    assert _hay_camino(m)
