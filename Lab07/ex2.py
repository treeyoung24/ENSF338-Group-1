class Node:
    def __init__(self, data, left=None, right=None, parent=None, height=1):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 1
        self.balance = 0  # New nodes are balanced
        

class AVLTree:
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def insert(self, data, root=None):
        current = root
        parent = None
        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        if root is None:
            root = Node(data)
        else:
            if data <= parent.data:
                parent.left = Node(data, parent=parent)
            else:
                parent.right = Node(data, parent=parent)

        pivot = None
        current = parent
        while current is not None:
            current.height = 1 + max(self._get_height(current.left), self._get_height(current.right))
            if abs(self._get_balance(current)) > 1:
                pivot = current
                break
            current = current.parent
        # Checking if pivot is None
        if pivot is None:
            print("Case #1: Pivot not detected")
        else:
        # Check if node was added to the shorter subtree
            if (pivot.balance == -1 and self._get_balance(pivot.right) == 1) or \
            (pivot.balance == 1 and self._get_balance(pivot.left) == -1):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case #3 not supported")

        return root, pivot

print("Adding a node results in Case 1")
avlt = AVLTree()
root, pivot = avlt.insert(10)
root, pivot = avlt.insert(5, root)
root, pivot = avlt.insert(15, root) 
# tree is balanced after adding 15.

print("Adding a node results in Case 2")
avlt = AVLTree()
root, pivot = avlt.insert(20)
root, pivot = avlt.insert(10, root)
root, pivot = avlt.insert(30, root)
root, pivot = avlt.insert(25, root)

print("Adding a node results in Case 3")
avlt = AVLTree()
root, pivot = avlt.insert(25, root)