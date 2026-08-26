# VIEW
# Vista encargada de interactuar con el usuario
# para gestionar productos mediante consola.

import pandas as pd
import time


class ProductoView:

    def __init__(self, controller, categoria_controller):
        self.controller = controller
        self.categoria_controller = categoria_controller

    # ==================================================
    # FUNCIONES DE ESPERA
    # ==================================================

    def esperar(self, segundos=1.5):
        time.sleep(segundos)

    def cargar(self, mensaje):
        print(f"\n{mensaje}...")
        self.esperar(1.5)

    def continuar(self):
        input("\nPresione ENTER para continuar...")

    # ==================================================
    # MOSTRAR PRODUCTOS
    # ==================================================

    def mostrar_productos(self):

        self.cargar("Cargando productos")

        productos = self.controller.listar_productos()

        if not productos:
            print("\nNo existen productos registrados.")
            return False

        datos = []

        for producto in productos:

            nombre_categoria = (
                self.controller.obtener_nombre_categoria(
                    producto.id_categoria
                )
            )

            datos.append({
                "ID": producto.id_producto,
                "NOMBRE": producto.nombre,
                "PRECIO": f"${producto.precio:,.0f}",
                "STOCK": producto.stock,
                "CATEGORÍA": nombre_categoria
            })

        tabla = pd.DataFrame(datos)

        print("\n" + "=" * 90)
        print("                         PRODUCTOS")
        print("=" * 90)

        print(
            tabla.to_string(
                index=False,
                justify="center",
                col_space=14
            )
        )

        print("=" * 90)

        return True

    # ==================================================
    # MOSTRAR CATEGORÍAS DISPONIBLES
    # ==================================================

    def mostrar_categorias_disponibles(self):

        self.cargar("Cargando categorías disponibles")

        categorias = (
            self.categoria_controller.listar_categorias()
        )

        if not categorias:

            print("\nNo existen categorías.")
            print("Primero debe crear una categoría.")

            return False

        datos = []

        for categoria in categorias:

            datos.append({
                "ID": categoria.id_categoria,
                "NOMBRE": categoria.nombre,
                "DESCRIPCIÓN": categoria.descripcion
            })

        tabla = pd.DataFrame(datos)

        print("\n" + "=" * 75)
        print("                    CATEGORÍAS DISPONIBLES")
        print("=" * 75)

        print(
            tabla.to_string(
                index=False,
                justify="center",
                col_space=18
            )
        )

        print("=" * 75)

        return True

    # ==================================================
    # AGREGAR PRODUCTO
    # ==================================================

    def agregar_producto(self):

        print("\n" + "=" * 60)
        print("                    AGREGAR PRODUCTO")
        print("=" * 60)

        if not self.mostrar_categorias_disponibles():

            self.continuar()
            return

        nombre = input("\nNombre del producto: ")

        if not nombre.strip():

            print(
                "\nEl nombre del producto "
                "no puede estar vacío."
            )

            self.continuar()
            return

        try:

            precio = float(
                input("Precio del producto: ")
            )

            stock = int(
                input("Stock disponible: ")
            )

            id_categoria = int(
                input("ID de la categoría: ")
            )

        except ValueError:

            print(
                "\nIngrese valores numéricos válidos."
            )

            self.continuar()
            return

        if precio <= 0:

            print(
                "\nEl precio debe ser mayor que 0."
            )

            self.continuar()
            return

        if stock < 0:

            print(
                "\nEl stock no puede ser negativo."
            )

            self.continuar()
            return

        self.cargar("Registrando producto")

        producto = (
            self.controller.agregar_producto(
                nombre,
                precio,
                stock,
                id_categoria
            )
        )

        if producto is None:

            print("\nERROR:")
            print("La categoría indicada no existe.")
            print("El producto no puede ser agregado.")

        else:

            print(
                "\nProducto agregado correctamente."
            )

            print(
                f"ID asignado: "
                f"{producto.id_producto}"
            )

        self.continuar()

    # ==================================================
    # ACTUALIZAR PRODUCTO
    # ==================================================

    def actualizar_producto(self):

        productos_existen = self.mostrar_productos()

        if not productos_existen:

            self.continuar()
            return

        try:

            id_producto = int(
                input("\nIngrese el ID del producto: ")
            )

        except ValueError:

            print(
                "\nDebe ingresar un número válido."
            )

            self.continuar()
            return

        producto = (
            self.controller.buscar_producto(
                id_producto
            )
        )

        if producto is None:

            print("\nEl producto no existe.")

            self.continuar()
            return

        if not self.mostrar_categorias_disponibles():

            self.continuar()
            return

        nombre = input("\nNuevo nombre: ")

        if not nombre.strip():

            print(
                "\nEl nombre no puede estar vacío."
            )

            self.continuar()
            return

        try:

            precio = float(
                input("Nuevo precio: ")
            )

            stock = int(
                input("Nuevo stock: ")
            )

            id_categoria = int(
                input("Nuevo ID de categoría: ")
            )

        except ValueError:

            print(
                "\nIngrese valores numéricos válidos."
            )

            self.continuar()
            return

        if precio <= 0:

            print(
                "\nEl precio debe ser mayor que 0."
            )

            self.continuar()
            return

        if stock < 0:

            print(
                "\nEl stock no puede ser negativo."
            )

            self.continuar()
            return

        self.cargar("Actualizando producto")

        resultado = (
            self.controller.actualizar_producto(
                id_producto,
                nombre,
                precio,
                stock,
                id_categoria
            )
        )

        if resultado:

            print(
                "\nProducto actualizado correctamente."
            )

        else:

            print(
                "\nNo se pudo actualizar el producto."
            )

            print(
                "Compruebe que la categoría exista."
            )

        self.continuar()

    # ==================================================
    # ELIMINAR PRODUCTO
    # ==================================================

    def eliminar_producto(self):

        productos_existen = self.mostrar_productos()

        if not productos_existen:

            self.continuar()
            return

        try:

            id_producto = int(
                input(
                    "\nIngrese el ID del producto "
                    "a eliminar: "
                )
            )

        except ValueError:

            print(
                "\nDebe ingresar un número válido."
            )

            self.continuar()
            return

        self.cargar("Eliminando producto")

        resultado = (
            self.controller.eliminar_producto(
                id_producto
            )
        )

        if resultado:

            print(
                "\nProducto eliminado correctamente."
            )

        else:

            print(
                "\nEl producto no existe."
            )

        self.continuar()

    # ==================================================
    # REALIZAR COMPRA
    # ==================================================

    def realizar_compra(self):

        productos_existen = self.mostrar_productos()

        if not productos_existen:

            self.continuar()
            return

        # ==================================================
        # SELECCIONAR PRODUCTO
        # ==================================================

        try:

            id_producto = int(
                input(
                    "\nIngrese el ID del producto "
                    "que desea comprar: "
                )
            )

        except ValueError:

            print(
                "\nDebe ingresar un número válido."
            )

            self.continuar()
            return

        producto = (
            self.controller.buscar_producto(
                id_producto
            )
        )

        if producto is None:

            print("\nEl producto no existe.")

            self.continuar()
            return

        # ==================================================
        # COMPROBAR STOCK
        # ==================================================

        if producto.stock <= 0:

            print(
                "\nEste producto no tiene "
                "stock disponible."
            )

            self.continuar()
            return

        # ==================================================
        # TIPO DE PERSONA
        # ==================================================

        print("\n" + "=" * 60)
        print("                    TIPO DE PERSONA")
        print("=" * 60)

        print("\n1. Estudiante")
        print("2. Profesor")

        tipo = input(
            "\nSeleccione una opción: "
        )

        # ==================================================
        # ESTUDIANTE
        # ==================================================

        if tipo == "1":

            tipo_persona = "estudiante"
            nombre_profesor = ""

        # ==================================================
        # PROFESOR
        # ==================================================

        elif tipo == "2":

            tipo_persona = "profesor"

            nombre_profesor = input(
                "\nIngrese el nombre del profesor: "
            ).strip()

            if not nombre_profesor:

                print(
                    "\nEl nombre del profesor "
                    "no puede estar vacío."
                )

                self.continuar()
                return

            # ==================================================
            # CONFIRMAR PROFESOR PAULO TAYPE
            # ==================================================

            print("\n" + "=" * 60)
            print("              CONFIRMACIÓN DE PROFESOR")
            print("=" * 60)

            print(
                "\n¿Es el profesor Paulo Taype?"
            )

            print("\n1. Sí")
            print("2. No")

            confirmacion = input(
                "\nSeleccione una opción: "
            )

            if confirmacion == "1":

                # Se establece el nombre exacto
                # para aplicar el 80%.
                nombre_profesor = "Paulo Taype"

            elif confirmacion == "2":

                # Se mantiene el nombre ingresado.
                # Recibirá el 30%.
                pass

            else:

                print(
                    "\nOpción inválida."
                )

                self.continuar()
                return

        # ==================================================
        # OPCIÓN INVÁLIDA
        # ==================================================

        else:

            print(
                "\nOpción inválida."
            )

            self.continuar()
            return

        # ==================================================
        # CALCULAR DESCUENTO
        # ==================================================

        self.cargar(
            "Calculando descuento"
        )

        (
            descuento,
            valor_descuento,
            precio_final
        ) = self.controller.calcular_descuento(
            producto.precio,
            tipo_persona,
            nombre_profesor
        )

        # ==================================================
        # ACTUALIZAR STOCK
        # ==================================================

        producto.stock -= 1

        # ==================================================
        # IDENTIFICAR TIPO DE PERSONA
        # ==================================================

        if tipo_persona == "estudiante":

            tipo_mostrar = "Estudiante"

        elif (
            tipo_persona == "profesor"
            and nombre_profesor.strip().lower()
            == "paulo taype"
        ):

            tipo_mostrar = "Profesor Paulo Taype"

        else:

            tipo_mostrar = "Otro profesor"

        # ==================================================
        # CREAR TABLA DE COMPRA
        # ==================================================

        datos = [{
            "PRODUCTO": producto.nombre,
            "PRECIO": f"${producto.precio:,.0f}",
            "TIPO": tipo_mostrar,
            "DESCUENTO": f"{descuento * 100:.0f}%",
            "DESC. $": f"${valor_descuento:,.0f}",
            "TOTAL": f"${precio_final:,.0f}"
        }]

        tabla = pd.DataFrame(datos)

        # ==================================================
        # MOSTRAR RESUMEN
        # ==================================================

        print("\n" + "=" * 90)
        print("                    RESUMEN DE COMPRA")
        print("=" * 90)

        print(
            tabla.to_string(
                index=False,
                justify="center",
                col_space=14
            )
        )

        print("=" * 90)

        print(
            "\nCompra realizada correctamente."
        )

        print(
            f"Stock restante: "
            f"{producto.stock}"
        )

        self.continuar()

    # ==================================================
    # MENÚ DE PRODUCTOS
    # ==================================================

    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("                    GESTIÓN DE PRODUCTOS")
            print("=" * 60)

            print("\n1. Agregar producto")
            print("2. Listar productos")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Realizar compra")
            print("6. Volver al menú principal")

            opcion = input(
                "\nSeleccione una opción: "
            )

            # ==================================================
            # AGREGAR
            # ==================================================

            if opcion == "1":

                self.cargar(
                    "Abriendo registro de producto"
                )

                self.agregar_producto()

            # ==================================================
            # LISTAR
            # ==================================================

            elif opcion == "2":

                self.mostrar_productos()
                self.continuar()

            # ==================================================
            # ACTUALIZAR
            # ==================================================

            elif opcion == "3":

                self.cargar(
                    "Abriendo actualización de producto"
                )

                self.actualizar_producto()

            # ==================================================
            # ELIMINAR
            # ==================================================

            elif opcion == "4":

                self.cargar(
                    "Abriendo eliminación de producto"
                )

                self.eliminar_producto()

            # ==================================================
            # COMPRA
            # ==================================================

            elif opcion == "5":

                self.cargar(
                    "Preparando sistema de compra"
                )

                self.realizar_compra()

            # ==================================================
            # VOLVER
            # ==================================================

            elif opcion == "6":

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