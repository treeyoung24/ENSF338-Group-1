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
    
