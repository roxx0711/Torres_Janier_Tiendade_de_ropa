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

    # ==================================================
    # INICIO DEL PROGRAMA
    # ==================================================

    print("=" * 60)

    print(
        " " * 18 +
        "TIENDA DE ROPA"
    )

    print("=" * 60)

    print("\nTienda de ropa iniciando...")

    time.sleep(4)

    print("\nTienda de ropa ya operando, jefe.")

    time.sleep(5)

    # ==================================================
    # CREAR CONTROLLERS
    # ==================================================

    categoria_controller = CategoriaController()

    producto_controller = ProductoController(
        categoria_controller
    )

    # ==================================================
    # CREAR VIEWS
    # ==================================================

    # CategoriaView necesita:
    # 1. CategoriaController
    # 2. ProductoController
    #
    # Esto permite comprobar si una categoría
    # tiene productos antes de eliminarla.

    categoria_view = CategoriaView(
        categoria_controller,
        producto_controller
    )

    producto_view = ProductoView(
        producto_controller,
        categoria_controller
    )

    # ==================================================
    # CREAR MENÚ PRINCIPAL
    # ==================================================

    menu_view = MenuView(
        producto_view,
        categoria_view
    )

    # ==================================================
    # INICIAR APLICACIÓN
    # ==================================================

    menu_view.iniciar()


# ==================================================
# EJECUTAR PROGRAMA
# ==================================================

if __name__ == "__main__":

    main()