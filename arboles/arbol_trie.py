# arboles/arbol_trie.py
from utils.logger_config import logger

class NodoTrie:
    """Clase para un nodo de un Árbol Trie."""
    def __init__(self):
        self.hijos = {}  # Diccionario para los nodos hijos
        self.es_fin_de_palabra = False

class Trie:
    """Clase para el Árbol Trie."""
    def __init__(self):
        self.raiz = NodoTrie()
        logger.info("Trie inicializado.")

    def insertar(self, palabra):
        """Inserta una palabra en el Trie."""
        nodo_actual = self.raiz
        for char in palabra:
            if char not in nodo_actual.hijos:
                nodo_actual.hijos[char] = NodoTrie()
            nodo_actual = nodo_actual.hijos[char]
        
        if nodo_actual.es_fin_de_palabra:
            logger.warning(f"La palabra '{palabra}' ya existía en el Trie.")
            print(f"⚠️ La palabra '{palabra}' ya existía.")
        else:
            nodo_actual.es_fin_de_palabra = True
            logger.info(f"Palabra '{palabra}' insertada en el Trie.")
            print(f"✅ Palabra '{palabra}' insertada.")

    def buscar(self, palabra):
        """Busca una palabra completa en el Trie."""
        nodo_actual = self.raiz
        for char in palabra:
            if char not in nodo_actual.hijos:
                logger.info(f"La palabra '{palabra}' no fue encontrada.")
                print(f"❌ La palabra '{palabra}' no fue encontrada.")
                return False
            nodo_actual = nodo_actual.hijos[char]
        
        if nodo_actual.es_fin_de_palabra:
            logger.info(f"La palabra '{palabra}' fue encontrada.")
            print(f"🔍 La palabra '{palabra}' fue encontrada.")
            return True
        else:
            logger.info(f"La palabra '{palabra}' no fue encontrada (es un prefijo).")
            print(f"❌ La palabra '{palabra}' no fue encontrada (es solo un prefijo).")
            return False

    def empieza_con(self, prefijo):
        """Verifica si existe alguna palabra en el Trie que comience con el prefijo dado."""
        nodo_actual = self.raiz
        for char in prefijo:
            if char not in nodo_actual.hijos:
                logger.info(f"Ninguna palabra empieza con el prefijo '{prefijo}'.")
                print(f"❌ Ninguna palabra empieza con el prefijo '{prefijo}'.")
                return False
            nodo_actual = nodo_actual.hijos[char]
        
        logger.info(f"Se encontraron palabras que empiezan con '{prefijo}'.")
        print(f"🔍 Se encontraron palabras que empiezan con '{prefijo}'.")
        return True