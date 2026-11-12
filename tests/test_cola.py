"""Pruebas de Cola (componente 03)."""
import pytest

from estructuras.cola import Cola, ColaVaciaError


def test_cola_nueva_esta_vacia():
    """CA-C2 (base): una cola nueva está vacía y su tamaño es 0."""
    c = Cola()
    assert c.esta_vacia()
    assert c.tamano() == 0


def test_desencolar_en_vacia_lanza_error():
    """CA-C2: desencolar sin elementos lanza ColaVaciaError."""
    with pytest.raises(ColaVaciaError):
        Cola().desencolar()


def test_frente_en_vacia_lanza_error_y_no_cambia():
    """CA-C2: frente sin elementos lanza ColaVaciaError y la cola sigue vacía."""
    c = Cola()
    with pytest.raises(ColaVaciaError):
        c.frente()
    assert c.esta_vacia()


def test_encolar_un_elemento():
    """CA-C3: encolar sube el tamaño y frente no quita el elemento."""
    c = Cola()
    c.encolar("a")
    assert c.tamano() == 1
    assert c.frente() == "a"
    assert c.tamano() == 1


def test_orden_primero_en_entrar_primero_en_salir():
    """CA-C1: los elementos salen en el orden en que entraron."""
    c = Cola()
    for x in (1, 2, 3):
        c.encolar(x)
    assert [c.desencolar(), c.desencolar(), c.desencolar()] == [1, 2, 3]


def test_desencolar_baja_el_tamano():
    """CA-C3: desencolar devuelve el frente y baja el tamaño."""
    c = Cola()
    c.encolar("a")
    c.encolar("b")
    assert c.desencolar() == "a"
    assert c.tamano() == 1
    assert c.frente() == "b"


def test_un_elemento_desencolar_deja_vacia_y_reutilizable():
    """CA-C4: con un elemento, desencolar vacía la cola y se puede encolar de nuevo."""
    c = Cola()
    c.encolar("a")
    assert c.desencolar() == "a"
    assert c.esta_vacia()
    c.encolar("b")
    assert c.frente() == "b"
    assert c.tamano() == 1


def test_vaciar_con_elementos():
    """CA-C5: vaciar deja tamaño 0 y la cola reutilizable."""
    c = Cola()
    for x in range(5):
        c.encolar(x)
    c.vaciar()
    assert c.esta_vacia()
    assert c.tamano() == 0
    c.encolar("z")
    assert c.desencolar() == "z"


def test_vaciar_en_vacia_no_falla():
    """CA-C5: vaciar una cola vacía no lanza error."""
    c = Cola()
    c.vaciar()
    assert c.tamano() == 0


def test_vaciar_con_un_elemento():
    """CA-C5: vaciar con un solo elemento deja la cola vacía."""
    c = Cola()
    c.encolar(1)
    c.vaciar()
    assert c.esta_vacia()
