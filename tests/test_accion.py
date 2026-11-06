"""Pruebas de Accion (T-05): el registro de datos que guarda el historial."""
import pytest

from dominio.accion import Accion


def _crear(tipo="mover", objeto=None):
    return Accion(
        tipo,
        pedro_antes=(3, 4, 100),
        pedro_despues=(3, 5, 100),
        zombis_antes=((1, 0, 0), (2, 9, 9)),
        zombis_despues=((1, 0, 1), (2, 9, 8)),
        turno_antes=7,
        turno_despues=8,
        objeto=objeto,
    )


def test_accion_guarda_sus_datos():
    """CA-14 y CA-15 (datos): guarda el estado de antes y de después."""
    a = _crear()
    assert a.tipo == "mover"
    assert a.pedro_antes == (3, 4, 100)
    assert a.pedro_despues == (3, 5, 100)
    assert a.zombis_antes == ((1, 0, 0), (2, 9, 9))
    assert a.zombis_despues == ((1, 0, 1), (2, 9, 8))
    assert a.turno_antes == 7
    assert a.turno_despues == 8


def test_accion_objeto_es_opcional():
    """CA-15 (datos): sin objeto queda en None; al recoger guarda el objeto."""
    assert _crear().objeto is None
    assert _crear("recoger", objeto="vacuna").objeto == "vacuna"


def test_accion_acepta_cero_zombis():
    """Caso extremo: una partida sin zombis vivos también se registra."""
    a = Accion(
        "esperar",
        pedro_antes=(0, 0, 50),
        pedro_despues=(0, 0, 50),
        zombis_antes=(),
        zombis_despues=(),
        turno_antes=0,
        turno_despues=1,
    )
    assert a.zombis_antes == ()
    assert a.zombis_despues == ()


def test_accion_rechaza_tipo_desconocido():
    """Caso extremo: un tipo que no está en la spec lanza ValueError."""
    with pytest.raises(ValueError):
        _crear("volar")
