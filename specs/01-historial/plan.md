# Plan — Historial de acciones

Versión 1.0 · 2026-10-14 · Implementa: `specs/01-historial/spec.md`

## Estructura elegida: dos pilas
- Pila **hechas**: acciones que se pueden deshacer. La cima es la acción más reciente.
- Pila **deshechas**: acciones que se pueden rehacer. La cima es la última deshecha.

| Operación | Cómo | Complejidad |
|---|---|---|
| `registrar` | apilar en *hechas*; vaciar *deshechas* | O(1) apilar; O(k) vaciar, con k = deshechas descartadas |
| `deshacer` | desapilar de *hechas* y apilar en *deshechas* | O(1) |
| `rehacer` | desapilar de *deshechas* y apilar en *hechas* | O(1) |
| `hay_deshacer` / `hay_rehacer` | preguntar si la pila está vacía | O(1) |
| `cantidad` | contador guardado en la pila | O(1) |

Nota sobre vaciar *deshechas*: se puede hacer en O(1) soltando la referencia a la cabeza de la lista y dejando que el recolector de basura libere los nodos; el costo real de liberar es de Python, no de nuestro código. Se declara O(1) amortizado en el código y se aclara en `ANALISIS.md`.

## Alternativa descartada: lista doble con cursor
También da O(1) en cada operación, pero obliga a mantener un cursor y a cortar la lista en cada acción nueva. Más código y más casos de borde para el mismo resultado. Si en la Entrega 2 aparece una razón (por ejemplo, saltar a una jugada arbitraria), se registra el cambio aquí.

## Módulos
- `estructuras/nodo.py`: clase `Nodo(dato, siguiente)` propia.
- `estructuras/pila.py`: `Pila` con `apilar`, `desapilar`, `cima`, `esta_vacia`, `tamano`, `vaciar`. Se construye con `Nodo`, sin `list`.
- `dominio/accion.py`: la acción registrada (datos descritos en la spec).
- `dominio/historial.py`: `Historial` que usa dos `Pila` y expone las operaciones de la spec.

## Soportes internos
Ninguno: no se usa `list`, `dict` ni `deque`.

## Decisiones de borde
- `desapilar` y `cima` sobre pila vacía lanzan `PilaVaciaError`; `Historial.deshacer()` y `rehacer()` la capturan y devuelven `None` para que la interfaz pueda informar sin romperse (CA-18).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
