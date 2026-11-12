# Spec — Inventario

Versión 1.0 · 2026-11-11 · Soporta: HU-03 (CA-09 a CA-13) y el deshacer de HU-04 (CA-14, CA-15). Must

## Propósito
Guardar los objetos que lleva Pedro, en el orden en que los recogió, con un máximo de objetos.

## Convenciones
- Las posiciones cuentan desde 0 (el primer objeto recogido está en la posición 0). La consola muestra desde 1 y convierte.
- El inventario guarda cualquier objeto que se le dé; no conoce sus efectos (eso lo decide el dominio).
- Capacidad por defecto: 5 objetos (D-2).

## Operaciones

| Operación | Entrada | Resultado | Errores |
|---|---|---|---|
| `Inventario(capacidad=5)` | Capacidad máxima | Inventario vacío | `ValueError` si la capacidad es menor que 1 |
| `agregar(objeto)` | Un objeto | El objeto queda en la última posición | `InventarioLlenoError` si ya está lleno |
| `insertar(posicion, objeto)` | Posición entre 0 y `tamano()` y un objeto | El objeto queda en esa posición; los demás conservan su orden | `InventarioLlenoError` si está lleno; `PosicionInventarioError` si la posición está fuera de rango |
| `quitar(posicion)` | Posición entre 0 y `tamano()-1` | Quita y devuelve el objeto de esa posición; los demás conservan su orden | `PosicionInventarioError` si está vacío o la posición está fuera de rango |
| `listar()` | — | Entrega los objetos en orden de recogida, sin modificar nada | — |
| `tamano()` | — | Cantidad de objetos | — |
| `esta_vacio()` | — | Verdadero si no hay objetos | — |
| `esta_lleno()` | — | Verdadero si el tamaño alcanzó la capacidad | — |

## Criterios de aceptación
Criterios de producto: **CA-09, CA-10 (vacío), CA-11, CA-12, CA-13** (ver `00-producto/historias.md`). Además:

- **CA-I1** `agregar` deja los objetos en el orden en que entraron (base de CA-13).
- **CA-I2** Con el inventario lleno, `agregar` e `insertar` lanzan `InventarioLlenoError` y no cambian nada (base de CA-12).
- **CA-I3** `quitar` devuelve el objeto de la posición pedida y los demás conservan su orden; con inventario vacío o posición fuera de rango lanza `PosicionInventarioError` y no cambia nada (base de CA-10 y CA-11).
- **CA-I4** `insertar` pone el objeto en la posición pedida sin alterar el orden de los demás; quitar un objeto e insertarlo en la misma posición deja el inventario como estaba (base de CA-14 y CA-15).
- **CA-I5** `listar` con inventario vacío no entrega nada y nunca modifica el inventario (base de CA-13).
- **CA-I6** Un inventario nuevo está vacío y tiene capacidad 5 por defecto; una capacidad menor que 1 lanza `ValueError`.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |
