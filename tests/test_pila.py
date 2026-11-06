"""Pruebas de Pila. T-02: casos con la pila vacía."""
import pytest

from estructuras.pila import Pila, PilaVaciaError


def test_pila_nueva_esta_vacia():
    """Base de CA-18: una pila nueva está vacía y su tamaño es 0."""
    p = Pila()
    assert p.esta_vacia()
    assert p.tamano() == 0


def test_desapilar_en_vacia_lanza_error():
    """Base de CA-18: desapilar sin elementos lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        Pila().desapilar()


def test_cima_en_vacia_lanza_error():
    """Base de CA-18: consultar la cima sin elementos lanza PilaVaciaError."""
    with pytest.raises(PilaVaciaError):
        Pila().cima()


def test_apilar_un_elemento():
    """Base de CA-H1: apilar un elemento lo deja en la cima y sube el tamaño."""
    p = Pila()
    p.apilar("a")
    assert p.cima() == "a"
    assert p.tamano() == 1
    assert not p.esta_vacia()


def test_desapilar_un_elemento_deja_vacia():
    """Base de CA-H1: desapilar el único elemento lo devuelve y vacía la pila."""
    p = Pila()
    p.apilar("a")
    assert p.desapilar() == "a"
    assert p.esta_vacia()
    assert p.tamano() == 0


def test_desapilar_sale_en_orden_inverso():
    """CA-H1 (base): con varios elementos sale primero el último que entró."""
    p = Pila()
    for x in (1, 2, 3):
        p.apilar(x)
    assert p.desapilar() == 3
    assert p.desapilar() == 2
    assert p.desapilar() == 1
    assert p.esta_vacia()


def test_cima_no_quita_el_elemento():
    """Base de CA-H1: cima() consulta sin modificar la pila."""
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    assert p.cima() == 2
    assert p.cima() == 2
    assert p.tamano() == 2

    

def test_vaciar_pila_vacia_no_falla():
    """Base de CA-17: vaciar una pila ya vacía no lanza error y sigue vacía."""
    p = Pila()
    p.vaciar()
    assert p.esta_vacia()
    assert p.tamano() == 0


def test_vaciar_con_un_elemento():
    """Base de CA-17: vaciar con un elemento deja la pila vacía."""
    p = Pila()
    p.apilar("a")
    p.vaciar()
    assert p.esta_vacia()
    with pytest.raises(PilaVaciaError):
        p.cima()


def test_vaciar_con_varios_y_reutilizar():
    """Base de CA-17: tras vaciar, la pila queda en uso normal."""
    p = Pila()
    for x in (1, 2, 3):
        p.apilar(x)
    p.vaciar()
    assert p.tamano() == 0
    p.apilar(9)
    assert p.cima() == 9
    assert p.tamano() == 1
