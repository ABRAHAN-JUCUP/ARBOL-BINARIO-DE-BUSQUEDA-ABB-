import os
from graphviz import Digraph

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._delete_rec(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def generate_dot(self):
        dot = Digraph(comment='Binary Search Tree')
        self._generate_dot_rec(self.root, dot)
        return dot

    def _generate_dot_rec(self, root, dot):
        if root:
            dot.node(str(root.key))
            if root.left:
                dot.edge(str(root.key), str(root.left.key))
                self._generate_dot_rec(root.left, dot)
            if root.right:
                dot.edge(str(root.key), str(root.right.key))
                self._generate_dot_rec(root.right, dot)

def menu():
    print("1. Insertar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Cargar desde archivo")
    print("5. Convertir a binario")
    print("6. Salir")

def load_from_file(tree, filename):
    with open(filename, 'r') as file:
        for line in file:
            tree.insert(int(line.strip()))

def main():
    tree = BinarySearchTree()
    while True:
        print("\nÁrbol Binario de Búsqueda:")
        dot = tree.generate_dot()
        dot.render('tree', format='png', cleanup=True)
        print("Árbol binario generado y guardado como 'tree.png'.")
        os.system('start tree.png')
        menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            key = int(input("Ingrese el número a insertar: "))
            tree.insert(key)
        elif choice == '2':
            key = int(input("Ingrese el número a buscar: "))
            if tree.search(key):
                print("El número está en el árbol.")
            else:
                print("El número no está en el árbol.")
        elif choice == '3':
            key = int(input("Ingrese el número a eliminar: "))
            tree.delete(key)
        elif choice == '4':
            filename = input("Ingrese el nombre del archivo: ")
            load_from_file(tree, filename)
        elif choice == '5':
            dot = tree.generate_dot()
            dot.render('tree', format='png', cleanup=True)
            print("El árbol binario se ha convertido a binario y se ha guardado como 'tree.png'.")
        elif choice == '6':
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
