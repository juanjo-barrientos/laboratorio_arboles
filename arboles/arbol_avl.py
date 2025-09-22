# arboles/arbol_avl.py
from collections import deque
from utils.logger_config import logger

class NodoAVL:
    """Clase para un nodo de un Árbol AVL."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # La altura de un nuevo nodo es siempre 1

class ArbolAVL:
    """Clase para el Árbol AVL."""
    def __init__(self):
        self.raiz = None
        logger.info("AVL inicializado.")

    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierdo) - self._get_altura(nodo.derecho)

    def _rotacion_derecha(self, z):
        logger.info(f"Ejecutando rotación derecha en el nodo {z.valor}")
        y = z.izquierdo
        T3 = y.derecho

        # Realizar rotación
        y.derecho = z
        z.izquierdo = T3

        # Actualizar alturas
        z.altura = 1 + max(self._get_altura(z.izquierdo), self._get_altura(z.derecho))
        y.altura = 1 + max(self._get_altura(y.izquierdo), self._get_altura(y.derecho))

        return y

    def _rotacion_izquierda(self, y):
        logger.info(f"Ejecutando rotación izquierda en el nodo {y.valor}")
        x = y.derecho
        T2 = x.izquierdo

        # Realizar rotación
        x.izquierdo = y
        y.derecho = T2

        # Actualizar alturas
        y.altura = 1 + max(self._get_altura(y.izquierdo), self._get_altura(y.derecho))
        x.altura = 1 + max(self._get_altura(x.izquierdo), self._get_altura(x.derecho))

        return x

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)
        
    def _insertar_recursivo(self, raiz, valor):
        # 1. Inserción normal de BST
        if not raiz:
            logger.info(f"Nodo {valor} insertado.")
            print(f"✅ Nodo {valor} insertado.")
            return NodoAVL(valor)
        elif valor < raiz.valor:
            raiz.izquierdo = self._insertar_recursivo(raiz.izquierdo, valor)
        elif valor > raiz.valor:
            raiz.derecho = self._insertar_recursivo(raiz.derecho, valor)
        else:
            logger.warning(f"Intento de insertar valor duplicado: {valor}.")
            print(f"⚠️ El valor {valor} ya existe en el árbol.")
            return raiz

        # 2. Actualizar la altura del ancestro
        raiz.altura = 1 + max(self._get_altura(raiz.izquierdo), self._get_altura(raiz.derecho))

        # 3. Obtener el factor de balance
        balance = self._get_balance(raiz)

        # 4. Si el nodo está desbalanceado, realizar rotaciones
        # Caso Izquierda-Izquierda
        if balance > 1 and valor < raiz.izquierdo.valor:
            return self._rotacion_derecha(raiz)

        # Caso Derecha-Derecha
        if balance < -1 and valor > raiz.derecho.valor:
            return self._rotacion_izquierda(raiz)

        # Caso Izquierda-Derecha
        if balance > 1 and valor > raiz.izquierdo.valor:
            raiz.izquierdo = self._rotacion_izquierda(raiz.izquierdo)
            return self._rotacion_derecha(raiz)

        # Caso Derecha-Izquierda
        if balance < -1 and valor < raiz.derecho.valor:
            raiz.derecho = self._rotacion_derecha(raiz.derecho)
            return self._rotacion_izquierda(raiz)

        return raiz

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if not nodo_actual:
            logger.info(f"Valor {valor} no encontrado en el árbol.")
            print(f"❌ Valor {valor} no encontrado.")
            return False
        
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.derecho, valor)
        else:
            logger.info(f"Valor {valor} encontrado en el árbol.")
            print(f"🔍 Valor {valor} encontrado.")
            return True

    # Los métodos de recorrido (inorden, preorden, postorden, bfs) son idénticos a los del BST
    # y pueden ser copiados aquí o heredados si se refactoriza a una clase base.
    # Por simplicidad, los replicamos aquí.
    
    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def bfs(self):
        if not self.raiz: return []
        resultado, cola = [], deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izquierdo: cola.append(nodo.izquierdo)
            if nodo.derecho: cola.append(nodo.derecho)
        return resultado