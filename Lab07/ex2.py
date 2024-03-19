import random
import time

import matplotlib.pyplot as plt


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

# 1.
class BinarySearchTree:
    
    def _get_pivot(self, node):
        if node is None:
            return None
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return node
        return self._get_pivot(node.parent)

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
        elif data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)
        if parent is not None:
            parent.height = 1 + max(self._get_height(parent.left), self._get_height(parent.right))
        return root

    def search(self, data, root):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

# 2.
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return abs(self._get_height(node.left) - self._get_height(node.right))

    def _preorder_traversal(self, node):
        if node:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)

# 3.
tasks = [list(range(1, 1001)) for _ in range(1000)]
for task in tasks:
    random.shuffle(task)

# 4.
bst = BinarySearchTree()

performances = []
balances = []
for task in tasks:
    root = None
    for item in task:
        root = bst.insert(item, root)
    start_time = time.time()
    for item in task:
        bst.search(item, root)
    end_time = time.time()
    performances.append(end_time - start_time)
    balances.append(max(bst._get_balance(node) for node in bst._preorder_traversal(root)))

# 5.
plt.scatter(balances, performances)
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time')
plt.show()