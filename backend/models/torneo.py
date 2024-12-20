class Torneo:
    def __init__(self, id, nombre, fecha, descripcion):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.categorias = []

    def __str__(self):
        return f"Torneo: {self.nombre}, Fecha: {self.fecha}"

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def obtener_categorias(self):
        return self.categorias

    def imprimir_categorias(self):
        print(f"Categorías en el torneo '{self.nombre}':")
        for categoria in self.categorias:
            print(f"- {categoria.nombre}: {categoria.descripcion}")