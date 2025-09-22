Claro, aquí tienes un `README.md` completo que sirve tanto como documentación del proyecto como informe de laboratorio. Es detallado, explica el funcionamiento y guía al usuario desde la instalación hasta el uso.

-----

# Laboratorio de Implementación y Visualización de Árboles

**Autor:** Juan José Barrientos Salazar
**Fecha:** 21 de septiembre de 2025
**Curso:** Estructuras de Datos

## 1\. Introducción y Objetivo

Este proyecto consiste en el desarrollo de un script en Python para la implementación, manejo y visualización de diversas estructuras de datos de tipo árbol. El objetivo principal es ofrecer una herramienta interactiva y verificable que permita a los usuarios experimentar con diferentes tipos de árboles y sus algoritmos de búsqueda, facilitando así un análisis claro y una comprensión profunda de su funcionamiento interno.

El script está diseñado de manera modular, encapsulando cada tipo de árbol en su propia clase y proporcionando una interfaz de línea de comandos (CLI) para interactuar con ellos. Además, se integra con la biblioteca `Graphviz` para generar representaciones gráficas de las estructuras, y cuenta con un sistema de logging para registrar las operaciones y pruebas unitarias para garantizar la fiabilidad del código.

-----

## 2\. Estructura del Proyecto

El proyecto está organizado en una estructura de directorios modular para promover la claridad y la mantenibilidad del código:

```
/laboratorio_arboles/
|
|-- logs/
|   |-- operations.log          # Archivo de registro de todas las operaciones
|
|-- arboles/
|   |-- __init__.py
|   |-- arbol_b.py              # Implementación del Árbol B
|   |-- arbol_binario.py        # Implementación del Árbol Binario de Búsqueda (BST)
|   |-- arbol_avl.py            # Implementación del Árbol AVL (Autobalanceado)
|   |-- arbol_n_ario.py         # Implementación del Árbol N-ario
|   |-- arbol_trie.py           # Implementación del Árbol Trie (para cadenas)
|
|-- utils/
|   |-- __init__.py
|   |-- visualizador.py         # Módulo para generar las visualizaciones con Graphviz
|   |-- logger_config.py        # Módulo para la configuración del logger
|
|-- main.py                     # Script principal con el menú interactivo
|-- tests.py                    # Pruebas unitarias para validar las implementaciones
|-- requirements.txt            # Dependencias de Python del proyecto
|-- README.md                   # Este archivo
```

-----

## 3\. Conceptos Teóricos y Estructuras Implementadas

### 3.1. Tipos de Árboles

  * **Árbol Binario de Búsqueda (BST):** Un árbol donde cada nodo tiene como máximo dos hijos. El valor del nodo izquierdo es menor que el del padre, y el valor del nodo derecho es mayor. Ofrece búsquedas, inserciones y eliminaciones eficientes ($O(\\log n)$ en el caso promedio).
  * **Árbol AVL:** Un BST autobalanceado. Mantiene su altura lo más pequeña posible mediante "rotaciones" después de cada inserción o eliminación, garantizando que el factor de equilibrio de cada nodo sea -1, 0 o 1. Esto asegura un rendimiento de $O(\\log n)$ incluso en el peor de los casos.
  * **Árbol B:** Un árbol de búsqueda auto-balanceado optimizado para sistemas que leen y escriben grandes bloques de datos, como bases de datos y sistemas de archivos. Cada nodo puede tener más de dos hijos y contener múltiples claves, lo que reduce la altura del árbol y el número de accesos a disco.
  * **Árbol Trie (Árbol de Prefijos):** Una estructura de datos de árbol utilizada para almacenar un conjunto de cadenas. Cada nodo representa un carácter, y los caminos desde la raíz hasta los nodos marcados representan palabras completas. Es extremadamente eficiente para búsquedas de prefijos y autocompletado.
  * **Árbol N-ario:** Un árbol generalista donde un nodo puede tener un número arbitrario de hijos. Es una estructura flexible utilizada para representar jerarquías como sistemas de archivos o estructuras organizacionales.

### 3.2. Métodos de Búsqueda (Recorridos)

  * **Búsqueda en Profundidad (DFS - Depth First Search):** Explora tan profundo como sea posible a lo largo de cada rama antes de retroceder.
      * **Preorden:** Visita la raíz, luego el subárbol izquierdo, y finalmente el subárbol derecho.
      * **Inorden:** Visita el subárbol izquierdo, luego la raíz, y finalmente el subárbol derecho. En un BST, este recorrido devuelve los elementos ordenados.
      * **Postorden:** Visita el subárbol izquierdo, luego el subárbol derecho, y finalmente la raíz.
  * **Búsqueda en Anchura (BFS - Breadth First Search):** Explora todos los nodos de un nivel antes de pasar al siguiente. Se implementa típicamente con una cola y es útil para encontrar el camino más corto en árboles no ponderados.

-----

## 4\. Guía de Instalación y Puesta en Marcha

Para ejecutar este proyecto, sigue los siguientes pasos:

### 4.1. Prerrequisitos

  * **Python 3.8** o superior.
  * **Git** (para clonar el repositorio).

### 4.2. Instalación del Software Graphviz

Este programa es **esencial** para la visualización de los árboles.

1.  **Descarga:** Ve a la [página oficial de Graphviz](https://graphviz.org/download/) y descarga el instalador para tu sistema operativo (Windows, macOS o Linux).
2.  **Instala:** Ejecuta el instalador.
3.  **Añadir al PATH:** Durante la instalación, **asegúrate de marcar la casilla que añade Graphviz al PATH del sistema**. Si omites este paso, el script no podrá generar las imágenes.

### 4.3. Configuración del Entorno de Python

Se recomienda encarecidamente utilizar un entorno virtual para aislar las dependencias del proyecto.

1.  **Clona el repositorio (si aplica) o descomprime los archivos del proyecto.**

    ```bash
    git clone https://github.com/juanjo-barrientos/laboratorio_arboles
    cd proyecto_arboles
    ```

2.  **Crea un entorno virtual.**

    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual.**

      * En **Windows**: `venv\Scripts\activate`
      * En **macOS/Linux**: `source venv/bin/activate`

4.  **Instala las dependencias de Python.**
    Crea un archivo llamado `requirements.txt` con el siguiente contenido:

    ```txt
    # requirements.txt
    graphviz==0.20.1 
    ```

    Luego, ejecuta el siguiente comando en tu terminal:

    ```bash
    pip install -r requirements.txt
    ```

-----

## 5\. Cómo Ejecutar la Aplicación

Una vez que el entorno esté configurado, puedes iniciar el programa.

1.  Asegúrate de que tu entorno virtual esté activado.

2.  Desde el directorio raíz del proyecto (`laboratorio_arboles/`), ejecuta el script principal:

    ```bash
    python main.py
    ```

3.  Aparecerá un menú interactivo en la terminal. Sigue las instrucciones para seleccionar un tipo de árbol y realizar operaciones como insertar, buscar y visualizar.

-----

## 6\. Funcionalidades del Script

  * **Menú Interactivo:** Permite una navegación sencilla entre los diferentes tipos de árboles y sus funcionalidades.
  * **Operaciones CRUD:** Cada árbol soporta operaciones de inserción y búsqueda. La eliminación se omite en algunos árboles complejos por simplicidad, pero la estructura está preparada para ello.
  * **Visualización Gráfica:** Al seleccionar la opción de visualizar, el script genera un archivo de imagen `.png` en la carpeta `output/` y lo abre automáticamente, mostrando la estructura actual del árbol.
  * **Logging de Operaciones:** Todas las acciones importantes (creación de árboles, inserciones, búsquedas) se registran en `logs/operations.log` con una marca de tiempo, lo que permite auditar y depurar el comportamiento del programa.
  * **Verificación y Manejo de Errores:** El sistema proporciona mensajes claros al usuario, confirmando operaciones exitosas y notificando errores (ej. insertar un valor duplicado, buscar un nodo inexistente).

-----

## 7\. Pruebas Unitarias

Para garantizar que todas las estructuras de datos y algoritmos funcionen correctamente, se ha incluido un conjunto de pruebas unitarias.

Para ejecutar las pruebas:

1.  Asegúrate de que el entorno virtual esté activado.

2.  Desde el directorio raíz, ejecuta el siguiente comando:

    ```bash
    python tests.py
    ```

3.  La salida mostrará los resultados de todas las pruebas, indicando si cada funcionalidad pasa la verificación.

-----

## 8\. Conclusión

Este laboratorio ha permitido aplicar de manera práctica los conceptos teóricos de las estructuras de datos de árboles. La implementación modular y las pruebas unitarias aseguran un código robusto y fácil de extender, mientras que la visualización gráfica y la interfaz interactiva lo convierten en una valiosa herramienta de aprendizaje.

### 8.1. Posibles Mejoras Futuras

  * **Implementación de la operación de `eliminar`** en todos los árboles (especialmente en AVL y Árbol B, que son más complejos).
  * Desarrollo de una **interfaz gráfica de usuario (GUI)** con Tkinter o PyQt para una experiencia más amigable.
  * Añadir la funcionalidad de **exportar e importar árboles** en un formato estándar como JSON para persistir los datos.
  * Mejorar el visualizador para manejar de forma más elegante los Árboles B y Tries.
