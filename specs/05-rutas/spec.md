# Spec — Rutas de los zombis

Versión 1.0 · 2026-11-11 · Soporta: HU-05 (CA-19, CA-20, CA-21) y la verificación de CA-02. Must

## Propósito
Dado el mapa, una celda de origen y una celda de destino, decir si hay camino, cuánto mide el más corto y cuál es el primer paso. Los zombis usan el primer paso para acercarse a Pedro.

## Convenciones
- Una celda se escribe como `(fila, columna)`.
- Se avanza una casilla por paso: arriba, abajo, izquierda o derecha (sin diagonales).
- Solo se pisan celdas transitables del mapa (`Mapa.es_transitable`): libres, de objeto o la meta.
- Cuando hay varios caminos igual de cortos, siempre se elige el mismo (determinista): el orden de preferencia es arriba, abajo, izquierda, derecha.

## Operaciones

| Operación | Entrada | Resultado | Errores |
|---|---|---|---|
| `buscar_ruta(mapa, origen, destino)` | Un mapa y dos celdas | Un resultado `Ruta` con `distancia` (pasos del camino más corto), `siguiente` (primera celda del camino, o `None` si origen y destino son la misma) y `exploradas` (cuántas celdas visitó la búsqueda, contando el origen); o `None` si no hay camino | `PosicionInvalidaError` si origen o destino están fuera del mapa |

Si origen o destino son un obstáculo, no hay camino y el resultado es `None`.
`buscar_ruta` nunca modifica el mapa.

## Criterios de aceptación
Criterios de producto: **CA-19, CA-20, CA-21**, y la comprobación de **CA-02** (ver `00-producto/historias.md`). Además:

- **CA-R1** `distancia` es el número mínimo de pasos entre origen y destino (en un mapa sin obstáculos es la distancia de Manhattan; con obstáculos puede ser mayor).
- **CA-R2** `siguiente` está a un paso del origen y desde ella la distancia al destino es `distancia - 1` (CA-19).
- **CA-R3** `siguiente` y todo el camino son celdas transitables dentro del mapa (CA-20).
- **CA-R4** Si no existe camino (muro completo o destino encerrado) el resultado es `None` (CA-21).
- **CA-R5** Si origen y destino son la misma celda, `distancia` es 0, `siguiente` es `None` y `exploradas` es 1.
- **CA-R6** Origen o destino fuera del mapa lanza `PosicionInvalidaError`; origen o destino en un obstáculo da `None`.
- **CA-R7** Con las mismas entradas siempre se obtiene el mismo resultado, y `exploradas` está entre 1 y la cantidad de celdas transitables.
- **CA-R8** `buscar_ruta` no modifica el mapa.
- **CA-R9** En todo mapa creado con `Mapa.generar` existe ruta entre `inicio` y `meta` (comprobación de CA-02).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |