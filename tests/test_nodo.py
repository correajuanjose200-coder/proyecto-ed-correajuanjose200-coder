"""Pruebas de Nodo (T-01). Es un componente de soporte: no cierra un CA propio."""
from estructuras.nodo import Nodo


def test_nodo_guarda_su_dato():
    """Soporte de CA-14..CA-18: el nodo conserva el dato que se le da."""
    assert Nodo(5).dato == 5


def test_nodo_no_tiene_siguiente_por_defecto():
    """Soporte: un nodo nuevo queda sin enlace."""
    assert Nodo("a").siguiente is None


def test_nodo_se_enlaza_con_otro():
    """Soporte: el enlace apunta al nodo indicado."""
    b = Nodo(2)
    a = Nodo(1, b)
    assert a.siguiente is b
    assert a.siguiente.dato == 2