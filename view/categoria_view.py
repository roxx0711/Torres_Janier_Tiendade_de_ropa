# VIEW
# Vista encargada de gestionar las categorías mediante consola.

import pandas as pd
import time


class CategoriaView:

    def __init__(self, controller):

        self.controller = controller

    # -----------------------------------------
    # PAUSAS
    # -----------------------------------------

    def esperar(self, segundos=1.5):

        time.sleep(segundos)

    def cargar(self, mensaje):

        print(f"\n{mensaje}...")

        self.esperar(1.5)

    def continuar(self):

        input("\nPresione ENTER para continuar...")

    # -----------------------------------------
    # LISTAR
    # -----------------------------------------

    def mostrar_categorias(self):

        self.cargar("Cargando categorías")

        categorias = self.controller.listar_categorias()

        if not categorias:

            print("\nNo existen categorías registradas.")

            self.continuar()

            return

        datos = []

        for categoria in categorias:

            datos.append({
                "ID": categoria.id_categoria,
                "NOMBRE": categoria.nombre,
                "DESCRIPCIÓN": categoria.descripcion
            })

        tabla = pd.DataFrame(datos)

        print("\n" + "=" * 70)
        print("                         CATEGORÍAS")
        print("=" * 70)

        print(tabla.to_string(index=False))

        print("=" * 70)

        self.continuar()

    # -----------------------------------------
    # AGREGAR
    # -----------------------------------------

    def agregar_categoria(self):

        print("\n" + "=" * 50)
        print("              AGREGAR CATEGORÍA")
        print("=" * 50)

        nombre = input("\nIngrese el nombre de la categoría: ")

        descripcion = input(
            "Ingrese la descripción: "
        )

        self.cargar("Registrando categoría")

        categoria = self.controller.agregar_categoria(
            nombre,
            descripcion
        )

        print("\nCategoría agregada correctamente.")

        print(
            f"ID asignado: {categoria.id_categoria}"
        )

        self.continuar()

    # -----------------------------------------
    # ACTUALIZAR
    # -----------------------------------------

    def actualizar_categoria(self):

        self.mostrar_categorias()

        try:

            id_categoria = int(
                input(
                    "\nIngrese el ID de la categoría "
                    "a actualizar: "
                )
            )

        except ValueError:

            print("\nDebe ingresar un número válido.")

            self.continuar()

            return

        categoria = self.controller.buscar_categoria(
            id_categoria
        )

        if categoria is None:

            print("\nLa categoría no existe.")

            self.continuar()

            return

        nombre = input("\nNuevo nombre: ")

        descripcion = input(
            "Nueva descripción: "
        )

        self.cargar("Actualizando categoría")

        resultado = self.controller.actualizar_categoria(
            id_categoria,
            nombre,
            descripcion
        )

        if resultado:

            print(
                "\nCategoría actualizada correctamente."
            )

        self.continuar()

    # -----------------------------------------
    # ELIMINAR
    # -----------------------------------------

    def eliminar_categoria(self):

        self.mostrar_categorias()

        try:

            id_categoria = int(
                input(
                    "\nIngrese el ID de la categoría "
                    "a eliminar: "
                )
            )

        except ValueError:

            print("\nDebe ingresar un número válido.")

            self.continuar()

            return

        self.cargar("Eliminando categoría")

        resultado = self.controller.eliminar_categoria(
            id_categoria
        )

        if resultado:

            print(
                "\nCategoría eliminada correctamente."
            )

        else:

            print(
                "\nLa categoría no existe."
            )

        self.continuar()

    # -----------------------------------------
    # MENÚ
    # -----------------------------------------

    def menu(self):

        while True:

            print("\n" + "=" * 55)
            print("             GESTIÓN DE CATEGORÍAS")
            print("=" * 55)

            print("\n1. Agregar categoría")
            print("2. Listar categorías")
            print("3. Actualizar categoría")
            print("4. Eliminar categoría")
            print("5. Volver al menú principal")

            opcion = input(
                "\nSeleccione una opción: "
            )

            if opcion == "1":

                self.agregar_categoria()

            elif opcion == "2":

                self.mostrar_categorias()

            elif opcion == "3":

                self.actualizar_categoria()

            elif opcion == "4":

                self.eliminar_categoria()

            elif opcion == "5":

                self.cargar(
                    "Volviendo al menú principal"
                )

                break

            else:

                print("\nOpción inválida.")

                self.continuar()