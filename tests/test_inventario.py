"""Pruebas de Inventario (componente 04)."""
import pytest

from estructuras.inventario import (
    Inventario,
    InventarioLlenoError,
    PosicionInventarioError,
)


def _con(*objetos, capacidad=5):
    inv = Inventario(capacidad)
    for o in objetos:
        inv.agregar(o)
    return inv


# --- crear, tamano, esta_vacio, esta_lleno, listar (I-01) ---

def test_inventario_nuevo_esta_vacio_con_capacidad_5():
    """CA-I6: un inventario nuevo está vacío y admite 5 objetos por defecto."""
    inv = Inventario()
    assert inv.esta_vacio()
    assert inv.tamano() == 0
    assert not inv.esta_lleno()
    for i in range(5):
        inv.agregar(i)
    assert inv.esta_lleno()


def test_capacidad_personalizada():
    """CA-I6: la capacidad se puede elegir y se respeta."""
    inv = _con("a", "b", capacidad=2)
    assert inv.esta_lleno()
    with pytest.raises(InventarioLlenoError):
        inv.agregar("c")


def test_capacidad_menor_que_1_lanza_error():
    """CA-I6: capacidad 0 o negativa lanza ValueError."""
    with pytest.raises(ValueError):
        Inventario(0)
    with pytest.raises(ValueError):
        Inventario(-3)


def test_listar_vacio_no_entrega_nada():
    """CA-I5 / CA-13: listar con inventario vacío no entrega objetos."""
    assert list(Inventario().listar()) == []


def test_listar_un_elemento():
    """CA-I5: listar con un solo objeto lo entrega."""
    assert list(_con("comida").listar()) == ["comida"]


def test_listar_no_modifica_el_inventario():
    """CA-I5: listar dos veces entrega lo mismo y no cambia el tamaño."""
    inv = _con("a", "b")
    assert list(inv.listar()) == list(inv.listar()) == ["a", "b"]
    assert inv.tamano() == 2


# --- agregar (I-02) ---

def test_agregar_un_objeto():
    """CA-09 / CA-I1: agregar sube el tamaño y deja el objeto en el inventario."""
    inv = Inventario()
    inv.agregar("comida")
    assert inv.tamano() == 1
    assert not inv.esta_vacio()
    assert list(inv.listar()) == ["comida"]


def test_agregar_conserva_el_orden_de_recogida():
    """CA-13 / CA-I1: los objetos salen en el orden en que se agregaron."""
    inv = _con("comida", "agua", "comida")
    assert list(inv.listar()) == ["comida", "agua", "comida"]


def test_agregar_con_inventario_lleno_lanza_error_y_no_cambia():
    """CA-12 / CA-I2: con 5 objetos, agregar otro lanza error y nada cambia."""
    inv = _con(1, 2, 3, 4, 5)
    with pytest.raises(InventarioLlenoError):
        inv.agregar(6)
    assert list(inv.listar()) == [1, 2, 3, 4, 5]
    assert inv.tamano() == 5


# --- quitar (I-03) ---

def test_quitar_en_vacio_lanza_error():
    """CA-10 / CA-I3: quitar con inventario vacío lanza PosicionInventarioError."""
    with pytest.raises(PosicionInventarioError):
        Inventario().quitar(0)


def test_quitar_posicion_fuera_de_rango_lanza_error_y_no_cambia():
    """CA-I3: posición negativa o igual al tamaño lanza error y no cambia nada."""
    inv = _con("a", "b")
    with pytest.raises(PosicionInventarioError):
        inv.quitar(-1)
    with pytest.raises(PosicionInventarioError):
        inv.quitar(2)
    assert list(inv.listar()) == ["a", "b"]


def test_quitar_el_unico_deja_vacio_y_reutilizable():
    """CA-I3: con un solo objeto, quitar lo devuelve y se puede agregar de nuevo."""
    inv = _con("a")
    assert inv.quitar(0) == "a"
    assert inv.esta_vacio()
    inv.agregar("b")
    assert list(inv.listar()) == ["b"]


def test_quitar_el_primero():
    """CA-11 / CA-I3: quitar la posición 0 conserva el orden de los demás."""
    inv = _con("a", "b", "c")
    assert inv.quitar(0) == "a"
    assert list(inv.listar()) == ["b", "c"]


def test_quitar_uno_del_medio():
    """CA-11 / CA-I3: quitar del medio conserva el orden de los demás."""
    inv = _con("a", "b", "c")
    assert inv.quitar(1) == "b"
    assert list(inv.listar()) == ["a", "c"]
    assert inv.tamano() == 2


def test_quitar_el_ultimo_y_luego_agregar_mantiene_el_orden():
    """CA-I3 / CA-I1: tras quitar el último, agregar sigue al final."""
    inv = _con("a", "b", "c")
    assert inv.quitar(2) == "c"
    inv.agregar("d")
    assert list(inv.listar()) == ["a", "b", "d"]


def test_tamano_baja_y_esta_vacio_cambia_al_quitar():
    """CA-I3: quitar baja el tamaño; al quitar todo el inventario queda vacío."""
    inv = _con("a", "b")
    inv.quitar(0)
    assert inv.tamano() == 1
    assert not inv.esta_vacio()
    inv.quitar(0)
    assert inv.esta_vacio()


# --- insertar (I-04) ---

def test_insertar_en_vacio_posicion_0():
    """CA-I4: insertar en la posición 0 de un inventario vacío funciona."""
    inv = Inventario()
    inv.insertar(0, "a")
    assert list(inv.listar()) == ["a"]
    inv.agregar("b")
    assert list(inv.listar()) == ["a", "b"]


def test_insertar_al_inicio():
    """CA-I4: insertar en 0 desplaza los demás sin alterar su orden."""
    inv = _con("b", "c")
    inv.insertar(0, "a")
    assert list(inv.listar()) == ["a", "b", "c"]


def test_insertar_en_el_medio():
    """CA-I4: insertar en medio conserva el orden de los demás."""
    inv = _con("a", "c")
    inv.insertar(1, "b")
    assert list(inv.listar()) == ["a", "b", "c"]


def test_insertar_al_final_equivale_a_agregar():
    """CA-I4: insertar en la posición igual al tamaño deja el objeto al final."""
    inv = _con("a", "b")
    inv.insertar(2, "c")
    inv.agregar("d")
    assert list(inv.listar()) == ["a", "b", "c", "d"]


def test_insertar_fuera_de_rango_lanza_error_y_no_cambia():
    """CA-I4: posición negativa o mayor que el tamaño lanza error y no cambia nada."""
    inv = _con("a")
    with pytest.raises(PosicionInventarioError):
        inv.insertar(-1, "x")
    with pytest.raises(PosicionInventarioError):
        inv.insertar(2, "x")
    assert list(inv.listar()) == ["a"]


def test_insertar_con_inventario_lleno_lanza_error():
    """CA-I2: insertar con el inventario lleno lanza error y no cambia nada."""
    inv = _con(1, 2, 3, 4, 5)
    with pytest.raises(InventarioLlenoError):
        inv.insertar(0, 9)
    assert list(inv.listar()) == [1, 2, 3, 4, 5]


def test_quitar_e_insertar_en_la_misma_posicion_restaura():
    """CA-I4 (base de CA-14/CA-15): quitar e insertar en la misma posición deja todo igual."""
    for pos in (0, 1, 2):
        inv = _con("a", "b", "c")
        objeto = inv.quitar(pos)
        inv.insertar(pos, objeto)
        assert list(inv.listar()) == ["a", "b", "c"]
