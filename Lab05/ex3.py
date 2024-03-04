import random
import timeit

import matplotlib.pyplot as plt


#1.
class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

#2.
class LinkedListStack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from an empty stack")
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def is_empty(self):
        return self.head is None

#3.
def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append('push')
        else:
            tasks.append('pop')
    return tasks

#4.
def measure_performance(stack_impl, tasks):
    stack = stack_impl()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'push':
            stack.push(1)  # Pushing a dummy value
        else:
            if not stack.is_empty():
                stack.pop()
    end_time = timeit.default_timer()
    return end_time - start_time

#5.
if __name__ == "__main__":
    tasks_lists = [generate_random_tasks() for _ in range(100)]

    array_times = [measure_performance(ArrayStack, tasks) for tasks in tasks_lists]
    linked_list_times = [measure_performance(LinkedListStack, tasks) for tasks in tasks_lists]

    plt.hist(array_times, alpha=0.5, label='Array Stack')
    plt.hist(linked_list_times, alpha=0.5, label='Linked List Stack')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Stack Performance')
    plt.legend(loc='upper right')
    plt.show()
# The graph shows that the array stack is faster than the linked list stack.
# Theoretically, push and pop are constant time operations for both implementations.
# However, the array stack could be faster in practice due to having a fixed-size array
# and not having to allocate memory for each new node as a linked-list would.