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

def insert(data, root=None):
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
        parent.height = 1 + max(_get_height(parent.left), _get_height(parent.right))
    return root

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def _get_height(node):
    if not node:
        return 0
    return node.height

def _get_balance(node):
    if not node:
        return 0
    return abs(_get_height(node.left) - _get_height(node.right))

def _preorder_traversal(node):
    if node:
        yield node
        yield from _preorder_traversal(node.left)
        yield from _preorder_traversal(node.right)

# Generate tasks
tasks = [list(range(1, 1001)) for _ in range(1000)]
for task in tasks:
    random.shuffle(task)

# Measure performance and balance
performances = []
balances = []
for task in tasks:
    root = None
    for item in task:
        root = insert(item, root)
    start_time = time.time()
    for item in task:
        search(item, root)
    end_time = time.time()
    performances.append(end_time - start_time)
    balances.append(max(_get_balance(node) for node in _preorder_traversal(root)))

# Generate scatterplot
plt.scatter(balances, performances)
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time')
plt.show()