# Question 1

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item) # insert element at the head of queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop() # remove and return the last element of the queue
        else:
            raise Exception("Queue is empty") # raise exception if queue is empty
    def is_empty(self):
        return len(self.queue) == 0 # check if queue is empty
    
    def size(self):
        return len(self.queue)  # return number of elements in the queue
    
# Question 2
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
        self.size -= 1
        return item
    
    def size(self):
        return self.size
    


# Question 3
import random
import timeit

def random_tasks():
    tasks = []
    size = 0
    for _ in range(10000):
        if size > 0 and random.random() < 0.3:
            tasks.append('dequeue')
            size += 1
        else:
            tasks.append('enqueue')
            size -= 1
    return tasks

# Question 4

def task_perform(queue,tasks):
    start_time = timeit.default_timer()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(1,100))
        elif task == 'dequeue':
            queue.dequeue()
    end_time = timeit.default_timer()
    return end_time - start_time


# Question 5
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_distribution(array_queue_times, linked_list_queue_times):
    max_time = max(max(array_queue_times), max(linked_list_queue_times))
    plt.hist(array_queue_times, bins=50, alpha=0.6, label='ArrayQueue', range=(0, max_time), color='blue', edgecolor='black')
    plt.hist(linked_list_queue_times, bins=50, alpha=0.6, label='LinkedListQueue', range=(0, max_time), color='red', edgecolor='black')
    plt.ylim(0, max(100, max(plt.ylim())))  
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Queue Performance')
    plt.show()



arrayQueue = [task_perform(Queue(), random_tasks()) for _ in range(100)]
linkedList = [task_perform(LinkedListQueue(), random_tasks()) for _ in range(100)]

averageQueue = sum(arrayQueue) / len(arrayQueue)
averageLL = sum(linkedList) / len(linkedList)

print(f"Average time for ArrayQueue: {averageQueue}")
print(f"Average time for LinkedListQueue: {averageLL}")


plot_distribution(arrayQueue, linkedList)

"""
From the result, it can be seen that implementation of Queue using linked list is faster than using array.
Since the time complexity of enqueue and dequeue operations in linked list is O(1) while in array is O(n).
"""