# arboles/arbol_b.py
from utils.logger_config import logger

class NodoB:
    """Clase para un nodo de un Árbol B."""
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class ArbolB:
    """Clase para el Árbol B."""
    def __init__(self, t):
        self.root = NodoB(leaf=True)
        self.t = t  # Grado mínimo
        logger.info(f"Árbol B inicializado con grado mínimo t={t}.")

    def buscar(self, k):
        """Busca una clave 'k' en el árbol."""
        nodo_actual = self.root
        while True:
            i = 0
            while i < len(nodo_actual.keys) and k > nodo_actual.keys[i]:
                i += 1
            if i < len(nodo_actual.keys) and k == nodo_actual.keys[i]:
                logger.info(f"Clave {k} encontrada.")
                print(f"🔍 Clave {k} encontrada.")
                return True, nodo_actual
            if nodo_actual.leaf:
                logger.info(f"Clave {k} no encontrada.")
                print(f"❌ Clave {k} no encontrada.")
                return False, None
            nodo_actual = nodo_actual.children[i]

    def insertar(self, k):
        """Inserta una nueva clave 'k' en el árbol."""
        root = self.root
        # Si la raíz está llena, el árbol crece en altura
        if len(root.keys) == (2 * self.t) - 1:
            new_root = NodoB()
            self.root = new_root
            new_root.children.insert(0, root)
            self._dividir_hijo(new_root, 0)
            self._insertar_no_lleno(new_root, k)
            logger.info(f"El árbol creció. Nueva raíz creada.")
        else:
            self._insertar_no_lleno(root, k)
        logger.info(f"Clave {k} insertada en el árbol B.")
        print(f"✅ Clave {k} insertada.")

    def _insertar_no_lleno(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._dividir_hijo(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insertar_no_lleno(x.children[i], k)

    def _dividir_hijo(self, x, i):
        t = self.t
        y = x.children[i]
        z = NodoB(leaf=y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t:(2*t - 1)]
        y.keys = y.keys[0:(t-1)]
        if not y.leaf:
            z.children = y.children[t:(2*t)]
            y.children = y.children[0:t]
        logger.info(f"Nodo dividido. Clave {x.keys[i]} promovida.")

    def imprimir_arbol(self):
        """Imprime el árbol para depuración."""
        print("Estructura del Árbol B:")
        self._imprimir_recursivo(self.root, "")

    def _imprimir_recursivo(self, nodo, prefijo):
        print(f"{prefijo}Keys: {nodo.keys}, Leaf: {nodo.leaf}")
        prefijo += "  "
        if not nodo.leaf:
            for hijo in nodo.children:
                self._imprimir_recursivo(hijo, prefijo)