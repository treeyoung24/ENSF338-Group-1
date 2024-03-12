import timeit
import random
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)

        # If the list is empty or the new value is smaller than the head value
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            # Find the appropriate position to insert the new value
            while current.next is not None and current.next.value <= value:
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("Priority queue is empty")

        value = self.head.value
        self.head = self.head.next
        return value
    
class HeapPriorityQueue:
    def __init__(self):
        self.heap = [] # Initialize an empty list to store the heap

    def enqueue(self, value):
        heapq.heappush(self.heap, value)

    def dequeue(self):
        if not self.heap: # Check if the heap is empty
            raise IndexError("Priority queue is empty")
        return heapq.heappop(self.heap)

def measure_time(queue, tasks):
    start = timeit.default_timer()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        else:
            try:
                queue.dequeue()
            except IndexError:
                pass
    end = timeit.default_timer()
    total_time = end - start
    average_time = total_time / len(tasks)
    return total_time, average_time

# Generate a list of 1000 tasks. Each task is either an enqueue operation (with probability 0.7) or a dequeue operation (with probability 0.3)
tasks = [('enqueue', random.randint(1, 100)) if random.random() < 0.7 else ('dequeue',) for _ in range(1000)]

list_queue = ListPriorityQueue()
heap_queue = HeapPriorityQueue()

listmeasuretime = measure_time(list_queue, tasks)
heapmeasuretime = measure_time(heap_queue, tasks)

print(f"Total time for ListPriorityQueue: {listmeasuretime[0]}, average time: {listmeasuretime[1]}")
print(f"Total time for HeapPriorityQueue: {heapmeasuretime[0]}, average time: {heapmeasuretime[1]}")

# 4. The implementation of priority queue using a heap is faster than the one using a linked list based on the results. This could be because
# HeapPriorityQueue has a time complexity of O(log n) for both enqueue and dequeue operations, while the ListPriorityQueue has a time complexity of O(n) 
# for enqueue and O(1) for dequeue. The linked list implementation requires traversing the list to find the correct position for insertion, which is slower than the heap implementation. 
