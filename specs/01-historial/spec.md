# Spec — Historial de acciones (deshacer y rehacer)

Versión 1.0 · 2026-10-14 · Soporta: HU-04 (F-04), Must

## Propósito
Recordar las acciones del jugador para poder revertirlas y reaplicarlas con todos sus efectos.

## Qué es una acción registrada
Una acción registrada contiene todo lo necesario para revertirla y reaplicarla: tipo de acción (mover, esperar, recoger, usar, soltar), posición y salud de Pedro antes y después, posición de cada zombie antes y después, objeto afectado (si lo hay) y contador de turnos antes y después.

## Operaciones

| Operación | Entrada | Resultado | Errores |
|---|---|---|---|
| `registrar(accion)` | Una acción ya aplicada al juego | La acción pasa a ser la más reciente que se puede deshacer. Lo que se podía rehacer se descarta. | — |
| `deshacer()` | — | Devuelve la acción más reciente que no está deshecha y la marca como deshecha. | Sin acciones: informa que no hay nada que deshacer y no cambia el estado. |
| `rehacer()` | — | Devuelve la acción deshecha más reciente y la vuelve a marcar como hecha. | Sin acciones deshechas: informa que no hay nada que rehacer y no cambia el estado. |
| `hay_deshacer()` | — | Verdadero si hay al menos una acción para deshacer. | — |
| `hay_rehacer()` | — | Verdadero si hay al menos una acción para rehacer. | — |
| `cantidad()` | — | Número de acciones que se pueden deshacer. | — |

## Reglas
- Las acciones se deshacen en orden inverso al que se registraron.
- Las acciones deshechas se rehacen en orden inverso al que se deshicieron.
- Una acción nueva descarta todo lo rehacible.
- El historial no tiene límite propio de tamaño.
- Las acciones rechazadas por el juego (movimiento inválido, etc.) no se registran, porque no consumen turno.

## Criterios de aceptación
Los criterios de producto que verifica este componente son **CA-14, CA-15, CA-16, CA-17 y CA-18** (ver `00-producto/historias.md`). Además:

- **CA-H1** Con N acciones registradas, N deshacer sucesivos las devuelven en orden inverso al registrado.
- **CA-H2** Con N acciones deshechas, N rehacer sucesivos las devuelven en el orden en que se deshicieron.
- **CA-H3** `cantidad()` es 0 con el historial vacío y baja en 1 con cada deshacer.
- **CA-H4** Registrar, deshacer una vez y registrar otra acción deja `hay_rehacer()` en falso.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
