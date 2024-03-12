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

#2.1
sorted_vector = list(range(10000))
vector_copy = sorted_vector.copy()
random.shuffle(sorted_vector)

root = None
for data in sorted_vector:
    root = insert(data, root)

#2.2
total_time_shuffled = 0
for data in sorted_vector:
    avg_time = timeit.timeit(lambda: search(data, root), number=10) / 10
    total_time_shuffled += avg_time

average_time = total_time_shuffled / len(sorted_vector)
print("Average Time for Shuffled Array:", average_time)
print("Total Time for Shuffled Array:", total_time_shuffled)

#3.1
vector_copy.sort()
root = None
for data in vector_copy:
    root = insert(data, root)

#3.2
total_time_sorted = 0
for data in sorted_vector:
    avg_time = timeit.timeit(lambda: search(data, root), number=10) / 10
    total_time_sorted += avg_time
average_time = total_time_sorted / len(sorted_vector)
print("Average Time for Sorted Array:", average_time)
print("Total Time for Sorted Array:", total_time_sorted)

#4.
# The shuffled array approach is much faster. This is because the tree made from the sorted array is extremely
# unbalanced as inserting each element in order will result in a tree that is essentially a linked list. This
# means that the search time for the sorted array is O(n) as it has to traverse the entire tree to find the
# element while using the shuffled array, the time complexity on average is O(log n) as the tree is much more
# balanced.