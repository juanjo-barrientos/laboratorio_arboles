# main.py
import os
# Importaciones de árboles
from arboles.arbol_binario import ArbolBinarioBusqueda
from arboles.arbol_avl import ArbolAVL
from arboles.arbol_b import ArbolB
from arboles.arbol_trie import Trie
from arboles.arbol_n_ario import ArbolNario
# Importaciones de utilidades
from utils.visualizador import visualizar_arbol
from utils.logger_config import logger

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione Enter para continuar...")

# --- Menús para cada tipo de árbol ---

def menu_bst():
    arbol = ArbolBinarioBusqueda()
    # (El código de este menú ya lo tienes)
    # ...
    pass # Reemplaza 'pass' con el código del menú BST de la respuesta anterior

def menu_avl():
    arbol = ArbolAVL()
    while True:
        print("\n--- Menú Árbol AVL ---")
        print("1. Insertar nodo")
        print("2. Buscar nodo")
        print("3. Visualizar árbol")
        print("4. Recorrido Inorden")
        print("5. Recorrido BFS")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            try:
                valor = int(input("Ingrese el valor a insertar: "))
                arbol.insertar(valor)
                visualizar_arbol(arbol.raiz, "avl")
            except ValueError: print("❌ Error: Ingrese un número entero.")
        elif opcion == '2':
            try:
                valor = int(input("Ingrese el valor a buscar: "))
                arbol.buscar(valor)
            except ValueError: print("❌ Error: Ingrese un número entero.")
        elif opcion == '3':
            visualizar_arbol(arbol.raiz, "avl")
        elif opcion == '4':
            print("Recorrido Inorden:", arbol.inorden())
        elif opcion == '5':
            print("Recorrido BFS:", arbol.bfs())
        elif opcion == '6': break
        else: print("Opción no válida.")
        pausar()
        limpiar_pantalla()

def menu_b():
    try:
        t = int(input("Ingrese el grado mínimo (t >= 2) para el Árbol B: "))
        if t < 2: raise ValueError
    except ValueError:
        print("Grado inválido. Usando t=3 por defecto.")
        t = 3
    arbol = ArbolB(t)
    while True:
        print(f"\n--- Menú Árbol B (Grado t={t}) ---")
        print("1. Insertar clave")
        print("2. Buscar clave")
        print("3. Imprimir estructura (consola)")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            try:
                valor = int(input("Ingrese la clave a insertar: "))
                arbol.insertar(valor)
            except ValueError: print("❌ Error: Ingrese un número entero.")
        elif opcion == '2':
            try:
                valor = int(input("Ingrese la clave a buscar: "))
                arbol.buscar(valor)
            except ValueError: print("❌ Error: Ingrese un número entero.")
        elif opcion == '3':
            arbol.imprimir_arbol()
        elif opcion == '4': break
        else: print("Opción no válida.")
        pausar()
        limpiar_pantalla()

def menu_trie():
    arbol = Trie()
    while True:
        print("\n--- Menú Árbol Trie ---")
        print("1. Insertar palabra")
        print("2. Buscar palabra completa")
        print("3. Buscar por prefijo")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            palabra = input("Ingrese la palabra a insertar (en minúsculas): ").lower()
            if palabra: arbol.insertar(palabra)
        elif opcion == '2':
            palabra = input("Ingrese la palabra a buscar: ").lower()
            if palabra: arbol.buscar(palabra)
        elif opcion == '3':
            prefijo = input("Ingrese el prefijo a buscar: ").lower()
            if prefijo: arbol.empieza_con(prefijo)
        elif opcion == '4': break
        else: print("Opción no válida.")
        pausar()
        limpiar_pantalla()

def menu_n_ario():
    try:
        valor_raiz = input("Ingrese el valor para el nodo raíz: ")
        arbol = ArbolNario(valor_raiz)
    except Exception:
        print("Valor inválido. Creando raíz con 'A'.")
        arbol = ArbolNario("A")

    while True:
        print("\n--- Menú Árbol N-ario ---")
        print("1. Insertar nodo")
        print("2. Buscar nodo")
        print("3. Visualizar árbol")
        print("4. Recorrido BFS")
        print("5. Recorrido DFS (Preorden)")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            padre = input("Ingrese el valor del nodo padre: ")
            nuevo = input("Ingrese el valor del nuevo nodo: ")
            arbol.insertar(nuevo, padre)
        elif opcion == '2':
            valor = input("Ingrese el valor a buscar: ")
            if arbol.buscar_nodo(valor): print(f"🔍 Nodo '{valor}' encontrado.")
            else: print(f"❌ Nodo '{valor}' no encontrado.")
        elif opcion == '3':
            visualizar_arbol(arbol.raiz, "n_ario")
        elif opcion == '4':
            print("Recorrido BFS:", arbol.bfs())
        elif opcion == '5':
            print("Recorrido DFS:", arbol.dfs_preorden())
        elif opcion == '6': break
        else: print("Opción no válida.")
        pausar()
        limpiar_pantalla()

# --- Menú Principal ---

def main_menu():
    while True:
        limpiar_pantalla()
        print("--- Implementación y Visualización de Árboles ---")
        print("1. Árbol Binario de Búsqueda (BST)")
        print("2. Árbol AVL")
        print("3. Árbol B")
        print("4. Árbol Trie")
        print("5. Árbol N-ario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1': menu_bst()
        elif opcion == '2': menu_avl()
        elif opcion == '3': menu_b()
        elif opcion == '4': menu_trie()
        elif opcion == '5': menu_n_ario()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            logger.info("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
            pausar()

if __name__ == "__main__":
    # Reemplaza el contenido del menú BST aquí
    def menu_bst():
        arbol = ArbolBinarioBusqueda()
        while True:
            print("\n--- Menú Árbol Binario de Búsqueda (BST) ---")
            print("1. Insertar nodo")
            print("2. Buscar nodo")
            print("3. Visualizar árbol")
            print("4. Recorrido Inorden (DFS)")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                try:
                    valor = int(input("Ingrese el valor a insertar: "))
                    arbol.insertar(valor)
                except ValueError: print("❌ Error: Ingrese un número entero.")
            elif opcion == '2':
                try:
                    valor = int(input("Ingrese el valor a buscar: "))
                    arbol.buscar(valor)
                except ValueError: print("❌ Error: Ingrese un número entero.")
            elif opcion == '3':
                visualizar_arbol(arbol.raiz, "bst")
            elif opcion == '4':
                print("Recorrido Inorden:", arbol.inorden())
            elif opcion == '5': break
            else: print("Opción no válida.")
            pausar()
            limpiar_pantalla()
    main_menu()