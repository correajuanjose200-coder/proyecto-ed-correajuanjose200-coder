# Trazabilidad criterio ↔ prueba

Versión 0.1 · 2026-10-14 · Se completa con cada entrega. "Pendiente" = prueba aún no escrita.

| CA | Componente | Prueba | Estado |
|---|---|---|---|
| CA-14 | 01-historial | `tests/test_historial.py::test_deshacer_orden_inverso` | Parcial: orden listo; efectos en T-10 |
| CA-15 | 01-historial | `tests/test_integracion_historial.py::test_deshacer_recogida` | Pendiente (T-10) |
| CA-16 | 01-historial | `tests/test_historial.py::test_rehacer_orden_inverso_al_deshacer` | Hecho |
| CA-17 | 01-historial | `tests/test_historial.py::test_accion_nueva_vacia_rehacer` | Hecho |
| CA-18 | 01-historial | `tests/test_historial.py::test_deshacer_sin_acciones_no_cambia_el_estado` y `test_rehacer_sin_deshechas_no_cambia_el_estado` | Hecho |
| CA-H1…H4 | 01-historial | `tests/test_historial.py` | Hecho |
| CA-01…CA-13, CA-19…CA-36 | otros componentes | por especificar en Entrega 2 | Pendiente |

## Componente 03-cola (2026-11-11)

| CA | Prueba | Estado |
|---|---|---|
| CA-C1 | `tests/test_cola.py::test_orden_primero_en_entrar_primero_en_salir` | Hecho |
| CA-C2 | `tests/test_cola.py::test_desencolar_en_vacia_lanza_error` y `test_frente_en_vacia_lanza_error_y_no_cambia` | Hecho |
| CA-C3 | `tests/test_cola.py::test_encolar_un_elemento` y `test_desencolar_baja_el_tamano` | Hecho |
| CA-C4 | `tests/test_cola.py::test_un_elemento_desencolar_deja_vacia_y_reutilizable` | Hecho |
| CA-C5 | `tests/test_cola.py::test_vaciar_con_elementos` | Hecho |
