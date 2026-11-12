# Plan — Inventario

Versión 1.0 · 2026-11-11 · Implementa: `specs/04-inventario/spec.md`

## Estructura elegida: lista enlazada simple con referencia al último nodo
| Operación | Cómo | Complejidad |
|---|---|---|
| `agregar` | Enlaza un nodo tras el último | O(1) |
| `insertar(posicion, ...)` | Al inicio o al final es directo; en medio recorre hasta la posición anterior | O(n), con n ≤ 5 |
| `quitar(posicion)` | Recorre hasta el nodo anterior y lo reenlaza | O(n), con n ≤ 5 |
| `listar` | Recorre de principio a fin entregando cada objeto | O(n) |
| `tamano`, `esta_vacio`, `esta_lleno` | Contador y capacidad | O(1) |

La operación que más se repite es recoger (agregar al final), que es O(1). Usar, soltar y deshacer son O(n), pero n nunca pasa de 5.

## Alternativa descartada: arreglo de capacidad fija
Con n ≤ 5 el costo sería parecido, pero quitar del medio obliga a desplazar elementos y a manejar posiciones vacías. Con nodos, quitar es cambiar una referencia.

## Soportes internos
Solo `Nodo` propio. No se usa `list`; `listar` es un generador que recorre los nodos.

## Decisiones de borde
- El inventario no conoce los objetos ni sus efectos: la regla de cuánta salud da cada uno vive en el dominio.
- `insertar` existe para que deshacer un uso o un soltar devuelva el objeto a su posición original (CA-14, CA-15).

## Módulo
`estructuras/inventario.py` (clase `Inventario`, `InventarioLlenoError`, `PosicionInventarioError`).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |
