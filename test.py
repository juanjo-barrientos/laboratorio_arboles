# tests.py
import unittest
# Importar todas las clases de árboles
from arboles.arbol_binario import ArbolBinarioBusqueda
from arboles.arbol_avl import ArbolAVL
from arboles.arbol_b import ArbolB
from arboles.arbol_trie import Trie
from arboles.arbol_n_ario import ArbolNario

class TestArbolBinarioBusqueda(unittest.TestCase):
    # (El código de esta clase de prueba ya lo tienes)
    def setUp(self):
        self.bst = ArbolBinarioBusqueda()
        self.elementos = [50, 30, 70, 20, 40, 60, 80]
        for elemento in self.elementos:
            self.bst.insertar(elemento)
    def test_recorrido_inorden(self):
        self.assertEqual(self.bst.inorden(), [20, 30, 40, 50, 60, 70, 80])

class TestArbolAVL(unittest.TestCase):
    def setUp(self):
        self.avl = ArbolAVL()
        # Caso que requiere rotación simple izquierda
        self.avl.insertar(10)
        self.avl.insertar(20)
        self.avl.insertar(30)
    
    def test_balanceo_rotacion_simple(self):
        # Después de insertar 10, 20, 30, la raíz debería ser 20
        self.assertEqual(self.avl.raiz.valor, 20)
        self.assertEqual(self.avl.inorden(), [10, 20, 30])

    def test_busqueda_avl(self):
        self.assertTrue(self.avl.buscar(10))
        self.assertTrue(self.avl.buscar(30))
        self.assertFalse(self.avl.buscar(99))

class TestArbolB(unittest.TestCase):
    def setUp(self):
        # Grado mínimo 3. Cada nodo puede tener entre 2 y 5 claves.
        self.b_tree = ArbolB(t=3)
        self.claves = [10, 20, 5, 6, 12, 30, 7, 17]
        for clave in self.claves:
            self.b_tree.insertar(clave)

    def test_insercion_y_busqueda_b(self):
        self.assertTrue(self.b_tree.buscar(6)[0])
        self.assertTrue(self.b_tree.buscar(30)[0])
        self.assertFalse(self.b_tree.buscar(99)[0])

    def test_division_raiz(self):
        # Insertar suficientes claves para forzar una división de la raíz
        b_tree_split = ArbolB(t=2) # Nodos con max 3 claves
        claves = [10, 20, 30, 40]
        for c in claves:
            b_tree_split.insertar(c)
        # La raíz debería haber sido dividida y ahora contener [20]
        self.assertEqual(b_tree_split.root.keys, [20])
        self.assertFalse(b_tree_split.root.leaf)

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.palabras = ["hola", "hasta", "horario", "gato", "gata"]
        for p in self.palabras:
            self.trie.insertar(p)

    def test_busqueda_trie(self):
        self.assertTrue(self.trie.buscar("hola"))
        self.assertTrue(self.trie.buscar("gata"))
        self.assertFalse(self.trie.buscar("ho")) # Es prefijo, no palabra
        self.assertFalse(self.trie.buscar("mundo"))

    def test_prefijo_trie(self):
        self.assertTrue(self.trie.empieza_con("ho"))
        self.assertTrue(self.trie.empieza_con("gat"))
        self.assertFalse(self.trie.empieza_con("mu"))

class TestArbolNario(unittest.TestCase):
    def setUp(self):
        self.n_ario = ArbolNario("A")
        self.n_ario.insertar("B", "A")
        self.n_ario.insertar("C", "A")
        self.n_ario.insertar("D", "B")
        self.n_ario.insertar("E", "C")
    
    def test_insercion_y_busqueda_n_ario(self):
        self.assertIsNotNone(self.n_ario.buscar_nodo("A"))
        self.assertIsNotNone(self.n_ario.buscar_nodo("D"))
        self.assertIsNone(self.n_ario.buscar_nodo("Z"))
    
    def test_bfs_n_ario(self):
        self.assertEqual(self.n_ario.bfs(), ["A", "B", "C", "D", "E"])
        
    def test_dfs_n_ario(self):
        self.assertEqual(self.n_ario.dfs_preorden(), ["A", "B", "D", "C", "E"])

if __name__ == '__main__':
    unittest.main(verbosity=2)