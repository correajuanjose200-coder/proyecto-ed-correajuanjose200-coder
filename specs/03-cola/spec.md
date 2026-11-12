# Spec — Cola

Versión 1.0 · 2026-11-11 · Soporta: HU-06 (CA-23, CA-25), HU-05 y turnos (orden de actores). Must

## Propósito
Guardar elementos y atenderlos en el mismo orden en que llegaron.

## Operaciones

| Operación | Entrada | Resultado | Errores |
|---|---|---|---|
| `Cola()` | — | Cola vacía | — |
| `encolar(dato)` | Un elemento | El elemento queda al final de la cola | — |
| `desencolar()` | — | Quita y devuelve el elemento del frente | `ColaVaciaError` si está vacía |
| `frente()` | — | Devuelve el elemento del frente sin quitarlo | `ColaVaciaError` si está vacía |
| `esta_vacia()` | — | Verdadero si no hay elementos | — |
| `tamano()` | — | Cantidad de elementos | — |
| `vaciar()` | — | La cola queda vacía | — |

## Criterios de aceptación
- **CA-C1** Los elementos salen en el mismo orden en que entraron (primero en entrar, primero en salir).
- **CA-C2** `desencolar` y `frente` sobre una cola vacía lanzan `ColaVaciaError` y no cambian la cola.
- **CA-C3** `frente` no quita el elemento; `tamano` sube con `encolar` y baja con `desencolar`.
- **CA-C4** Con un solo elemento, `desencolar` deja la cola vacía y se puede volver a encolar.
- **CA-C5** `vaciar` deja `tamano` en 0 y la cola reutilizable.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |
