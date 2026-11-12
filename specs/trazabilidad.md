# Trazabilidad criterio ↔ prueba

Versión 1.0 · 2026-11-11 (cierre al final; 0.1 del 2026-10-14) · Se completa con cada entrega. "Pendiente" = prueba aún no escrita.

| CA | Componente | Prueba | Estado |
|---|---|---|---|
| CA-14 | 01-historial | `tests/test_historial.py::test_deshacer_orden_inverso` | Parcial: orden listo; efectos en T-10 |
| CA-15 | 01-historial | `tests/test_integracion_historial.py::test_deshacer_recogida` | Hecho: ver cierre (test_juego.py) |
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

## Cierre de la entrega final (2026-11-11)

Pruebas de integración en `tests/test_juego.py`; por estructura en `test_pila.py`, `test_cola.py`, `test_inventario.py`, `test_historial.py`, `test_mapa.py`, `test_mapa_generar.py`, `test_rutas.py`.

| CA | Prueba | Estado |
|---|---|---|
| CA-01, CA-02 | `test_mapa_generar.py`, `test_rutas.py::test_hay_ruta_en_mapas_generados` | Hecho |
| CA-07 | `test_juego.py::test_no_atraviesa_obstaculos` | Hecho |
| CA-10 | `test_juego.py::test_usar_comida_sube_salud` | Hecho (comida); agua sin prueba |
| CA-15 | `test_juego.py::test_recoger_y_deshacer_devuelve_el_objeto_al_mapa` | Hecho |
| CA-16 | `test_juego.py::test_rehacer_recogida_vuelve_a_recoger` | Hecho |
| CA-17 | `test_juego.py::test_accion_nueva_vacia_lo_rehacible` | Hecho |
| CA-19 a CA-21 | `test_rutas.py` | Hecho (BFS) |
| CA-22 | `test_juego.py::test_no_entra_a_celda_con_zombi` | Parcial: bloqueo y -25 de salud; sin aturdimiento |
| CA-23, CA-25 | `test_juego.py::test_eventos_salen_en_orden_de_llegada` | Hecho |
| CA-26, CA-27 | `test_juego.py::test_victoria_al_llegar_a_la_meta`, `test_derrota_sin_salud` | Hecho |
| CA-28 | Implementado en `Juego.estado`, sin prueba dedicada | Pendiente la prueba |
| CA-03, CA-04, CA-06, CA-08, CA-09, CA-11 a CA-14, CA-18, CA-24, CA-29, CA-35, CA-36 | Implementados en `juego.py` y `main.py`; sin prueba dedicada | Pendiente |
| CA-05 | Antídoto no implementado | No implementado |
| CA-30 a CA-34 | AVL y montículo no implementados (Won't) | No implementado |
