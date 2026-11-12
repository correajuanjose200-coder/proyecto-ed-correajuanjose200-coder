# Tareas — Rutas de los zombis

Versión 1.0 · 2026-11-11 · Una tarea = un commit de prueba y uno de código. La prueba va primero.

| ID | Tarea | Cierra | Prueba (archivo) |
|---|---|---|---|
| R-01 | `buscar_ruta`: casos triviales (misma celda, vecinas, errores, obstáculos) | CA-R5, CA-R6 | `tests/test_rutas.py` |
| R-02 | Camino más corto y primer paso, con y sin obstáculos | CA-19, CA-R1, CA-R2, CA-R3 | `tests/test_rutas.py` |
| R-03 | Sin camino | CA-21, CA-R4 | `tests/test_rutas.py` |
| R-04 | Determinismo, `exploradas` y mapa intacto | CA-R7, CA-R8 | `tests/test_rutas.py` |
| R-05 | Ruta en mapas generados | CA-02, CA-R9 | `tests/test_rutas.py` |

## Definición de hecho
Pruebas pasando, docstrings con complejidad, `specs/trazabilidad.md` actualizado.