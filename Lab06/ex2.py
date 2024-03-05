import random
import timeit


#1.
class Node:
     def __init__(self, data, parent=None, left=None, right=None):
          self.parent = parent
          self.data = data
          self.left = left
          self.right = right

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

#2.1
sorted_vector = list(range(10000))
random.shuffle(sorted_vector)

root = None
for data in sorted_vector:
    insert(data, root)

#2.2
total_time = 0
for data in sorted_vector:
    avg_time = timeit.timeit(lambda: search(data, root), number=10) / 10
    total_time += avg_time

average_time = total_time / len(sorted_vector)
average_time, total_time
print("Average Time:", average_time)
print("Total Time:", total_time)

#3.1
sorted_vector.sort()
total_time = 0
for data in sorted_vector:
    avg_time = timeit.timeit(lambda: search(data, root), number=10) / 10
    total_time += avg_time
average_time = total_time / len(sorted_vector)
average_time, total_time
print("Average Time:", average_time)
print("Total Time:", total_time)