class Partido:
    def __init__(self, id, torneo_cat_id, fecha, equipo1, equipo2):
        self.id = id
        self.torneo_cat_id = torneo_cat_id
        self.fecha = fecha
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

        # Actualiza estadísticas de cada jugador basado en el tipo de evento
        for jugador in self.equipo1.jugadores + self.equipo2.jugadores:
            if jugador.id == evento.jugador_id:
                if evento.tipo == "gol":
                    jugador.total_goles += 1
                elif evento.tipo == "amarilla":
                    jugador.total_amarillas += 1
                elif evento.tipo == "roja":
                    jugador.total_rojas += 1

    def obtener_eventos(self):
        return self.eventos

    def obtener_resultado(self):
        # Crear listas de IDs de jugadores para cada equipo
        jugadores_equipo1 = [jugador.id for jugador in self.equipo1.jugadores]
        jugadores_equipo2 = [jugador.id for jugador in self.equipo2.jugadores]

        # Contar los goles de cada equipo usando las listas de IDs de jugadores
        goles_equipo1 = sum(
            1
            for e in self.eventos
            if e.tipo == "gol" and e.jugador_id in jugadores_equipo1
        )
        goles_equipo2 = sum(
            1
            for e in self.eventos
            if e.tipo == "gol" and e.jugador_id in jugadores_equipo2
        )

        return goles_equipo1, goles_equipo2

    def imprimir_estadisticas_jugadores(self):
        print(
            f"Estadísticas del partido entre {self.equipo1.nombre} y {self.equipo2.nombre}:"
        )
        # Imprimir estadísticas del equipo 1
        print(f"Equipo: {self.equipo1.nombre}")
        for jugador in self.equipo1.jugadores:
            jugador.imprimir_estadisticas()
            print("-------------------------------")

        # Imprimir estadísticas del equipo 2
        print(f"\nEquipo: {self.equipo2.nombre}")
        for jugador in self.equipo2.jugadores:
            jugador.imprimir_estadisticas()
            print("-------------------------------")
