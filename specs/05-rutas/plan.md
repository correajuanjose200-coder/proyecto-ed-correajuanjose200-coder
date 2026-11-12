# Plan — Rutas de los zombis

Versión 1.0 · 2026-11-11 · Implementa: `specs/05-rutas/spec.md`

## Estructura elegida: grafo implícito sobre la matriz + búsqueda en anchura (BFS)
Cada celda transitable es un vértice y cada par de celdas vecinas transitables es una arista. El grafo no se construye: los vecinos de una celda se calculan al vuelo (arriba, abajo, izquierda, derecha) consultando `Mapa.es_transitable`.

| Operación | Cómo | Complejidad |
|---|---|---|
| `buscar_ruta` | BFS desde el origen con la `Cola` propia como frontera; al descubrir el destino se reconstruye el primer paso siguiendo los padres hacia atrás | O(V + E) = O(filas × columnas) |
| Consultar vecinos | 4 consultas a `es_transitable` | O(1) por celda |
| Memoria | Matriz de visitadas y matriz de padres, del tamaño del mapa | O(filas × columnas) |

Con V ≤ filas × columnas y E ≤ 4V, el costo por zombi y por turno es O(filas × columnas): unas 400 celdas en un mapa de 20×20.

BFS encuentra el camino con menos pasos porque explora por capas: todas las celdas a distancia k antes que las de distancia k+1. El primer camino que llega al destino es, por tanto, de longitud mínima (CA-R1, CA-19).

## Alternativas descartadas
- **A\***: explora menos celdas, pero exige una heurística admisible y más código; con ~400 celdas la diferencia es pequeña. Queda como Could.
- **Grafo explícito con listas de adyacencia**: duplicaría en memoria la información que ya está en la matriz y habría que reconstruirlo cada vez que cambie el mapa (por ejemplo, al soltar un objeto).

## Soportes internos (regla 4)
- Visitadas y padres: `list` de tamaño fijo (filas × columnas), igual que la matriz del mapa; no hay `append` ni `pop`, y no se usa `set` ni `dict`.
- La frontera es la `Cola` propia (`estructuras/cola.py`).
- El orden de vecinos es una tupla constante de 4 desplazamientos.

## Decisiones de borde
- Otros zombis no bloquean el camino: la regla de contacto vive en el dominio (D-3), no en la búsqueda.
- La búsqueda se detiene al descubrir el destino, sin recorrer todo el mapa.
- `exploradas` se devuelve para poder medir y comparar con A* en `ANALISIS.md`.

## Módulo
`dominio/rutas.py` (función `buscar_ruta` y clase `Ruta`).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-11 | Versión inicial | Entrega final |