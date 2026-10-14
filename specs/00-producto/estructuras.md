# Decisión de estructuras — Última Dosis

Versión 1.0 · 2026-10-14

Todas se implementan desde cero en `estructuras/`. La **operación dominante** es la que más se repite en el juego.

| Capacidad | Estructura | Operación dominante y complejidad | Por qué esta | Alternativa descartada y motivo | Dónde se usa |
|---|---|---|---|---|---|
| Deshacer y rehacer | Dos pilas (hechas y deshechas) | Apilar y desapilar la acción más reciente: O(1) | Deshacer y rehacer siempre actúan sobre la última acción. Una acción nueva vacía la pila de deshechas. | Lista doble con cursor: también O(1), pero exige mantener el cursor y cortar la lista en cada acción nueva; más código para el mismo resultado. | `dominio/historial.py` en cada turno de Pedro |
| Inventario de Pedro | Lista enlazada simple (con puntero a la cola) | Agregar al final: O(1). Usar/soltar por posición: O(n), con n ≤ 5. | Conserva el orden de recogida y quitar de cualquier posición no desplaza elementos. | Arreglo con capacidad 5: con n ≤ 5 el costo es igual, pero obliga a desplazar elementos al quitar del medio y a manejar posiciones vacías. | `dominio/inventario.py`; menú de usar, soltar y listar |
| Eventos del juego | Cola | Encolar y atender por el frente: O(1) | Los eventos se atienden por orden de llegada (CA-23). | Cola de prioridad: todos los eventos tienen la misma urgencia, la prioridad solo añadiría O(log n) sin beneficio. | `dominio/eventos.py`; panel de eventos del turno |
| Orden de los turnos | Cola (desencolar y volver a encolar) | Rotar el actor: O(1) | Orden fijo Pedro → zombies por id; los que aparecen a mitad de partida se encolan al final. | Lista circular: equivalente en O(1), pero reutilizar la cola evita un módulo más sin perder nada. | `dominio/turnos.py` |
| Índice de entidades por id | Árbol AVL | Buscar por id: O(log n) garantizado | Los ids se asignan en orden creciente; en un BST simple degeneraría en una lista (O(n)). El AVL se mantiene balanceado y permite listar en orden. | BST: O(n) en el peor caso con ids crecientes. Tabla hash: busca en O(1) promedio, pero no recorre en orden y la función hash habría que implementarla y justificarla. | `dominio/indice.py`; opción "buscar entidad" |
| Ranking de puntajes | Montículo máximo | Insertar: O(log n). Obtener el mejor: O(1). Top 5: O(k log n) | La consulta típica es "los mejores", no el recorrido completo. | AVL: ordena todo en O(n) pero guarda más de lo que se consulta y es más código para un top 5. | `dominio/puntajes.py`; opción "ver ranking" |
| Ruta de los zombies | Grafo implícito sobre la matriz + BFS | BFS: O(V + E) = O(filas × columnas) por zombie y turno | El mapa es de ~400 celdas; el camino con menos pasos basta y es fácil de probar (CA-19). | A* : explora menos celdas, pero exige heurística admisible, más código y más riesgo en la sustentación; queda como Could. | `dominio/rutas.py`; movimiento de zombies y chequeo de CA-02 |
| Representación del mapa | Matriz densa (arreglo 2D) | Consultar o cambiar una celda: O(1) | Se consulta celda por celda en cada turno. Con hasta 25 % de obstáculos y 400 celdas, guardar las vacías cuesta poco. | Matriz dispersa: ahorraría memoria solo si casi todo estuviera vacío; aquí añade búsqueda extra en cada consulta. | `dominio/mapa.py` |

## Soportes internos declarados (regla 4)

- **Matriz densa**: se usa `list` de Python solo como contenedor de tamaño fijo (filas × columnas) y todas las operaciones se implementan en `Mapa`; no hay `append` ni `pop`.
- **BFS**: la lista de celdas visitadas es otra matriz de booleanos del mismo tamaño que el mapa (no `set`); la frontera es la `Cola` propia.
- **Montículo**: el arreglo interno es una `list` de tamaño controlado por el propio montículo.
- Las pilas, la cola y la lista enlazada se construyen con una clase `Nodo` propia, sin `list`.

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
