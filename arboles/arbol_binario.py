# arboles/arbol_binario.py
from collections import deque
from utils.logger_config import logger

class NodoBST:
    """Clase para un nodo de un Árbol Binario de Búsqueda."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    """Clase para el Árbol Binario de Búsqueda (BST)."""
    def __init__(self):
        self.raiz = None
        logger.info("BST inicializado.")

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoBST(valor)
            logger.info(f"Nodo {valor} insertado como raíz.")
            print(f"✅ Nodo {valor} insertado como raíz.")
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoBST(valor)
                logger.info(f"Nodo {valor} insertado a la izquierda de {nodo_actual.valor}.")
                print(f"✅ Nodo {valor} insertado.")
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoBST(valor)
                logger.info(f"Nodo {valor} insertado a la derecha de {nodo_actual.valor}.")
                print(f"✅ Nodo {valor} insertado.")
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
        else:
            logger.warning(f"Intento de insertar un valor duplicado: {valor}.")
            print(f"⚠️ El valor {valor} ya existe en el árbol.")

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None or nodo_actual.valor == valor:
            if nodo_actual:
                logger.info(f"Valor {valor} encontrado en el árbol.")
                print(f"🔍 Valor {valor} encontrado.")
            else:
                logger.info(f"Valor {valor} no encontrado en el árbol.")
                print(f"❌ Valor {valor} no encontrado.")
            return nodo_actual is not None
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        return self._buscar_recursivo(nodo_actual.derecho, valor)
    
    # --- Métodos de Búsqueda (Recorridos) ---

    def preorden(self):
        """Recorrido Preorden (Raíz, Izquierda, Derecha)."""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        logger.info(f"Recorrido Preorden ejecutado: {resultado}")
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def inorden(self):
        """Recorrido Inorden (Izquierda, Raíz, Derecha). Para un BST, devuelve los nodos ordenados."""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        logger.info(f"Recorrido Inorden ejecutado: {resultado}")
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def postorden(self):
        """Recorrido Postorden (Izquierda, Derecha, Raíz)."""
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        logger.info(f"Recorrido Postorden ejecutado: {resultado}")
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)

    def bfs(self):
        """Búsqueda en Anchura (BFS) o Recorrido por Niveles."""
        if not self.raiz:
            return []
        
        resultado = []
        cola = deque([self.raiz])
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        
        logger.info(f"Recorrido BFS ejecutado: {resultado}")
        return resultado