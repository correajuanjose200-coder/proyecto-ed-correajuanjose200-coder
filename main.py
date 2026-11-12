"""Interfaz de consola de "Última Dosis"."""
import sys

from dominio.juego import Juego

AYUDA = """Comandos:
  w/a/s/d  mover (arriba, izquierda, abajo, derecha)
  x        esperar
  u N      usar el objeto N del inventario (desde 1)
  g N      soltar el objeto N en tu celda
  z / r    deshacer / rehacer
  i        ver inventario
  h        ayuda
  q        salir
Mapa: P = Pedro, Z = zombi, E = meta, C = comida, A = agua, # = obstáculo"""


def _mostrar(juego):
    print(juego.dibujar())
    _, _, salud = juego.pedro
    print(f"Turno {juego.turno} · Salud {salud} · Zombis {len(juego.zombis)}")


def _eventos(juego):
    for texto in juego.procesar_eventos():
        print("  >", texto)


def jugar(juego, entrada=input):
    """Bucle de la partida. 'entrada' se puede cambiar para probarlo."""
    print(AYUDA)
    _eventos(juego)
    while juego.estado == "jugando":
        _mostrar(juego)
        try:
            partes = entrada("> ").strip().lower().split()
        except EOFError:
            break
        if not partes:
            continue
        cmd = partes[0]
        if cmd == "q":
            break
        if cmd == "h":
            print(AYUDA)
            continue
        if cmd == "i":
            objetos = juego.inventario.listar()
            if juego.inventario.esta_vacio():
                print("Inventario vacío.")
            for n, obj in enumerate(objetos, 1):
                print(f"  {n}. {'comida' if obj == 'C' else 'agua'}")
            continue
        if cmd in ("w", "a", "s", "d"):
            ok, msg = juego.mover(cmd)
        elif cmd == "x":
            ok, msg = juego.esperar()
        elif cmd in ("u", "g"):
            try:
                pos = int(partes[1]) - 1
            except (IndexError, ValueError):
                print("Usa: u N  o  g N (N = posición desde 1)")
                continue
            ok, msg = juego.usar(pos) if cmd == "u" else juego.soltar(pos)
        elif cmd == "z":
            ok, msg = juego.deshacer()
        elif cmd == "r":
            ok, msg = juego.rehacer()
        else:
            print("Comando desconocido (h = ayuda).")
            continue
        print(msg)
        _eventos(juego)
    _mostrar(juego)
    if juego.estado == "victoria":
        print("¡Llegaste a la meta! VICTORIA.")
    elif juego.estado == "derrota":
        print("Los zombis te alcanzaron. DERROTA.")


def main(interactivo=False, semilla=1):
    print("=== Última Dosis ===")
    print("Proyecto integrador · Estructuras de Datos (ID 706132)")
    if interactivo:
        jugar(Juego(semilla))


if __name__ == "__main__":
    main(True, int(sys.argv[1]) if len(sys.argv) > 1 else 1)
