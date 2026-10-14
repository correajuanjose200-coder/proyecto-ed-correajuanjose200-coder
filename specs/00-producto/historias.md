# Historias de usuario — Última Dosis

Versión 1.0 · 2026-10-14

Contexto: Pedro lleva el antídoto por una ciudad infectada hasta el aeropuerto (`E`). Los zombies (`Z`) lo persiguen. Se juega por turnos en consola.

## Decisiones de reglas (cierran las ambigüedades del borrador)

| # | Tema | Decisión |
|---|---|---|
| D-1 | Recoger | Automático: al pisar una celda con objeto, entra al inventario. No hay comando "recoger". |
| D-2 | Capacidad del inventario | 5 objetos. Si está lleno, el objeto queda en la celda y se genera un evento. |
| D-3 | Contacto | Hay contacto cuando un zombie intenta entrar a la celda de Pedro, o Pedro intenta entrar a la de un zombie. Nadie entra a esa celda. Pedro pierde 25 de salud y ese zombie queda aturdido 1 turno (no se mueve ni ataca). |
| D-4 | Precedencia | Pedro se mueve primero. Si llega a `E` ese turno, gana y los zombies no actúan. Victoria prima sobre derrota. |
| D-5 | Soltar | Solo si la celda de Pedro no tiene otro objeto; si la tiene, se rechaza. |
| D-6 | Eventos | Se generan durante toda la partida (inicio y turnos). Se atienden en orden de llegada. |
| D-7 | Puntaje | Solo se registra al ganar: `max(0, 1000 − 5·turnos + 10·salud_final)`. Desempate: gana la partida registrada primero. |
| D-8 | Rechazos | Una acción inválida se rechaza con mensaje, no consume turno y no cambia el estado. |
| D-9 | Salud | Máximo 100. |

---

## HU-01 · Iniciar partida (F-01) — Must
**Como** jugador, **quiero** empezar una partida con la ciudad, Pedro, zombies y objetos ya colocados, **para** poder jugar desde un estado válido y justo.

- **CA-01** El mapa mide al menos 20×20 y los obstáculos ocupan como máximo el 25 % de las celdas.
- **CA-02** Siempre existe al menos un camino transitable entre Pedro y el aeropuerto al iniciar.
- **CA-03** Hay al menos 2 zombies, cada uno en una celda libre distinta de la de Pedro y la del aeropuerto.
- **CA-04** Hay al menos un objeto de comida y uno de agua en celdas libres.
- **CA-05** Pedro empieza con salud 100 y con el antídoto, y el estado en pantalla muestra ambas cosas.

## HU-02 · Mover a Pedro (F-02) — Must
**Como** jugador, **quiero** mover a Pedro una casilla por turno o esperar, **para** decidir cómo esquivar a los zombies.

- **CA-06** Un movimiento válido (arriba, abajo, izquierda, derecha) cambia la posición de Pedro en una casilla y consume un turno.
- **CA-07** Un movimiento hacia un obstáculo o fuera del mapa se rechaza, no cambia el estado y no consume turno.
- **CA-08** Esperar consume un turno y deja a Pedro en su celda.

## HU-03 · Gestionar el inventario (F-03) — Must
**Como** jugador, **quiero** recoger, usar, soltar y listar objetos, **para** recuperar salud cuando más lo necesito.

- **CA-09** Al pisar una celda con objeto, el objeto sale del mapa y entra al inventario.
- **CA-10** Usar comida suma 20 de salud y usar agua suma 10 (sin pasar de 100); el objeto usado se consume. Usar con inventario vacío se rechaza.
- **CA-11** Soltar deja el objeto en la celda de Pedro y lo quita del inventario; se rechaza si esa celda ya tiene un objeto.
- **CA-12** Con 5 objetos en el inventario, pisar otro objeto lo deja en el mapa y genera un evento.
- **CA-13** Listar muestra los objetos en el orden en que se recogieron; con inventario vacío informa que está vacío.

## HU-04 · Deshacer y rehacer (F-04) — Must
**Como** jugador, **quiero** deshacer y rehacer mis jugadas con todos sus efectos, **para** corregir un error sin empezar de cero.

- **CA-14** Deshacer devuelve a Pedro, a todos los zombies, la salud y el contador de turnos al estado anterior a la acción; deshacer varias veces retrocede en orden inverso al que se jugó.
- **CA-15** Deshacer una recogida devuelve el objeto a su celda y lo quita del inventario.
- **CA-16** Rehacer reaplica la última acción deshecha con los mismos efectos.
- **CA-17** Tras una acción nueva, ya no se puede rehacer lo que estaba deshecho.
- **CA-18** Deshacer sin acciones previas, o rehacer sin acciones deshechas, se rechaza sin cambiar el estado.

## HU-05 · Zombies que persiguen (F-05) — Must
**Como** jugador, **quiero** que los zombies me persigan por el camino más corto, **para** que el juego sea un reto real.

- **CA-19** Después de Pedro, cada zombie avanza exactamente una casilla por un camino de menor longitud hacia Pedro.
- **CA-20** Ningún zombie entra a un obstáculo ni sale del mapa.
- **CA-21** Si un zombie no tiene camino hacia Pedro, se queda quieto ese turno.
- **CA-22** En un contacto (ver D-3), Pedro pierde 25 de salud, el zombie queda aturdido 1 turno y ninguno entra a la celda del otro.

## HU-06 · Ver los eventos del turno (F-06) — Must
**Como** jugador, **quiero** ver qué pasó en cada turno y en qué orden, **para** entender por qué perdí salud o qué recogí.

- **CA-23** Los eventos se muestran en el mismo orden en que ocurrieron dentro del turno.
- **CA-24** Existen eventos de aparición (zombie u objeto), recolección y colisión.
- **CA-25** Cada evento se atiende (se muestra) una sola vez.

## HU-07 · Ganar o perder (F-07) — Must
**Como** jugador, **quiero** saber cuándo gané o perdí, **para** tener un objetivo claro.

- **CA-26** Hay victoria cuando Pedro llega a la celda `E`.
- **CA-27** Hay derrota cuando la salud de Pedro llega a 0 o menos.
- **CA-28** Si Pedro llega a `E` en un turno, hay victoria aunque en ese mismo turno quedaría sin salud (D-4).
- **CA-29** Con la partida terminada, cualquier acción de juego se rechaza.

## HU-08 · Buscar entidades y ver puntajes (F-08) — Must
**Como** jugador, **quiero** buscar un zombie u objeto por su identificador y ver el ranking, **para** planear mi ruta y compararme con mis mejores partidas.

- **CA-30** Buscar por un identificador existente muestra el tipo y la posición de la entidad.
- **CA-31** Buscar un identificador inexistente informa "no encontrada" sin romper el programa.
- **CA-32** Al ganar, se registra el puntaje según D-7.
- **CA-33** El ranking muestra como máximo los 5 mejores puntajes, de mayor a menor.
- **CA-34** Con ningún puntaje registrado, el ranking informa que está vacío.

## HU-09 · Jugar desde la consola (transversal a F-01…F-08) — Must
**Como** jugador, **quiero** un menú de consola que dibuje el mapa, **para** poder usar todas las funciones sin conocer el código.

- **CA-35** Después de cada turno se dibuja el mapa con los símbolos `P`, `Z`, `#`, `.`, `C`, `A`, `E` y el estado (salud, turno, antídoto).
- **CA-36** Una opción de menú inválida o un texto vacío muestra un mensaje y no cierra el programa.
