class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def obtener_equipos(self):
        return self.equipos

    def __str__(self):
        return f"Categoría: {self.nombre}"
