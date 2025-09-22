# arboles/arbol_n_ario.py
from collections import deque
from utils.logger_config import logger

class NodoNario:
    """Clase para un nodo de un Árbol N-ario."""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolNario:
    """Clase para el Árbol N-ario."""
    def __init__(self, valor_raiz):
        self.raiz = NodoNario(valor_raiz)
        logger.info(f"Árbol N-ario inicializado con raíz {valor_raiz}.")

    def buscar_nodo(self, valor):
        """Busca un nodo por su valor y lo retorna."""
        if not self.raiz: return None
        
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            if nodo.valor == valor:
                return nodo
            for hijo in nodo.hijos:
                cola.append(hijo)
        return None

    def insertar(self, valor_nuevo, valor_padre):
        """Inserta un nuevo nodo como hijo de un nodo existente."""
        nodo_padre = self.buscar_nodo(valor_padre)
        if nodo_padre:
            nodo_padre.hijos.append(NodoNario(valor_nuevo))
            logger.info(f"Nodo {valor_nuevo} insertado como hijo de {valor_padre}.")
            print(f"✅ Nodo {valor_nuevo} insertado como hijo de {valor_padre}.")
            return True
        else:
            logger.warning(f"No se encontró el nodo padre con valor {valor_padre}.")
            print(f"❌ No se encontró el nodo padre con valor {valor_padre}.")
            return False

    def bfs(self):
        """Recorrido en anchura (BFS)."""
        if not self.raiz: return []
        
        resultado, cola = [], deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            for hijo in nodo.hijos:
                cola.append(hijo)
        
        logger.info(f"Recorrido BFS ejecutado: {resultado}")
        return resultado
    
    def dfs_preorden(self):
        """Recorrido en profundidad (DFS) en estilo pre-orden."""
        resultado = []
        self._dfs_recursivo(self.raiz, resultado)
        logger.info(f"Recorrido DFS (Preorden) ejecutado: {resultado}")
        return resultado
        
    def _dfs_recursivo(self, nodo, resultado):
        if not nodo: return
        resultado.append(nodo.valor)
        for hijo in nodo.hijos:
            self._dfs_recursivo(hijo, resultado)