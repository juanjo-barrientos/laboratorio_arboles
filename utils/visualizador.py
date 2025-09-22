# utils/visualizador.py
from graphviz import Digraph
import os

def visualizar_arbol(nodo_raiz, nombre_archivo="arbol"):
    """
    Genera una visualización de un árbol y la guarda como un archivo de imagen.
    Funciona con BST, AVL, y N-ario. Otros árboles requieren adaptadores.
    """
    if not nodo_raiz:
        print("El árbol está vacío. No se puede visualizar.")
        return

    dot = Digraph(comment='Visualización del Árbol')
    dot.attr('node', shape='circle', style='filled', fillcolor='skyblue')

    def agregar_nodos_y_aristas(nodo):
        if nodo is None:
            return
        
        # Nodo para BST/AVL/N-ario
        if hasattr(nodo, 'valor'):
            dot.node(str(id(nodo)), str(nodo.valor))
            if hasattr(nodo, 'izquierdo') and nodo.izquierdo:
                dot.edge(str(id(nodo)), str(id(nodo.izquierdo)))
                agregar_nodos_y_aristas(nodo.izquierdo)
            if hasattr(nodo, 'derecho') and nodo.derecho:
                dot.edge(str(id(nodo)), str(id(nodo.derecho)))
                agregar_nodos_y_aristas(nodo.derecho)
            if hasattr(nodo, 'hijos'): # Para N-ario
                for hijo in nodo.hijos:
                    dot.edge(str(id(nodo)), str(id(hijo)))
                    agregar_nodos_y_aristas(hijo)
    
    agregar_nodos_y_aristas(nodo_raiz)
    
    # Renderizar el gráfico
    try:
        # Crea la carpeta de salida si no existe
        if not os.path.exists('output'):
            os.makedirs('output')
        ruta_completa = os.path.join('output', nombre_archivo)
        dot.render(ruta_completa, format='png', view=True)
        print(f"Árbol visualizado y guardado en 'output/{nombre_archivo}.png'")
    except Exception as e:
        print(f"Error al visualizar el árbol. Asegúrate de que Graphviz esté instalado y en el PATH del sistema.")
        print(f"Detalle del error: {e}")