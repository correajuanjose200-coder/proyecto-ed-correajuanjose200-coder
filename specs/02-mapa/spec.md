# Spec — Mapa de la ciudad

Versión 1.0 · 2026-11-06 · Soporta: HU-01 (CA-01 a CA-04), HU-02 (CA-07), HU-05 (CA-20), HU-09 (CA-35), Must

## Propósito
Representar la ciudad como una rejilla y responder qué hay en cada celda y si se puede pisar.

## Símbolos de celda
`.` libre · `#` obstáculo · `E` aeropuerto (meta) · `C` comida · `A` agua.
Pedro y los zombis no forman parte del mapa: se dibujan encima de él.

## Operaciones

| Operación | Entrada | Resultado | Errores |
|---|---|---|---|
| `Mapa(filas, columnas)` | Dimensiones | Mapa con todas las celdas libres | `ValueError` si filas o columnas son menores que 1 |
| `dentro(f, c)` | Posición | Verdadero si la posición está dentro del mapa | — |
| `obtener(f, c)` | Posición | Símbolo de esa celda | `PosicionInvalidaError` si está fuera |
| `poner(f, c, simbolo)` | Posición y símbolo | La celda pasa a tener ese símbolo; las demás no cambian | `PosicionInvalidaError` si está fuera; `ValueError` si el símbolo no es válido |
| `es_transitable(f, c)` | Posición | Verdadero si está dentro y no es obstáculo | — |
| `contar(simbolo)` | Símbolo | Cuántas celdas tienen ese símbolo | `ValueError` si el símbolo no es válido |
| `proporcion_obstaculos()` | — | Fracción de celdas que son obstáculo (entre 0 y 1) | — |
| `generar(filas, columnas, semilla)` | Dimensiones y semilla | Mapa listo para jugar (ver reglas) | `ValueError` si las dimensiones son menores que 20 |
| `dibujar()` | — | Texto con una línea por fila | — |

## Reglas de `generar`
- Mide al menos 20×20 y los obstáculos no superan el 25 % de las celdas.
- Siempre existe un camino de celdas transitables entre la celda de inicio de Pedro y la meta.
- Hay al menos una comida y un agua en celdas libres.
- Con la misma semilla se genera el mismo mapa.

## Criterios de aceptación
Criterios de producto: **CA-01, CA-02, CA-04, CA-07, CA-20, CA-35** (ver `00-producto/historias.md`). Además:

- **CA-M1** `dentro` es verdadero en las cuatro esquinas y falso un paso fuera de cada borde.
- **CA-M2** `es_transitable` es falso para obstáculos y para posiciones fuera del mapa, y verdadero para celdas libres, de objeto o meta.
- **CA-M3** Lo que se pone en una celda es lo que se obtiene, y no cambia ninguna otra celda.
- **CA-M4** Obtener o poner fuera del mapa lanza `PosicionInvalidaError`.
- **CA-M5** Poner un símbolo desconocido lanza `ValueError` y no cambia el mapa.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-06 | Versión inicial | Entrega 2 |
