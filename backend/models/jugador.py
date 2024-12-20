class Jugador:
    def __init__(
        self, id, nombre, total_goles=0, total_amarillas=0, total_rojas=0, equipo=None):
        self.id = id
        self.nombre = nombre
        self.total_goles = total_goles
        self.total_amarillas = total_amarillas
        self.total_rojas = total_rojas
        self.equipo = equipo

    def registrar_evento(self, tipo_evento):
        if tipo_evento == "gol":
            self.total_goles += 1
        elif tipo_evento == "amarilla":
            self.total_amarillas += 1
        elif tipo_evento == "roja":
            self.total_rojas += 1

    def imprimir_estadisticas(self):
        print(f"Jugador: {self.nombre}")
        print(f"Goles: {self.total_goles}")
        print(f"Tarjetas amarillas: {self.total_amarillas}")
        print(f"Tarjetas rojas: {self.total_rojas}")

