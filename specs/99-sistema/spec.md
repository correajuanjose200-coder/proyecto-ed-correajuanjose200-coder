# Spec del sistema — Última Dosis

Versión 1.1 · 2026-11-11

## Qué hace el sistema
Juego por turnos en consola. Pedro cruza un mapa de 20 x 20 hasta la meta `E`. Dos zombis lo persiguen por BFS. Hay objetos (comida `C`, agua `A`), inventario de 5, deshacer y rehacer con efectos, eventos en orden, y victoria y derrota.

## Componentes y cómo encajan
| Componente | Módulo | Contrato con el resto |
|---|---|---|
| Pila | `estructuras/pila.py` | La usa `Historial` (hechas y deshechas) |
| Cola | `estructuras/cola.py` | La usan `Juego` (eventos) y `rutas.py` (frontera del BFS) |
| Inventario | `estructuras/inventario.py` | `Juego` agrega, quita e inserta por posición |
| Historial y Accion | `dominio/historial.py`, `dominio/accion.py` | `Juego` registra una `Accion` por turno; deshacer restaura el estado de antes |
| Mapa | `dominio/mapa.py` | Matriz densa; genera con semilla y camino garantizado |
| Rutas | `dominio/rutas.py` | `buscar_ruta(mapa, origen, destino)` devuelve distancia, primer paso y celdas exploradas |
| Juego | `dominio/juego.py` | Reglas de turno, zombis, salud, victoria y derrota |
| Consola | `main.py` | `python main.py` abre el bucle; `main.main()` solo imprime el banner |

## Reglas
Salud inicial 100, comida +20, agua +10 (tope 100), contacto con un zombi -25. La victoria tiene prioridad sobre la derrota (CA-28).

## No implementado
AVL de entidades, montículo de ranking, cola de turnos propia, antídoto y aturdimiento de zombis. Ver `moscow.md` v1.1.

## Historial de cambios
| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
| 1.1 | 2026-11-11 | Componentes reales, reglas y lista de lo no implementado | Entrega final |
