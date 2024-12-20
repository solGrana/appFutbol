class TorneoCategoria:
    def __init__(self, id, torneo_id, categoria_id):
        self.id = id
        self.torneo_id = torneo_id
        self.categoria_id = categoria_id


    def agregar_categoria(self, categoria):
        # Puedo crear una nueva instancia de TorneoCategoria:
        # nueva_asociacion = TorneoCategoria(id, torneo.id, categoria.id)
        pass

    def eliminar_categoria(self, categoria):
        pass

    @staticmethod
    def obtener_categorias_por_torneo(torneo_id):
        # Lógica para obtener todas las categorías asociadas a un torneo
        pass

    