# Plan — Cola

Versión 1.0 · 2026-11-11 · Implementa: `specs/03-cola/spec.md`

## Estructura elegida: lista enlazada con referencias al primero y al último
| Operación | Cómo | Complejidad |
|---|---|---|
| `encolar` | Enlaza un nodo nuevo tras el último | O(1) |
| `desencolar`, `frente` | Lee o quita el primer nodo | O(1) |
| `esta_vacia`, `tamano` | Contador | O(1) |
| `vaciar` | Suelta las referencias | O(1) amortizado |

## Alternativa descartada: arreglo
Quitar del frente obliga a desplazar todos los elementos (O(n)), o a manejar índices circulares; con nodos enlazados el frente y el final se mueven sin desplazar nada.

## Soportes internos
Solo `Nodo` propio. No se usa `list` ni `collections.deque`.

## Módulo
`estructuras/cola.py` (clase `Cola` y `ColaVaciaError`).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |
