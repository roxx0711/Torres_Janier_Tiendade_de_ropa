# CONTROLLER

# Controller encargado de gestionar las operaciones CRUD
# de Categoria y las reglas de negocio relacionadas
# con los productos.

from model.categoria import Categoria


class CategoriaController:

    def __init__(self):

        # Lista en memoria donde se almacenan
        # las categorías.
        self.categorias = []

        # Contador para generar IDs automáticamente.
        self.siguiente_id = 1

    # ==================================================
    # CREATE
    # ==================================================

    def agregar_categoria(
        self,
        nombre,
        descripcion
    ):

        categoria = Categoria(
            self.siguiente_id,
            nombre,
            descripcion
        )

        self.categorias.append(categoria)

        self.siguiente_id += 1

        return categoria

    # ==================================================
    # READ
    # ==================================================

    def listar_categorias(self):

        return self.categorias

    # ==================================================
    # BUSCAR CATEGORÍA
    # ==================================================

    def buscar_categoria(
        self,
        id_categoria
    ):

        for categoria in self.categorias:

            if categoria.id_categoria == id_categoria:

                return categoria

        return None

    # ==================================================
    # UPDATE
    # ==================================================

    def actualizar_categoria(
        self,
        id_categoria,
        nombre,
        descripcion
    ):

        categoria = (
            self.buscar_categoria(
                id_categoria
            )
        )

        if categoria is None:

            return False

        categoria.nombre = nombre

        categoria.descripcion = descripcion

        return True

    # ==================================================
    # BUSCAR PRODUCTOS DE UNA CATEGORÍA
    # ==================================================

    def obtener_productos_categoria(
        self,
        id_categoria,
        productos
    ):

        productos_categoria = []

        for producto in productos:

            if producto.id_categoria == id_categoria:

                productos_categoria.append(producto)

        return productos_categoria

    # ==================================================
    # DELETE CATEGORÍA
    # ==================================================

    def eliminar_categoria(
        self,
        id_categoria,
        productos
    ):

        # Buscar la categoría.

        categoria = (
            self.buscar_categoria(
                id_categoria
            )
        )

        # Si no existe, no se puede eliminar.

        if categoria is None:

            return False

        # ==================================================
        # BUSCAR PRODUCTOS ASOCIADOS
        # ==================================================

        productos_categoria = (
            self.obtener_productos_categoria(
                id_categoria,
                productos
            )
        )

        # ==================================================
        # ELIMINAR PRODUCTOS ASOCIADOS
        # ==================================================

        for producto in productos_categoria:

            productos.remove(producto)

        # ==================================================
        # ELIMINAR CATEGORÍA
        # ==================================================

        self.categorias.remove(categoria)

        return True