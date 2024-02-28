class ListNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.first_node = None

    def add_node(self, data):
        new_node = ListNode(data)
        if self.first_node is None:
            self.first_node = new_node
        else:
            current_node = self.first_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def get_length(self):
        count = 0
        current_node = self.first_node
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def get_node_at_index(self, index):
        current_node = self.first_node
        for i in range(index):
            current_node = current_node.next_node
        return current_node

    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_length()-1, -1, -1):
            currNode = self.get_node_at_index(i)
            currNewNode = ListNode(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next_node = currNewNode
            prevNode = currNewNode
        self.head = newhead
        
    def optimized_reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

import timeit
import random
import matplotlib.pyplot as plt

sizes = [1000, 2000, 3000, 4000]
reverseTimes = []
optimizedReverseTimes = []

for size in sizes:
    print(f"Size {size}:")
    linked_list = SinglyLinkedList()
    for i in range(size):
        linked_list.add_node(random.randint(0, 1000))
    reverseTime = timeit.timeit("linked_list.reverse()", globals=globals(), number=100)
    reverseTimes.append(reverseTime)
    print(f"Reverse time for size {size} is {reverseTime}")
    optimizedReverseTime = timeit.timeit("linked_list.optimized_reverse()", globals=globals(), number=100)
    optimizedReverseTimes.append(optimizedReverseTime)
    print(f"Optimized reverse time for size {size} is {optimizedReverseTime}")

plt.plot(sizes, reverseTimes, label="Reverse")
plt.plot(sizes, optimizedReverseTimes, label="Optimized Reverse")
plt.legend()
plt.xlabel("Size of List")
plt.ylabel("Time (s)")
plt.title("Time to Reverse a Linked List")
plt.show()