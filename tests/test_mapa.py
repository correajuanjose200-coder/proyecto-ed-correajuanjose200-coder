"""Pruebas de Mapa (M-01 a M-05). Cada prueba nombra el criterio que verifica."""
import pytest

from dominio.mapa import Mapa, PosicionInvalidaError


def test_mapa_nuevo_tiene_todas_las_celdas_libres():
    """CA-M3 (base): un mapa nuevo está libre en todas sus celdas."""
    m = Mapa(3, 4)
    assert m.filas == 3
    assert m.columnas == 4
    for f in range(3):
        for c in range(4):
            assert m.obtener(f, c) == "."


def test_mapa_de_una_celda():
    """Caso extremo: el mapa más pequeño posible es de 1×1."""
    m = Mapa(1, 1)
    assert m.obtener(0, 0) == "."


def test_mapa_rechaza_dimensiones_menores_que_uno():
    """Caso extremo: filas o columnas menores que 1 lanzan ValueError."""
    with pytest.raises(ValueError):
        Mapa(0, 5)
    with pytest.raises(ValueError):
        Mapa(5, 0)
    with pytest.raises(ValueError):
        Mapa(-1, 5)


def test_dentro_en_las_esquinas():
    """CA-M1: las cuatro esquinas están dentro."""
    m = Mapa(3, 4)
    assert m.dentro(0, 0)
    assert m.dentro(0, 3)
    assert m.dentro(2, 0)
    assert m.dentro(2, 3)


def test_dentro_un_paso_fuera_de_cada_borde():
    """CA-M1: un paso fuera de cada borde no está dentro."""
    m = Mapa(3, 4)
    assert not m.dentro(-1, 0)
    assert not m.dentro(3, 0)
    assert not m.dentro(0, -1)
    assert not m.dentro(0, 4)


def test_poner_y_obtener():
    """CA-M3: lo que se pone es lo que se obtiene."""
    m = Mapa(3, 3)
    m.poner(1, 2, "#")
    assert m.obtener(1, 2) == "#"


def test_poner_no_cambia_otras_celdas():
    """CA-M3: poner en una celda no modifica las demás."""
    m = Mapa(3, 3)
    m.poner(1, 1, "C")
    assert m.obtener(0, 0) == "."
    assert m.obtener(1, 0) == "."
    assert m.obtener(1, 2) == "."
    assert m.obtener(2, 2) == "."


def test_poner_sobrescribe_la_celda():
    """CA-M3: poner de nuevo reemplaza el símbolo anterior."""
    m = Mapa(2, 2)
    m.poner(0, 0, "C")
    m.poner(0, 0, ".")
    assert m.obtener(0, 0) == "."


def test_obtener_fuera_lanza_error():
    """CA-M4: obtener fuera del mapa lanza PosicionInvalidaError."""
    m = Mapa(3, 3)
    with pytest.raises(PosicionInvalidaError):
        m.obtener(3, 0)
    with pytest.raises(PosicionInvalidaError):
        m.obtener(0, -1)


def test_poner_fuera_lanza_error():
    """CA-M4: poner fuera del mapa lanza PosicionInvalidaError."""
    m = Mapa(3, 3)
    with pytest.raises(PosicionInvalidaError):
        m.poner(5, 5, "#")


def test_poner_simbolo_invalido_lanza_error_y_no_cambia():
    """CA-M5: un símbolo desconocido lanza ValueError y no cambia el mapa."""
    m = Mapa(3, 3)
    with pytest.raises(ValueError):
        m.poner(1, 1, "X")
    assert m.obtener(1, 1) == "."
