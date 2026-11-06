"""Pruebas de Historial (T-06 a T-09). Cada prueba nombra el criterio que verifica."""
from dominio.accion import Accion
from dominio.historial import Historial


def _accion(n=0):
    """Acción de prueba; n la distingue de las demás (se guarda en turno_antes)."""
    return Accion(
        "mover",
        pedro_antes=(0, 0, 100),
        pedro_despues=(0, 1, 100),
        zombis_antes=(),
        zombis_despues=(),
        turno_antes=n,
        turno_despues=n + 1,
    )


def test_historial_nuevo_esta_vacio():
    """CA-H3: un historial nuevo tiene cantidad 0 y nada que deshacer ni rehacer."""
    h = Historial()
    assert h.cantidad() == 0
    assert not h.hay_deshacer()
    assert not h.hay_rehacer()


def test_registrar_una_accion():
    """CA-H3: registrar una acción sube la cantidad a 1 y habilita deshacer."""
    h = Historial()
    h.registrar(_accion())
    assert h.cantidad() == 1
    assert h.hay_deshacer()
    assert not h.hay_rehacer()


def test_registrar_varias_acciones():
    """CA-H3: cada registro sube la cantidad en 1."""
    h = Historial()
    for n in range(3):
        h.registrar(_accion(n))
    assert h.cantidad() == 3


def test_deshacer_orden_inverso():
    """CA-14, CA-H1: N deshacer sucesivos devuelven las acciones en orden inverso."""
    h = Historial()
    for n in (1, 2, 3):
        h.registrar(_accion(n))
    assert h.deshacer().turno_antes == 3
    assert h.deshacer().turno_antes == 2
    assert h.deshacer().turno_antes == 1


def test_deshacer_baja_cantidad_y_habilita_rehacer():
    """CA-H3: cada deshacer baja cantidad() en 1 y habilita rehacer."""
    h = Historial()
    h.registrar(_accion(1))
    h.registrar(_accion(2))
    h.deshacer()
    assert h.cantidad() == 1
    assert h.hay_rehacer()


def test_deshacer_la_unica_accion_deja_historial_vacio():
    """CA-H3: tras deshacer la única acción, cantidad es 0 y no hay más que deshacer."""
    h = Historial()
    h.registrar(_accion())
    h.deshacer()
    assert h.cantidad() == 0
    assert not h.hay_deshacer()


def test_deshacer_sin_acciones_no_cambia_el_estado():
    """CA-18: sin acciones, deshacer devuelve None y el estado queda igual."""
    h = Historial()
    assert h.deshacer() is None
    assert h.cantidad() == 0
    assert not h.hay_rehacer()
