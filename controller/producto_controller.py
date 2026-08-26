# CONTROLLER
# Controller encargado de gestionar los productos
# y las reglas de negocio relacionadas con ellos.

from model.producto import Producto


class ProductoController:

    def __init__(self, categoria_controller):

        # Lista en memoria donde se almacenan los productos.
        self.productos = []

        # Contador para generar IDs automáticamente.
        self.siguiente_id = 1

        # Controller de categorías para comprobar
        # que la categoría exista.
        self.categoria_controller = categoria_controller

    # CREATE
    def agregar_producto(self, nombre, precio, stock, id_categoria):

        # REGLA DE NEGOCIO:
        # Un producto debe pertenecer a una categoría existente.
        categoria = self.categoria_controller.buscar_categoria(id_categoria)

        if categoria is None:
            return None

        producto = Producto(
            self.siguiente_id,
            nombre,
            precio,
            stock,
            id_categoria
        )

        self.productos.append(producto)
        self.siguiente_id += 1

        return producto

    # READ
    def listar_productos(self):
        return self.productos

    # READ - Buscar producto por ID
    def buscar_producto(self, id_producto):

        for producto in self.productos:

            if producto.id_producto == id_producto:
                return producto

        return None

    # UPDATE
    def actualizar_producto(
        self,
        id_producto,
        nombre,
        precio,
        stock,
        id_categoria
    ):

        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        # REGLA DE NEGOCIO:
        # El producto solamente puede actualizarse
        # si la categoría indicada existe.
        categoria = self.categoria_controller.buscar_categoria(id_categoria)

        if categoria is None:
            return False

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.id_categoria = id_categoria

        return True

    # DELETE
    def eliminar_producto(self, id_producto):

        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        self.productos.remove(producto)

        return True

    # Obtener el nombre de la categoría de un producto
    def obtener_nombre_categoria(self, id_categoria):

        categoria = self.categoria_controller.buscar_categoria(id_categoria)

        if categoria is None:
            return "Sin categoría"

        return categoria.nombre

    # REGLAS DE NEGOCIO DE DESCUENTOS
    def calcular_descuento(
        self,
        precio,
        tipo_persona,
        nombre_profesor
    ):

        # Estudiante = 10%
        # Profesor Paulo Taype = 80%
        # Otro profesor = 30%

        if tipo_persona == "estudiante":

            descuento = 0.10

        elif (
            tipo_persona == "profesor"
            and nombre_profesor.lower() == "paulo taype"
        ):

            descuento = 0.80

        elif tipo_persona == "profesor":

            descuento = 0.30

        else:

            descuento = 0.30

        valor_descuento = precio * descuento
        precio_final = precio - valor_descuento

        return (
            descuento,
            valor_descuento,
            precio_final
        )