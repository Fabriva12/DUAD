class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root  

    def print_tree(self):
        self._print_node(self.root)

    def _print_node(self, node):
        if node is not None:
            print(node.value)            
            self._print_node(node.left)
            self._print_node(node.right)  

nodoA = Node("A")
nodoB = Node("B")
nodoC = Node("C")
nodoD = Node("D")
nodoE = Node("E")

nodoA.left = nodoB
nodoA.right = nodoC
nodoB.left = nodoD
nodoB.right = nodoE

my_tree = BinaryTree(nodoA)

my_tree.print_tree()