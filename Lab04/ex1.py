import random
import timeit

import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def newNode(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp

def middle(start, last):
    if start is None:
        return None
    slow = start
    fast = start.next

    while fast != last:
        fast = fast.next
        if fast != last:
            slow = slow.next
            fast = fast.next

    return slow

def binarySearch(head, value):
    start = head
    last = None

    while True:
        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if mid is None:
            return None

        # If value is present at middle
        if mid.data == value:
            return mid

        # If value is more than mid
        elif mid.data < value:
            start = mid.next

        # If the value is less than mid.
        else:
            last = mid

        if not (last is None or last != start):
            break

    # value not present
    return None

class Array:
    def __init__(self):
        self.array = []

    def insert(self, data):
        self.array.append(data)
        self.array.sort()

    def display(self):
        return self.array

    def binary_search(self, target):
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

def main():
    sizes = [1000, 2000, 4000, 8000]
    array_times = []
    linked_list_times = []

    for size in sizes:
        data = random.sample(range(1, size * 10), size)

        # Create and populate array
        array = Array()
        for item in data:
            array.insert(item)

        # Create and populate linked list
        head = None
        for item in sorted(data):
            if head is None:
                head = newNode(item)
                current = head
            else:
                current.next = newNode(item)
                current.next.prev = current
                current = current.next

        search_element = random.choice(data)

        # Measure binary search time for array
        array_time = timeit.timeit(lambda: array.binary_search(search_element), number=1000)
        array_times.append(array_time)

        # Measure binary search time for linked list
        linked_list_time = timeit.timeit(lambda: binarySearch(head, search_element), number=1000)
        linked_list_times.append(linked_list_time)

    plt.plot(sizes, array_times, label='Array')
    plt.plot(sizes, linked_list_times, label='LinkedList')
    plt.xlabel('Array size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
