"""Prueba de humo de la Entrega 1: main.py arranca y pytest corre.

Criterio: requisito de repositorio de la Entrega 1 (sin CA de producto).
"""
import main


def test_main_arranca(capsys):
    main.main()
    salida = capsys.readouterr().out
    assert "Última Dosis" in salida
