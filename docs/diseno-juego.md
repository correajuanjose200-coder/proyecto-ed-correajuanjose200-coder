# "Última Dosis"

Proyecto integrador · Temática A: Motor de juego 2D con pathfinding
Autor: Juan José Correa · Curso: Estructuras de Datos (ID 706132)

## 1. Contexto narrativo

En una ciudad infectada por un virus, Pedro fue enviado a buscar un antídoto y lo encontró, pero su equipo de rescate murió y quedó solo. Debe cruzar la ciudad, conseguir comida y agua, y llegar al aeropuerto, de donde recibió un mensaje de S.O.S., mientras los infectados lo persiguen.

## 2. Descripción general

Juego por turnos que se juega en la consola, sobre una rejilla que representa la ciudad. No hay gráficos, saltos ni desplazamiento lateral: lo importante es la lógica del juego y las estructuras de datos que la sostienen. El jugador controla a Pedro, y en cada turno los zombies calculan una ruta hacia él y avanzan.

## 3. Objetivo

Llevar el antídoto hasta la celda del aeropuerto sin que la salud de Pedro llegue a cero.

## 4. El mundo (mapa)

- Rejilla de 20 × 20 celdas como mínimo.
- Los obstáculos (autos abandonados, escombros, vallas, edificios derrumbados) ocupan máximo el 25 % de las celdas (100 de 400). El resto es transitable.
- Siempre debe existir al menos un camino entre Pedro y el aeropuerto.

| Símbolo | Significado |
|---|---|
| P | Pedro |
| Z | Zombie |
| # | Obstáculo |
| . | Celda libre |
| C | Comida |
| A | Agua |
| R | Refugio (Should) |
| E | Aeropuerto (meta) |

## 5. El jugador

- Se mueve una casilla por turno: arriba, abajo, izquierda, derecha, o esperar.
- No puede atravesar obstáculos ni salir del mapa; un movimiento inválido se rechaza y no consume turno.
- Salud: empieza en 100. El contacto con un zombie le resta 25.
- Lleva el antídoto desde el inicio. Se muestra siempre en el estado de pantalla.

## 6. Objetos e inventario

- Al pisar una celda con objeto, Pedro lo recoge y entra al inventario.
- Objetos: comida (recupera 20 de salud) y agua (recupera 10).
- Operaciones del inventario: agregar, usar, soltar y listar.
- Usar un objeto lo consume. Soltar lo devuelve a la celda donde está Pedro.
- Capacidad máxima del inventario: por definir en la spec (por ejemplo, 5).

## 7. Enemigos

- Mínimo 2 zombies caminantes al iniciar la partida.
- En cada turno, cada zombie calcula una ruta hacia Pedro y avanza una casilla por ella.
- Se mueven después de Pedro. Los zombies no atraviesan obstáculos.
- Colisión: si un zombie queda en la celda de Pedro, o viceversa, Pedro pierde salud.
- Mejoras opcionales (no obligatorias): zombie corredor (2 casillas por turno), zombie grande (más lento y con más daño), zombies que aparecen a mitad de partida.

## 8. Deshacer y rehacer

- Cada acción del jugador se guarda en un historial.
- Deshacer revierte la acción y sus efectos: si deshaces una recogida, el objeto vuelve al mapa; si deshaces un movimiento, los zombies vuelven a su posición anterior.
- Rehacer reaplica la acción deshecha.
- Si haces una acción nueva, lo que se podía rehacer se descarta.

## 9. Eventos

Cada turno genera eventos que se muestran en el orden en que ocurrieron:

- Aparición: un zombie u objeto entra al mapa.
- Recolección: Pedro recoge un objeto.
- Colisión: un zombie alcanza a Pedro.

## 10. Victoria y derrota

- Victoria: Pedro llega a la celda del aeropuerto con el antídoto.
- Derrota: la salud de Pedro llega a 0.

## 11. Búsqueda y puntajes

- Buscar una entidad (zombie, objeto) por su identificador.
- Consultar el ranking de puntajes de las partidas, calculado según los turnos usados y la salud final (fórmula por definir en la spec).

## 12. Interfaz de consola

Menú que dibuja el mapa en cada turno y permite: mover, esperar, recoger, usar, soltar, listar inventario, deshacer, rehacer, ver eventos, buscar entidades y ver puntajes.

## 13. Funcionalidades del proyecto (trazabilidad con el documento)

| ID | Funcionalidad | Dónde se cubre |
|---|---|---|
| F-01 | Iniciar partida | Secciones 4, 5, 6, 7 |
| F-02 | Mover al jugador | Sección 5 |
| F-03 | Inventario | Sección 6 |
| F-04 | Deshacer y rehacer | Sección 8 |
| F-05 | Movimiento de enemigos | Sección 7 |
| F-06 | Eventos en orden | Sección 9 |
| F-07 | Victoria y derrota | Sección 10 |
| F-08 | Buscar entidad / puntajes | Sección 11 |

## 14. Priorización inicial (borrador MoSCoW)

- Must: F-01 a F-08 con lo descrito en las secciones 4 a 12.
- Should: refugios (celdas seguras donde los zombies no entran), zombie corredor.
- Could: zombie grande, jefe final en el aeropuerto, varios niveles.
- Won't (mínimo 2, con razón): gráficos y pixel art (el proyecto se juega en consola); plataformas con salto, trepar y desplazamiento lateral (no es juego por turnos en rejilla); música y efectos de sonido (no aportan a las estructuras de datos).

> Nota: las reglas que aquí quedaban "por definir" (capacidad del inventario, puntaje, contacto, precedencia) se cerraron en `specs/00-producto/historias.md`.
