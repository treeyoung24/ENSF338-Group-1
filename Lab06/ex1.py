import timeit
import random
import sys

# avoid RecursionError limit of standard 1000
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

 
    def search(self, root, key):
        current = root
        while current is not None:
            if key == current.val:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
#timing mesaurements
def performance_measurement(bst, elements):
    total_time = 0
    for element in elements:
        start_time = timeit.default_timer()
        for i in range(10):
            bst.search(bst.root, element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    average_time = total_time / (len(elements) * 10)
    return average_time, total_time


#Generate a 10000-element sorted vector and use it to build a tree by inserting each element
elements = list(range(10000))

bst = BinarySearchTree()
for element in elements:
    bst.root = bst.insert(element)

# Measure search performance of sorted 
average_time, total_time = performance_measurement(bst, elements)
print(f"Average time: {average_time}, Total time: {total_time}")

# Shuffle the vector
random.shuffle(elements)

# Measure search performance of shuffled
average_time, total_time = performance_measurement(bst, elements)
print(f"Average time after shuffle: {average_time}, Total time after shuffle: {total_time}")

# 4. Discuss the results:
# The faster approach would be the shuffled array. This is because the tree is less efficient with the elements being in a linked list, which happens 
# with the array being sorted. The shuffled array has a well balanced tree, which is more efficient.
