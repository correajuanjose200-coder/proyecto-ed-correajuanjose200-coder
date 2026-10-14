# Spec del sistema — Última Dosis (versión inicial)

Versión 0.1 · 2026-10-14

## Qué hace el sistema
Un juego por turnos en consola. Pedro cruza una ciudad en rejilla con el antídoto, recoge comida y agua, y llega al aeropuerto sin que su salud llegue a 0, mientras los zombies lo persiguen por el camino más corto. El jugador puede deshacer y rehacer jugadas, ver los eventos de cada turno, buscar entidades y consultar el ranking.

## Orden de un turno
1. El jugador elige una acción (mover, esperar, usar, soltar, deshacer, rehacer, etc.).
2. Si la acción es inválida, se rechaza y el turno no avanza.
3. Si es válida: se aplica, se registra en el historial y se generan los eventos.
4. Si Pedro llegó al aeropuerto, hay victoria y termina el turno (D-4).
5. Si no, cada zombie actúa en su turno (avanza o hace contacto).
6. Se evalúa derrota, se atienden los eventos y se dibuja el mapa.

## Componentes previstos

| # | Componente | Historias | Estructura (ver `estructuras.md`) |
|---|---|---|---|
| 01 | Historial de acciones | HU-04 | Dos pilas |
| 02 | Inventario | HU-03 | Lista enlazada simple |
| 03 | Eventos | HU-06 | Cola |
| 04 | Turnos | HU-02, HU-05 | Cola |
| 05 | Índice de entidades | HU-08 | Árbol AVL |
| 06 | Puntajes | HU-08 | Montículo máximo |
| 07 | Rutas de zombies | HU-05, HU-01 | Grafo implícito + BFS |
| 08 | Mapa | HU-01, HU-02 | Matriz densa |
| — | Consola (`main.py`) | HU-09 | — |

## Cómo encajan (por completar en la Entrega 2)
- `Mapa` es consultado por `Rutas`, el inventario y las reglas de movimiento.
- `Turnos` decide quién actúa; cada acción de Pedro produce una `Accion` para `Historial` y eventos para `Eventos`.
- Cada entidad nueva se inserta en el `Índice`; al ganar, `Puntajes` recibe el puntaje.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 0.1 | 2026-10-14 | Versión inicial | Entrega 1 |
