# Constitución del proyecto "Última Dosis"

Versión 1.0 · 2026-10-14 · Autor: Juan José Correa · Curso Estructuras de Datos (ID 706132)

## Principios

1. **La especificación va primero.** Ningún código de un componente se escribe antes de que su `spec.md`, `plan.md` y `tasks.md` estén commiteados. El historial de Git debe mostrarlo.
2. **La spec dice qué, el plan dice cómo.** `spec.md` describe operaciones y criterios de aceptación sin nombrar estructuras ni algoritmos. La estructura y su complejidad viven en `plan.md`.
3. **Todo criterio es verificable.** Cada criterio tiene identificador `CA-XX` y se puede comprobar con una prueba automática o con una salida observable en consola.
4. **Trazabilidad en ambos sentidos.** Cada prueba nombra en su docstring el CA que verifica; cada CA apunta a su prueba en `specs/trazabilidad.md`.
5. **Estructuras propias.** Cada estructura declarada se implementa desde cero en su propio módulo (`estructuras/`). `list`, `dict`, `set`, `collections.deque` y `heapq` no sustituyen una estructura declarada; solo se usan como soporte interno si el `plan.md` lo justifica.
6. **Complejidad declarada.** Toda operación pública lleva en su docstring su complejidad en tiempo.
7. **Pruebas mínimas.** Al menos 3 pruebas por operación pública, incluyendo extremos: vacío, un elemento, elemento inexistente.
8. **Código que puedo explicar.** No integro código (propio, de internet o de una IA) que no pueda explicar línea por línea.
9. **Uso de IA declarado.** Todo uso de asistentes de IA se registra en `BITACORA.md` y en el informe final.
10. **Cambios con historia.** Cambiar una decisión después de la Entrega 1 se hace con un commit en la spec o el plan y una línea en su historial de cambios con el motivo.

## Reglas técnicas

- Python 3.11 o superior; solo `pytest` (y opcionalmente `matplotlib`) como dependencias.
- Un módulo por estructura; la lógica del juego vive en `dominio/`; sin archivos monolíticos.
- Commits pequeños, uno por tarea de `tasks.md`, con prefijos `spec(...)`, `plan(...)`, `test(...)`, `feat(...)`, `fix(...)`.
- Las partidas son deterministas cuando se les da una semilla (para poder probar y demostrar).

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
