# CONTROLLER
# Controller encargado de gestionar las operaciones CRUD de Categoria.

from model.categoria import Categoria


class CategoriaController:

    def __init__(self):
        # Lista en memoria donde se almacenan las categorías.
        self.categorias = []

        # Contador para generar IDs automáticamente.
        self.siguiente_id = 1

    # CREATE
    def agregar_categoria(self, nombre, descripcion):

        categoria = Categoria(
            self.siguiente_id,
            nombre,
            descripcion
        )

        self.categorias.append(categoria)
        self.siguiente_id += 1

        return categoria

    # READ
    def listar_categorias(self):
        return self.categorias

    # READ - Buscar una categoría por ID
    def buscar_categoria(self, id_categoria):

        for categoria in self.categorias:

            if categoria.id_categoria == id_categoria:
                return categoria

        return None

    # UPDATE
    def actualizar_categoria(self, id_categoria, nombre, descripcion):

        categoria = self.buscar_categoria(id_categoria)

        if categoria is None:
            return False

        categoria.nombre = nombre
        categoria.descripcion = descripcion

        return True

    # DELETE
    def eliminar_categoria(self, id_categoria):

        categoria = self.buscar_categoria(id_categoria)

        if categoria is None:
            return False

        self.categorias.remove(categoria)

        return True