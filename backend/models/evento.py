class Evento:
    def __init__(self, id, partido_id, tipo, jugador_id, minuto):
        self.id = id
        self.partido_id = partido_id
        self.tipo = tipo  # 'roja', 'amarilla', 'gol'
        self.jugador_id = jugador_id
        self.minuto = minuto
