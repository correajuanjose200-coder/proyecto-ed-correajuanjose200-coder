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