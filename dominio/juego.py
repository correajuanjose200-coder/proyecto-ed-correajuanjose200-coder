"""Juego: reglas de la partida e integración de las estructuras."""
import random

from dominio.accion import Accion
from dominio.historial import Historial
from dominio.mapa import AGUA, COMIDA, LIBRE, Mapa
from dominio.rutas import buscar_ruta
from estructuras.cola import Cola
from estructuras.inventario import Inventario, PosicionInventarioError

SALUD_INICIAL = 3
SALUD_MAXIMA = 5
_MOVIMIENTOS = (("w", -1, 0), ("s", 1, 0), ("a", 0, -1), ("d", 0, 1))


def _nombre(simbolo):
    return "comida" if simbolo == COMIDA else "agua"


class Juego:
    """Una partida. El estado de Pedro y de los zombis son tuplas inmutables.

    Cada acción válida consume un turno, mueve a los zombis (BFS), se registra
    en el Historial (dos pilas) y deja eventos en una Cola, en orden.
    """

    def __init__(self, semilla=1, filas=20, columnas=20, n_zombis=2, n_objetos=3):
        self.mapa = Mapa.generar(filas, columnas, semilla)
        self.inventario = Inventario(5)
        self.historial = Historial()
        self._eventos = Cola()
        self.turno = 0
        rng = random.Random(semilla)
        ocupadas = (tuple(self.mapa.inicio), tuple(self.mapa.meta))
        for simbolo in (COMIDA, AGUA):
            for _ in range(n_objetos):
                celda = self._celda_libre(rng, ocupadas, 0)
                ocupadas = ocupadas + (celda,)
                self.mapa.poner(celda[0], celda[1], simbolo)
        zombis = []
        for zid in range(1, n_zombis + 1):
            celda = self._celda_libre(rng, ocupadas, 8)
            ocupadas = ocupadas + (celda,)
            zombis.append((zid, celda[0], celda[1]))
            self._emitir(f"Aparece el zombi {zid} en {celda}")
        self.zombis = tuple(zombis)
        self.pedro = (self.mapa.inicio[0], self.mapa.inicio[1], SALUD_INICIAL)

    # ---------- consultas ----------
    @property
    def estado(self):
        """'derrota', 'victoria' o 'jugando', calculado del estado actual."""
        f, c, salud = self.pedro
        if salud <= 0:
            return "derrota"
        if (f, c) == tuple(self.mapa.meta):
            return "victoria"
        return "jugando"

    def procesar_eventos(self):
        """Saca los eventos pendientes en el orden en que ocurrieron."""
        salida = []
        while not self._eventos.esta_vacia():
            salida.append(self._eventos.desencolar())
        return salida

    def dibujar(self):
        """Mapa en texto: P = Pedro, Z = zombi."""
        lineas = []
        for f in range(self.mapa.filas):
            linea = ""
            for c in range(self.mapa.columnas):
                if (f, c) == (self.pedro[0], self.pedro[1]):
                    linea += "P"
                elif self._zombi_en(f, c) is not None:
                    linea += "Z"
                else:
                    linea += self.mapa.obtener(f, c)
            lineas.append(linea)
        return "\n".join(lineas)

    # ---------- acciones del jugador ----------
    def mover(self, tecla):
        """Mueve a Pedro con w/a/s/d. Devuelve (ok, mensaje)."""
        if self.estado != "jugando":
            return False, "La partida ya terminó."
        for t, df, dc in _MOVIMIENTOS:
            if t == tecla:
                break
        else:
            return False, "Dirección desconocida."
        f, c, salud = self.pedro
        nf, nc = f + df, c + dc
        if not self.mapa.dentro(nf, nc) or not self.mapa.es_transitable(nf, nc):
            return False, "Hay un obstáculo o el borde del mapa."
        if self._zombi_en(nf, nc) is not None:
            return False, "Un zombi bloquea el paso."
        simbolo = self.mapa.obtener(nf, nc)
        if simbolo in (COMIDA, AGUA) and not self.inventario.esta_lleno():
            pos = self.inventario.tamano()
            self.inventario.agregar(simbolo)
            self.mapa.poner(nf, nc, LIBRE)
            self._emitir(f"Recogiste {_nombre(simbolo)}")
            self._turno("recoger", nf, nc, salud, (simbolo, pos))
        else:
            if simbolo in (COMIDA, AGUA):
                self._emitir("Inventario lleno: dejas el objeto en el suelo")
            self._turno("mover", nf, nc, salud)
        return True, "Te moviste."

    def esperar(self):
        if self.estado != "jugando":
            return False, "La partida ya terminó."
        f, c, salud = self.pedro
        self._turno("esperar", f, c, salud)
        return True, "Esperaste."

    def usar(self, pos):
        """Usa el objeto de la posición pos (desde 0): comida +2, agua +1."""
        if self.estado != "jugando":
            return False, "La partida ya terminó."
        try:
            simbolo = self.inventario.quitar(pos)
        except PosicionInventarioError:
            return False, "No hay objeto en esa posición."
        f, c, salud = self.pedro
        mejora = 2 if simbolo == COMIDA else 1
        self._emitir(f"Usaste {_nombre(simbolo)}")
        self._turno("usar", f, c, min(SALUD_MAXIMA, salud + mejora), (simbolo, pos))
        return True, f"Usaste {_nombre(simbolo)}."

    def soltar(self, pos):
        """Suelta el objeto de la posición pos en la celda de Pedro (si está libre)."""
        if self.estado != "jugando":
            return False, "La partida ya terminó."
        f, c, salud = self.pedro
        if self.mapa.obtener(f, c) != LIBRE:
            return False, "Aquí ya hay algo: muévete a una celda libre."
        try:
            simbolo = self.inventario.quitar(pos)
        except PosicionInventarioError:
            return False, "No hay objeto en esa posición."
        self.mapa.poner(f, c, simbolo)
        self._emitir(f"Soltaste {_nombre(simbolo)}")
        self._turno("soltar", f, c, salud, (simbolo, pos))
        return True, f"Soltaste {_nombre(simbolo)}."

    def deshacer(self):
        accion = self.historial.deshacer()
        if accion is None:
            return False, "No hay nada que deshacer."
        if accion.tipo == "recoger":
            simbolo, pos = accion.objeto
            self.inventario.quitar(pos)
            self.mapa.poner(accion.pedro_despues[0], accion.pedro_despues[1], simbolo)
        elif accion.tipo == "usar":
            simbolo, pos = accion.objeto
            self.inventario.insertar(pos, simbolo)
        elif accion.tipo == "soltar":
            simbolo, pos = accion.objeto
            self.mapa.poner(accion.pedro_despues[0], accion.pedro_despues[1], LIBRE)
            self.inventario.insertar(pos, simbolo)
        self.pedro = accion.pedro_antes
        self.zombis = accion.zombis_antes
        self.turno = accion.turno_antes
        self._emitir(f"Deshiciste: {accion.tipo}")
        return True, f"Deshiciste: {accion.tipo}."

    def rehacer(self):
        accion = self.historial.rehacer()
        if accion is None:
            return False, "No hay nada que rehacer."
        if accion.tipo == "recoger":
            simbolo, pos = accion.objeto
            self.inventario.agregar(simbolo)
            self.mapa.poner(accion.pedro_despues[0], accion.pedro_despues[1], LIBRE)
        elif accion.tipo == "usar":
            self.inventario.quitar(accion.objeto[1])
        elif accion.tipo == "soltar":
            simbolo, pos = accion.objeto
            self.inventario.quitar(pos)
            self.mapa.poner(accion.pedro_despues[0], accion.pedro_despues[1], simbolo)
        self.pedro = accion.pedro_despues
        self.zombis = accion.zombis_despues
        self.turno = accion.turno_despues
        self._emitir(f"Rehiciste: {accion.tipo}")
        return True, f"Rehiciste: {accion.tipo}."

    # ---------- internos ----------
    def _emitir(self, texto):
        self._eventos.encolar(texto)

    def _zombi_en(self, f, c):
        for zid, zf, zc in self.zombis:
            if (zf, zc) == (f, c):
                return zid
        return None

    def _celda_libre(self, rng, ocupadas, dist_min):
        """Celda LIBRE al azar (con semilla), lejos del inicio y alcanzable."""
        ini = self.mapa.inicio
        while True:
            f = rng.randrange(self.mapa.filas)
            c = rng.randrange(self.mapa.columnas)
            if self.mapa.obtener(f, c) != LIBRE or (f, c) in ocupadas:
                continue
            if abs(f - ini[0]) + abs(c - ini[1]) < dist_min:
                continue
            if buscar_ruta(self.mapa, tuple(ini), (f, c)) is None:
                continue
            return (f, c)

    def _turno(self, tipo, f, c, salud, objeto=None):
        """Aplica el turno: nuevo estado de Pedro, zombis se mueven, se registra."""
        antes_p, antes_z, turno_antes = self.pedro, self.zombis, self.turno
        self.pedro = (f, c, salud)
        self.turno += 1
        self._mover_zombis()
        self.historial.registrar(Accion(
            tipo, pedro_antes=antes_p, pedro_despues=self.pedro,
            zombis_antes=antes_z, zombis_despues=self.zombis,
            turno_antes=turno_antes, turno_despues=self.turno, objeto=objeto))

    def _mover_zombis(self):
        f, c, salud = self.pedro
        actuales = list(self.zombis)  # soporte local; se guarda como tupla
        for i in range(len(actuales)):
            zid, zf, zc = actuales[i]
            ruta = buscar_ruta(self.mapa, (zf, zc), (f, c))
            if ruta is None:
                continue
            if ruta.distancia <= 1:
                salud -= 1
                self._emitir(f"Colisión: el zombi {zid} te ataca (salud {salud})")
                continue
            sf, sc = ruta.siguiente
            if self._ocupada_por_otro(actuales, i, sf, sc):
                continue
            actuales[i] = (zid, sf, sc)
        self.zombis = tuple(actuales)
        self.pedro = (f, c, salud)

    @staticmethod
    def _ocupada_por_otro(actuales, i, f, c):
        for j in range(len(actuales)):
            if j != i and (actuales[j][1], actuales[j][2]) == (f, c):
                return True
        return False
