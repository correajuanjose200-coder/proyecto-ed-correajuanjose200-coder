# Priorización MoSCoW — Última Dosis

Versión 1.0 · 2026-10-14

## Cálculo de capacidad

> Supuesto de partida: (trabajo en INDER y otros cursos pero siempre en la semana dispongo de 8h libres para dedicar a proyecto).

| Concepto | Horas |
|---|---|
| Tiempo disponible: 8 h/semana × 4 semanas (14 oct – 11 nov) | 32 |
| Menos: `ANALISIS.md`, informe final, `BITACORA.md` y preparar la sustentación | −6 |
| Subtotal | 26 |
| Menos: reserva por imprevistos (15 %) | −4 |
| **Capacidad para Must** | **22** |

## Must (entran sí o sí) — 22 h estimadas (incluyen pruebas)

| Historia | Descripción | Horas |
|---|---|---|
| HU-01 | Iniciar partida y generar mapa con camino garantizado | 3,0 |
| HU-02 | Mover a Pedro y esperar | 2,0 |
| HU-03 | Inventario (recoger, usar, soltar, listar) | 3,0 |
| HU-04 | Deshacer y rehacer | 3,0 |
| HU-05 | Zombies con ruta hacia Pedro (BFS) | 4,0 |
| HU-06 | Eventos en orden | 2,0 |
| HU-07 | Victoria y derrota | 1,5 |
| HU-08 | Búsqueda por id y ranking | 3,5 |
| HU-09 | Consola | (incluida en las anteriores) |
| **Total** | | **22,0** ≤ 22 ✔ |

Los Must caben justo en la capacidad. Por eso Should y Could solo se tocan si sobra tiempo.

## Should (si sobra tiempo)

- **Refugios `R`**: celdas donde los zombies no entran. Cambia la regla de movimiento de zombies y la generación del mapa.
- **Zombie corredor**: se mueve 2 casillas por turno.

## Could

- Zombie grande (más lento, más daño).
- A* como alternativa a BFS, con comparación de celdas exploradas.
- Varios niveles y jefe final en el aeropuerto.

## Won't (esta versión)

| Elemento | Razón |
|---|---|
| Gráficos y pixel art | El proyecto se juega en consola; lo evaluado son las estructuras de datos. |
| Plataformas con salto, trepar y desplazamiento lateral | No es un juego por turnos sobre rejilla. |
| Música y efectos de sonido | No aportan a las estructuras de datos y consumen tiempo de la capacidad. |

## Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-10-14 | Versión inicial | Entrega 1 |
