import timeit
import random

# class Node:
#     def __init__(self, data, parent=None, left=None, right=None):
#         self.parent = parent
#         self.data = data
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    # def search(self, root):
    #     current = root
    #     while current is not None:
    #         if self == current.self:
    #             return current
    #         elif self <= current.self:
    #             current = current.left
    #         else:
    #             current = current.right
    #     return None  
    def search(self, root, key):
        current = root
        while current is not None:
            if key == current.val:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
#timing mesaurements, but unfinished.
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
    bst.root = bst.insert(bst.root, element)

# Measure search performance
average_time, total_time = performance_measurement(bst, elements)
print(f"Average time: {average_time}, Total time: {total_time}")

# Shuffle the vector used for question 2 (using random.shuffle)
random.shuffle(elements)

# Measure search performance
average_time, total_time = measure_search_performance(bst, elements)
print(f"Average time after shuffle: {average_time}, Total time after shuffle: {total_time}")