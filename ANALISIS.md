# ANÁLISIS de complejidad

Versión final · 2026-11-11. n = elementos de la estructura; F x C = celdas del mapa (20 x 20 = 400).

## Tabla de complejidad (lo implementado)

| Módulo | Operación | Complejidad |
|---|---|---|
| `estructuras/pila.py` | apilar, desapilar, cima, tamano, esta_vacia | O(1) |
| `estructuras/pila.py` | vaciar | O(n) (suelta nodos uno a uno) |
| `estructuras/cola.py` | encolar, desencolar, frente, tamano, esta_vacia | O(1) |
| `estructuras/cola.py` | vaciar | O(n) |
| `estructuras/inventario.py` | agregar (al final, con puntero al último) | O(1) |
| `estructuras/inventario.py` | insertar, quitar, listar (por posición) | O(n), n <= 5 |
| `dominio/historial.py` | registrar, deshacer, rehacer | O(1) |
| `dominio/accion.py` | crear una acción | O(1) |
| `dominio/mapa.py` | obtener, poner, dentro, es_transitable | O(1) |
| `dominio/mapa.py` | contar, dibujar, proporcion_obstaculos | O(F x C) |
| `dominio/mapa.py` | generar | O(F x C) más la verificación del camino |
| `dominio/rutas.py` | buscar_ruta (BFS) | O(V + E) = O(F x C) |

| `dominio/juego.py` | un turno (mover, esperar, usar, soltar) | O(Z × F × C), con Z zombis: cada zombi hace un BFS |
| `dominio/juego.py` | deshacer, rehacer | O(1) en el historial; el inventario cuesta O(n) con n ≤ 5 |
| `dominio/juego.py` | procesar_eventos | O(k), con k eventos pendientes |
| `dominio/juego.py` | dibujar | O(F × C × Z) |
| `dominio/juego.py` | crear la partida | esperado O((objetos + zombis) × F × C): cada celda candidata se valida con un BFS |

## Medición: celdas exploradas por BFS
Camino de `inicio` a `meta` en mapas de 20 × 20 generados con las semillas 1 a 10 (320 celdas transitables en cada uno):

| Semilla | Pasos del camino | Celdas exploradas |
|---|---|---|
| 1 | 38 | 316 |
| 2 | 38 | 320 |
| 3 | 38 | 319 |
| 4 | 38 | 319 |
| 5 | 38 | 320 |
| 6 | 38 | 318 |
| 7 | 38 | 318 |
| 8 | 38 | 318 |
| 9 | 38 | 315 |
| 10 | 38 | 316 |

En este trayecto largo, BFS visita casi todo el mapa (entre 315 y 320 de 320). No se implementó A*, así que no hay comparación medida contra él.

## Comparación de decisiones contra la alternativa descartada

**1. Deshacer y rehacer: dos pilas frente a lista doble con cursor.** Las dos dan deshacer y rehacer en O(1). Con la lista doble, cada acción nueva obliga a cortar la lista en el cursor, lo que agrega casos y código. Con dos pilas basta vaciar la pila de deshechas: `registrar` es O(1) amortizado, porque vaciar cuesta O(n) pero cada acción se descarta una sola vez.

**2. Inventario: lista enlazada con puntero al último frente a arreglo de capacidad 5.** Agregar es O(1) en ambas, y quitar o insertar en el medio es O(n) en ambas. Con n ≤ 5 el costo es prácticamente igual. La lista evita desplazar elementos y manejar posiciones vacías. Con una capacidad grande, el arreglo ganaría en acceso por posición (O(1)) a cambio de desplazar en O(n).

**3. Ruta de los zombis: BFS frente a A\*.** BFS cuesta O(V + E) = O(F × C) por zombi y por turno, y encuentra el camino más corto sin heurística que justificar. A\* exploraría menos celdas, pero exige una heurística admisible y más código. Con 400 celdas la diferencia práctica es pequeña, y por eso A\* quedó como Could.

## Lo que no se implementó
AVL de entidades, montículo de ranking, cola de turnos propia, antídoto y aturdimiento de zombis (ver `moscow.md` v1.1).
