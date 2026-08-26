# Janier Torres Riascos - Tema 8 - Tienda de ropa

# MAIN
# Punto de entrada de la aplicación.

import time

from controller.categoria_controller import CategoriaController
from controller.producto_controller import ProductoController

from view.categoria_view import CategoriaView
from view.producto_view import ProductoView
from view.menu_view import MenuView


def main():

    print("=" * 60)
    print("                  TIENDA DE ROPA")
    print("=" * 60)

    print("\nTienda de ropa iniciando...")

    time.sleep(4)

    print("\nTienda de ropa ya operando, jefe.")

    time.sleep(5)

    # Crear Controllers
    categoria_controller = CategoriaController()

    producto_controller = ProductoController(
        categoria_controller
    )

    # Crear Views
    categoria_view = CategoriaView(
        categoria_controller
    )

    producto_view = ProductoView(
        producto_controller,
        categoria_controller
    )

    menu_view = MenuView(
        producto_view,
        categoria_view
    )

    # Iniciar programa
    menu_view.iniciar()


if __name__ == "__main__":
    main()