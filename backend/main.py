from models.torneo import Torneo
from models.categoria import Categoria
from models.torneo_categoria import TorneoCategoria
from models.equipo import Equipo
from models.partido import Partido
from models.jugador import Jugador
from models.evento import Evento

# Ejemplo de uso:

# Crear Torneo y Categoría
torneo = Torneo(1, "Torneo clausura", "11-01-2024", "Competencia anual")
categoria_reserva = Categoria(1, "Reserva", "la reserva")
torneo.agregar_categoria(categoria_reserva)

# Crear Equipos y Jugadores
equipo1 = Equipo(1, "Ferro", categoria_reserva.id, "escudo1.png")
equipo2 = Equipo(2, "River", categoria_reserva.id, "escudo2.png")
jugador1 = Jugador(1, "Sol Graña")
jugador2 = Jugador(2, "Agustina Gomez")
jugador3 = Jugador(3, "Sofia Martinez")
jugador4 = Jugador(4, "Camila Belen")
jugador5 = Jugador(5, "Paula Casas")
jugador6 = Jugador(6, "Romina Gomez")


equipo1.agregar_jugador(jugador1)
equipo2.agregar_jugador(jugador2)
equipo1.agregar_jugador(jugador3)
equipo2.agregar_jugador(jugador4)
equipo1.agregar_jugador(jugador5)
equipo2.agregar_jugador(jugador6)


# Agregar equipos a la categoría
categoria_reserva.agregar_equipo(equipo1)
categoria_reserva.agregar_equipo(equipo2)

# Crear Partido y agregar Eventos
partido = Partido(1, categoria_reserva.id, "20-01-2024", equipo1, equipo2)

evento1 = Evento(
    1, partido.id, "gol", jugador1.id, 23
)  # Gol de Sol Graña en el minuto 23
evento2 = Evento(
    2, partido.id, "amarilla", jugador2.id, 45
)  # Tarjeta amarilla para Agustina Gomez

# Agregar eventos y obtener el resultado
partido.agregar_evento(evento1)
partido.agregar_evento(evento2)

# Obtener Resultado
resultado = partido.obtener_resultado()
print(
    f"\nResultado del partido: {equipo1.nombre} {resultado[0]} - {equipo2.nombre} {resultado[1]}"
)

# Imprimir estadísticas de los jugadores
partido.imprimir_estadisticas_jugadores()

# Imprimir categorías del torneo
torneo.imprimir_categorias()

