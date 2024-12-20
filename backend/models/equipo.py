class Equipo:
    def __init__(self, id, nombre, torneo_categoria_id, escudo):
        self.id = id
        self.nombre = nombre
        self.torneo_categoria_id = torneo_categoria_id
        self.jugadores = []
        self.escudo = escudo
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        jugador.equipo = self # Actualiza el equipo_id del jugador cuando se agrega al equipo

    def eliminar_jugador(self, jugador):
        if jugador in self.jugadores:
            self.jugadores.remove(jugador)
            jugador.equipo = None

    def obtener_jugadores(self):
        return self.jugadores

    def actualizar_puntos(self, goles_favor, goles_contra):
        if goles_favor > goles_contra:
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.puntos += 1
        self.goles_a_favor += goles_favor
        self.goles_en_contra += goles_contra
