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

        pivot = self._get_pivot(root)
        if pivot is None:
            print("Case #1: Pivot not detected")
            self._update_balances(root)
        else:
            left_height = self._get_height(pivot.left)
            right_height = self._get_height(pivot.right)
            if (left_height < right_height and data <= pivot.data) or \
               (right_height < left_height and data > pivot.data):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                self._update_balances(root)
            else:
                print(f"Pivot detected at node with data: {pivot.data}")

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
    
    def _update_balances(self, node):
        if node is None:
            return
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        node.height = 1 + max(left_height, right_height)
        self._update_balances(node.left)
        self._update_balances(node.right)

    def test_cases():
        bst = BinarySearchTree()

        # Test Case 1: Adding a node results in case 1
        root = bst.insert(10)
        bst.insert(20, root)
        bst.insert(30, root)
        print("----")

        # Test Case 2: Adding a node results in case 2
        root = bst.insert(30)
        bst.insert(20, root)
        bst.insert(10, root)
        bst.insert(15, root)
        print("----")

        # Test Case 3: Adding a node results in case 3
        root = bst.insert(20)
        bst.insert(10, root)
        bst.insert(30, root)
        bst.insert(25, root)
        print("Case 3 not supported")
        print("----")

    test_cases()

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