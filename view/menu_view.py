# VIEW
# Vista principal de la aplicación.

import time


class MenuView:

    def __init__(self, producto_view, categoria_view):

        self.producto_view = producto_view
        self.categoria_view = categoria_view

    def esperar(self, segundos=1.5):

        time.sleep(segundos)

    def cargar(self, mensaje="Procesando"):

        print(f"\n{mensaje}...")

        self.esperar(1.5)

    def iniciar(self):

        while True:

            print("\n" + "=" * 60)
            print("                    TIENDA DE ROPA")
            print("=" * 60)

            print("\n1. Gestionar productos")
            print("2. Gestionar categorías")
            print("3. Realizar compra")
            print("4. Salir")

            opcion = input("\nSeleccione una opción: ")

            # -----------------------------------------
            # PRODUCTOS
            # -----------------------------------------

            if opcion == "1":

                self.cargar("Abriendo gestión de productos")

                self.producto_view.menu()

            # -----------------------------------------
            # CATEGORÍAS
            # -----------------------------------------

            elif opcion == "2":

                self.cargar("Abriendo gestión de categorías")

                self.categoria_view.menu()

            # -----------------------------------------
            # COMPRA
            # -----------------------------------------

            elif opcion == "3":

                self.cargar("Preparando sistema de compra")

                self.producto_view.realizar_compra()

                input("\nPresione ENTER para volver al menú principal...")

            # -----------------------------------------
            # SALIR
            # -----------------------------------------

            elif opcion == "4":

                self.cargar("Cerrando Tienda de Ropa")

                print("\nGracias por utilizar el sistema.")

                self.esperar(2)

                break

            else:

                print("\nOpción inválida.")

                self.esperar(1.5)