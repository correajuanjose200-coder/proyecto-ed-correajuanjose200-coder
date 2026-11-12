# ANÁLISIS de complejidad

Versión final · 2026-11-11. n = elementos de la estructura; F x C = celdas del mapa (20 x 20 = 400).

## Tabla de complejidad (lo implementado)

| Módulo | Operación | Complejidad |
|---|---|---|
| `estructuras/pila.py` | apilar, desapilar, cima, tamano, esta_vacia | O(1) |
| `estructuras/pila.py` | vaciar | O(n) (suelta nodos uno a uno) |
| `estructuras/cola.py` | encolar, desencolar, frente, tamano, esta_vacia | O(1) |
| `estructuras/cola.py` | vaciar | O(n) |
| `estructuras/inventario.py` | agregar (al final, con puntero al último) | O(1) |
| `estructuras/inventario.py` | insertar, quitar, listar (por posición) | O(n), n <= 5 |
| `dominio/historial.py` | registrar, deshacer, rehacer | O(1) |
| `dominio/accion.py` | crear una acción | O(1) |
| `dominio/mapa.py` | obtener, poner, dentro, es_transitable | O(1) |
| `dominio/mapa.py` | contar, dibujar, proporcion_obstaculos | O(F x C) |
| `dominio/mapa.py` | generar | O(F x C) más la verificación del camino |
| `dominio/rutas.py` | buscar_ruta (BFS) | O(V + E) = O(F x C) |
| `dominio/juego.py` | un turno | O(Z x F x C), con Z zombis
cat >> specs/trazabilidad.md << 'EOF'

## Cierre de la entrega final (2026-11-11)

Las pruebas de integración están en `tests/test_juego.py`. Pruebas por estructura: `test_pila.py`, `test_cola.py`, `test_inventario.py`, `test_historial.py`, `test_mapa.py`, `test_mapa_generar.py`, `test_rutas.py`.

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
| CA-06, CA-08, CA-09, CA-11 a CA-14, CA-18, CA-24, CA-29, CA-35, CA-36 | Implementados en `juego.py` y `main.py`; sin prueba dedicada de integración | Pendiente |
| CA-03, CA-04 | Implementados en `Juego.__init__`; sin prueba dedicada | Pendiente |
| CA-05 | Antídoto no implementado | No implementado |
| CA-30 a CA-34 | AVL y montículo no implementados (Won't) | No implementado |
