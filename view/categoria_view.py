# VIEW

# Vista encargada de gestionar las categorías
# mediante la consola.

from tabulate import tabulate
import time


class CategoriaView:

    def __init__(self, controller, producto_controller):

        self.controller = controller

        # Controller de productos.
        # Se utiliza para comprobar si una categoría
        # tiene productos asociados.
        self.producto_controller = producto_controller

    # ==================================================
    # PAUSAS
    # ==================================================

    def esperar(self, segundos=1.5):

        time.sleep(segundos)

    def cargar(self, mensaje):

        print(f"\n{mensaje}...")

        self.esperar(1.5)

    def continuar(self):

        input("\nPresione ENTER para continuar...")

    # ==================================================
    # LISTAR CATEGORÍAS
    # ==================================================

    def mostrar_categorias(self):

        self.cargar("Cargando categorías")

        categorias = (
            self.controller.listar_categorias()
        )

        if not categorias:

            print(
                "\nNo existen categorías registradas."
            )

            self.continuar()

            return False

        datos = []

        for categoria in categorias:

            datos.append({

                "ID": categoria.id_categoria,

                "NOMBRE": categoria.nombre,

                "DESCRIPCIÓN": categoria.descripcion

            })

        print("\n" + "=" * 70)

        print(
            " " * 25 +
            "CATEGORÍAS"
        )

        print("=" * 70)

        print(
            tabulate(
                datos,
                headers="keys",
                tablefmt="grid",
                showindex=False,
                stralign="center",
                numalign="center"
            )
        )

        print("=" * 70)

        return True

    # ==================================================
    # AGREGAR CATEGORÍA
    # ==================================================

    def agregar_categoria(self):

        print("\n" + "=" * 55)

        print(
            " " * 18 +
            "AGREGAR CATEGORÍA"
        )

        print("=" * 55)

        nombre = input(
            "\nIngrese el nombre de la categoría: "
        ).strip()

        if not nombre:

            print(
                "\nEl nombre no puede estar vacío."
            )

            self.continuar()

            return

        descripcion = input(
            "Ingrese la descripción: "
        ).strip()

        if not descripcion:

            print(
                "\nLa descripción no puede estar vacía."
            )

            self.continuar()

            return

        self.cargar(
            "Registrando categoría"
        )

        categoria = (
            self.controller.agregar_categoria(
                nombre,
                descripcion
            )
        )

        print(
            "\nCategoría agregada correctamente."
        )

        print(
            f"ID asignado: "
            f"{categoria.id_categoria}"
        )

        self.continuar()

    # ==================================================
    # ACTUALIZAR CATEGORÍA
    # ==================================================

    def actualizar_categoria(self):

        categorias_existen = (
            self.mostrar_categorias()
        )

        if not categorias_existen:

            self.continuar()

            return

        try:

            id_categoria = int(
                input(
                    "\nIngrese el ID de la categoría "
                    "a actualizar: "
                )
            )

        except ValueError:

            print(
                "\nDebe ingresar un número válido."
            )

            self.continuar()

            return

        categoria = (
            self.controller.buscar_categoria(
                id_categoria
            )
        )

        if categoria is None:

            print(
                "\nLa categoría no existe."
            )

            self.continuar()

            return

        nombre = input(
            "\nNuevo nombre: "
        ).strip()

        if not nombre:

            print(
                "\nEl nombre no puede estar vacío."
            )

            self.continuar()

            return

        descripcion = input(
            "Nueva descripción: "
        ).strip()

        if not descripcion:

            print(
                "\nLa descripción no puede estar vacía."
            )

            self.continuar()

            return

        self.cargar(
            "Actualizando categoría"
        )

        resultado = (
            self.controller.actualizar_categoria(
                id_categoria,
                nombre,
                descripcion
            )
        )

        if resultado:

            print(
                "\nCategoría actualizada correctamente."
            )

        else:

            print(
                "\nNo se pudo actualizar la categoría."
            )

        self.continuar()

    # ==================================================
    # ELIMINAR CATEGORÍA
    # ==================================================

    def eliminar_categoria(self):

        categorias_existen = (
            self.mostrar_categorias()
        )

        if not categorias_existen:

            self.continuar()

            return

        try:

            id_categoria = int(
                input(
                    "\nIngrese el ID de la categoría "
                    "a eliminar: "
                )
            )

        except ValueError:

            print(
                "\nDebe ingresar un número válido."
            )

            self.continuar()

            return

        categoria = (
            self.controller.buscar_categoria(
                id_categoria
            )
        )

        if categoria is None:

            print(
                "\nLa categoría no existe."
            )

            self.continuar()

            return

        # ==================================================
        # BUSCAR PRODUCTOS ASOCIADOS
        # ==================================================

        productos = (
            self.producto_controller.listar_productos()
        )

        productos_categoria = (
            self.controller.obtener_productos_categoria(
                id_categoria,
                productos
            )
        )

        # ==================================================
        # SI LA CATEGORÍA TIENE PRODUCTOS
        # ==================================================

        if productos_categoria:

            print("\n" + "=" * 70)

            print(
                " " * 10 +
                "⚠️ CATEGORÍA CON PRODUCTOS"
            )

            print("=" * 70)

            print(
                f"\nLa categoría "
                f"'{categoria.nombre}' "
                f"tiene "
                f"{len(productos_categoria)} "
                f"producto(s) asociado(s)."
            )

            # Crear tabla con los productos asociados.

            datos = []

            for producto in productos_categoria:

                datos.append({

                    "ID": producto.id_producto,

                    "PRODUCTO": producto.nombre,

                    "PRECIO": f"${producto.precio:,.0f}",

                    "STOCK": producto.stock

                })

            print("\nProductos asociados:")

            print(
                tabulate(
                    datos,
                    headers="keys",
                    tablefmt="grid",
                    showindex=False,
                    stralign="center",
                    numalign="center"
                )
            )

            print("\n" + "=" * 70)

            print(
                "¿Desea eliminar esta categoría "
                "de todas formas?"
            )

            print("\n1. Sí, eliminar")

            print("2. No, cancelar")

            opcion = input(
                "\nSeleccione una opción: "
            )

            # ==================================================
            # CONFIRMACIÓN
            # ==================================================

            if opcion == "1":

                self.cargar(
                    "Eliminando categoría"
                )

                resultado = (
                    self.controller.eliminar_categoria(
                        id_categoria,
                        productos
                    )
                )

                if resultado:

                    print(
                        "\nCategoría eliminada correctamente."
                    )

                    print(
                        "Los productos asociados también "
                        "fueron eliminados."
                    )

                else:

                    print(
                        "\nNo se pudo eliminar "
                        "la categoría."
                    )

            elif opcion == "2":

                print(
                    "\nOperación cancelada."
                )

                print(
                    "La categoría no fue eliminada."
                )

            else:

                print(
                    "\nOpción inválida."
                )

                print(
                    "La categoría no fue eliminada."
                )

        # ==================================================
        # SI NO TIENE PRODUCTOS
        # ==================================================

        else:

            print("\n" + "=" * 70)

            print(
                " " * 15 +
                "CATEGORÍA SIN PRODUCTOS"
            )

            print("=" * 70)

            print(
                f"\nLa categoría "
                f"'{categoria.nombre}' "
                f"no tiene productos asociados."
            )

            print(
                "\nEliminando categoría..."
            )

            self.esperar(1.5)

            resultado = (
                self.controller.eliminar_categoria(
                    id_categoria,
                    productos
                )
            )

            if resultado:

                print(
                    "\nCategoría eliminada correctamente."
                )

            else:

                print(
                    "\nNo se pudo eliminar "
                    "la categoría."
                )

        self.continuar()

    # ==================================================
    # MENÚ
    # ==================================================

    def menu(self):

        while True:

            print("\n" + "=" * 60)

            print(
                " " * 17 +
                "GESTIÓN DE CATEGORÍAS"
            )

            print("=" * 60)

            print("\n1. Agregar categoría")

            print("2. Listar categorías")

            print("3. Actualizar categoría")

            print("4. Eliminar categoría")

            print("5. Volver al menú principal")

            opcion = input(
                "\nSeleccione una opción: "
            )

            # ==================================================
            # AGREGAR
            # ==================================================

            if opcion == "1":

                self.cargar(
                    "Abriendo registro de categoría"
                )

                self.agregar_categoria()

            # ==================================================
            # LISTAR
            # ==================================================

            elif opcion == "2":

                self.mostrar_categorias()

                self.continuar()

            # ==================================================
            # ACTUALIZAR
            # ==================================================

            elif opcion == "3":

                self.cargar(
                    "Abriendo actualización de categoría"
                )

                self.actualizar_categoria()

            # ==================================================
            # ELIMINAR
            # ==================================================

            elif opcion == "4":

                self.cargar(
                    "Abriendo eliminación de categoría"
                )

                self.eliminar_categoria()

            # ==================================================
            # VOLVER
            # ==================================================

            elif opcion == "5":

                self.cargar(
                    "Volviendo al menú principal"
                )

                break

            # ==================================================
            # OPCIÓN INCORRECTA
            # ==================================================

            else:

                print(
                    "\nOpción inválida."
                )

                self.continuar()
