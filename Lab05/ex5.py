# Question 1
class CircularQueueArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("enqueue None")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        front_item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {front_item}")
        return front_item

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        print(f"peek {self.queue[self.front]}")
        return self.queue[self.front]


# Question 2
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        print(f"enqueue {item}")

    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        if self.front == self.rear:  # Only one element
            temp = self.front
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
        print(f"dequeue {temp.value}")
        return temp.value

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        print(f"peek {self.front.value}")
        return self.front.value


# Question 3

# Assuming queue capacity is 5 for array implementation
queue = CircularQueueArray(5)

# Test operations
operations = [
    lambda: queue.enqueue(1),  # enqueue 1
    lambda: queue.enqueue(2),  # enqueue 2
    lambda: queue.peek(),      # peek 1
    lambda: queue.dequeue(),   # dequeue 1
    lambda: queue.enqueue(3),  # enqueue 3
    lambda: queue.enqueue(4),  # enqueue 4
    lambda: queue.enqueue(5),  # enqueue 5
    lambda: queue.enqueue(6),  # enqueue 6
    lambda: queue.dequeue(),   # dequeue 2
    lambda: queue.dequeue(),   # dequeue 3
    lambda: queue.peek(),      # peek 4
    lambda: queue.dequeue(),   # dequeue 4
    lambda: queue.dequeue(),   # dequeue 5
    lambda: queue.dequeue(),   # dequeue 6
    lambda: queue.peek(),      # peek None
    lambda: queue.dequeue(),   # dequeue None
    lambda: queue.enqueue(7),  # enqueue 7
    lambda: queue.enqueue(8),  # enqueue 8
    lambda: queue.enqueue(9),  # enqueue 9
    lambda: queue.enqueue(10), # enqueue 10
    lambda: queue.enqueue(11), # enqueue 11
    lambda: queue.enqueue(12), # enqueue None (queue is full)
]

# Execute operations
for op in operations:
    op()
