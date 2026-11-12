"""Pruebas del juego (integración de las estructuras)."""
from dominio.juego import Juego
from dominio.mapa import COMIDA, LIBRE, OBSTACULO


def _juego_sin_zombis():
    j = Juego(1)
    j.zombis = ()
    j.procesar_eventos()
    return j


def test_recoger_y_deshacer_devuelve_el_objeto_al_mapa():
    """CA-15: deshacer una recogida quita el objeto del inventario y lo devuelve al mapa."""
    j = _juego_sin_zombis()
    j.mapa.poner(0, 1, COMIDA)
    j.mover("d")
    assert j.inventario.tamano() == 1
    assert j.mapa.obtener(0, 1) == LIBRE
    j.deshacer()
    assert j.inventario.tamano() == 0
    assert j.mapa.obtener(0, 1) == COMIDA
    assert j.pedro[:2] == (0, 0)


def test_rehacer_recogida_vuelve_a_recoger():
    """CA-16: rehacer una recogida deshecha la aplica de nuevo."""
    j = _juego_sin_zombis()
    j.mapa.poner(0, 1, COMIDA)
    j.mover("d")
    j.deshacer()
    j.rehacer()
    assert j.inventario.tamano() == 1
    assert j.mapa.obtener(0, 1) == LIBRE
    assert j.pedro[:2] == (0, 1)


def test_accion_nueva_vacia_lo_rehacible():
    """CA-17: tras deshacer, una acción nueva impide rehacer."""
    j = _juego_sin_zombis()
    j.mover("d")
    j.deshacer()
    j.esperar()
    ok, _ = j.rehacer()
    assert ok is False


def test_no_atraviesa_obstaculos():
    """CA-07: un obstáculo bloquea el movimiento y no gasta turno."""
    j = _juego_sin_zombis()
    j.mapa.poner(0, 1, OBSTACULO)
    ok, _ = j.mover("d")
    assert ok is False
    assert j.turno == 0


def test_no_entra_a_celda_con_zombi():
    """CA-22: un zombi bloquea el paso."""
    j = _juego_sin_zombis()
    j.zombis = ((1, 0, 1),)
    ok, _ = j.mover("d")
    assert ok is False


def test_victoria_al_llegar_a_la_meta():
    """CA-26: pisar la meta termina la partida en victoria."""
    j = _juego_sin_zombis()
    j.pedro = (19, 18, 3)
    j.mover("d")
    assert j.estado == "victoria"


def test_derrota_sin_salud():
    """CA-27: un zombi adyacente ataca y con salud 0 hay derrota."""
    j = _juego_sin_zombis()
    j.pedro = (0, 0, 1)
    j.zombis = ((1, 0, 1),)
    j.esperar()
    assert j.estado == "derrota"


def test_usar_comida_sube_salud():
    """CA-10: usar comida da +20 de salud y la quita del inventario."""
    j = _juego_sin_zombis()
    j.pedro = (0, 0, 50)
    j.inventario.agregar(COMIDA)
    j.usar(0)
    assert j.pedro[2] == 70
    assert j.inventario.esta_vacio()


def test_eventos_salen_en_orden_de_llegada():
    """CA-23: los eventos se procesan en el orden en que ocurrieron y luego quedan vacíos."""
    j = Juego(1)
    eventos = j.procesar_eventos()
    assert "zombi 1" in eventos[0] and "zombi 2" in eventos[1]
    assert j.procesar_eventos() == []
