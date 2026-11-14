# Spec del sistema — Última Dosis

Versión 1.2 · 2026-11-13

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

## Contrato del enunciado frente a lo construido

### 1. Elementos mínimos del dominio (definidos por el docente)

| Elemento mínimo | Estado | Criterios | Cómo se ve en el juego |
|---|---|---|---|
| Mapa ≥ 20×20, obstáculos ≤ 25 % | Cumple | CA-01, CA-02 | Mapa 20×20 por semilla, con camino garantizado a la meta |
| Jugador por turnos (4 direcciones y esperar) | Cumple | CA-07 | w, a, s, d, x |
| ≥ 2 enemigos que avanzan hacia el jugador | Cumple | CA-19, CA-20, CA-21 | 2 zombis, un paso por turno por el camino más corto |
| Objetos e inventario (agregar, usar, soltar, listar) | Cumple | CA-09, CA-10, CA-12, CA-13 | Recoger al pisar; u N, g N, i |
| Historial con deshacer y rehacer con efectos | Cumple | CA-15, CA-16, CA-17 | z, r; deshacer una recogida devuelve el objeto al mapa |
| Eventos en orden de ocurrencia | Cumple | CA-23, CA-25 | Se muestran una vez; CA-25 sin prueba dedicada |
| Victoria y derrota | Cumple | CA-26, CA-27, CA-28 | Llegar a E; salud 0; CA-28 (victoria gana el empate) sin prueba dedicada |
| Consola que ejercita todas las funcionalidades | Parcial | n/a | main.py; no cubre F-08 |

### 2. Funcionalidades esperadas

| ID | Estado | Nota |
|---|---|---|
| F-01 a F-07 | Cumplen | Ver tabla anterior |
| F-08 Buscar entidad y puntajes | No cumple | CA-30 a CA-34; pasó a Won't en moscow.md v1.1 por falta de tiempo |

### 3. Decisiones que no vienen del enunciado

| Decisión | Valor | Origen |
|---|---|---|
| Salud inicial, comida, agua, daño | 100, +20, +10, -25 | Spec (borrador con IA, revisado por mí). El primer código usaba otros valores y se corrigió a los de la spec |
| Capacidad del inventario | 5 | Mía |
| Narrativa (Pedro, zombis, aeropuerto) | n/a | Mía |
| Victoria gana el empate | CA-28 | Spec (borrador con IA, revisado por mí) |
| Código de rutas, juego y consola; pruebas de juego | n/a | Borradores de IA, probados y comparados contra mis specs |

### 4. Desviaciones respecto al contrato

| Qué | Efecto |
|---|---|
| AVL y montículo no implementados | F-08 sin cubrir; la rúbrica pide justificar estructuras y estas dos no existen |
| Orden de turnos fijo, sin cola propia | La capacidad "orden de los turnos" queda sin estructura dedicada |
| A* no implementado | BFS cumple el mínimo; no hay comparación medida |
| Antídoto (CA-05) y aturdimiento (CA-22) | Pendientes; CA-22 es parcial |
| Sin prueba dedicada: CA-03, CA-06, CA-08, CA-24, CA-25, CA-28, CA-36 | Implementados pero no demostrados con prueba |
| CA-29 parcial | Deshacer y rehacer no comprueban si la partida terminó; la consola no llega a ellos |

## Historial de cambios
| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
| 1.1 | 2026-11-11 | Componentes reales, reglas y lista de lo no implementado | Entrega final |
| 1.2 | 2026-11-13 | Se agrega la comparación contrato vs. construido | Preparar la sustentación; no cambia comportamiento |
