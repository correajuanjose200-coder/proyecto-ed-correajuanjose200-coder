"""Acción registrada en el historial: lo necesario para deshacer y rehacer."""

TIPOS_VALIDOS = ("mover", "esperar", "recoger", "usar", "soltar")


class Accion:
    """Registro de una acción del jugador que ya se aplicó al juego.

    Guarda el estado de antes y de después para poder revertirla (deshacer)
    o reaplicarla (rehacer). Es solo un registro de datos: no cambia el juego.

    Formato de los datos (tuplas que no se modifican después de crearlas):
        pedro_antes / pedro_despues   : (fila, columna, salud)
        zombis_antes / zombis_despues : ((id, fila, columna), ...)
        objeto                        : objeto afectado, o None si no hay
        turno_antes / turno_despues   : contador de turnos

    Complejidad: crear una Accion es O(1), porque solo guarda referencias.
    Lanza ValueError si el tipo no es uno de TIPOS_VALIDOS.
    """

    def __init__(self, tipo, *, pedro_antes, pedro_despues, zombis_antes,
                 zombis_despues, turno_antes, turno_despues, objeto=None):
        if tipo not in TIPOS_VALIDOS:
            raise ValueError(f"Tipo de acción desconocido: {tipo}")
        self.tipo = tipo
        self.pedro_antes = pedro_antes
        self.pedro_despues = pedro_despues
        self.zombis_antes = zombis_antes
        self.zombis_despues = zombis_despues
        self.turno_antes = turno_antes
        self.turno_despues = turno_despues
        self.objeto = objeto
