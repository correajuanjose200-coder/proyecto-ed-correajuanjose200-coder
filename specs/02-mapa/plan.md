# Plan — Mapa de la ciudad

Versión 1.0 · 2026-11-06 · Implementa: `specs/02-mapa/spec.md`

## Estructura elegida: matriz densa (arreglo 2D)
Una celda por posición, accesible por (fila, columna).

| Operación | Cómo | Complejidad |
|---|---|---|
| `dentro`, `obtener`, `poner`, `es_transitable` | Acceso directo por índices | O(1) |
| `contar`, `proporcion_obstaculos` | Recorrer toda la matriz | O(filas × columnas) |
| `generar` | Abrir un corredor libre entre inicio y meta, y colocar obstáculos solo fuera de él | O(filas × columnas) |
| `dibujar` | Recorrer toda la matriz | O(filas × columnas) |

## Alternativa descartada: matriz dispersa
Ahorra memoria solo si casi todo está vacío. Aquí hasta el 25 % son obstáculos y además se consulta celda por celda en cada turno; la dispersa añadiría una búsqueda en cada consulta.

## Soportes internos
`list` de Python solo como contenedor de tamaño fijo (filas × columnas), creado una vez. No hay `append` ni `pop`; todas las operaciones están implementadas en `Mapa`.

## Decisiones de borde
- `generar` garantiza el camino abriendo primero el corredor y poniendo obstáculos solo fuera de él (CA-02), sin usar BFS, para que el mapa no dependa del componente de rutas.
- `generar` recibe la semilla para que las pruebas sean repetibles.

## Módulo
`dominio/mapa.py` (clase `Mapa` y `PosicionInvalidaError`).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-11-06 | Versión inicial | Entrega 2 |
