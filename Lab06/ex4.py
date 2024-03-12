import random


class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr[:]
        for i in reversed(range(len(self.heap)//2)):
            self._sift_down(i)

    def enqueue(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def dequeue(self):
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return item

    def _sift_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)

    def _sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

def is_heap(list):
    n = len(list)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and list[i] < list[left]:
            return False
        if right < n and list[i] < list[right]:
            return False
    return True

def test_heap():
    # Test 1: Input array is already a correctly sorted heap
    heap = Heap()
    heap.heapify([9, 6, 5, 0, 3, 2])
    if heap.heap != [9, 6, 5, 0, 3, 2]:
        print("Test 1 failed")
    else:
        print("Test 1 passed")

    # Test 2: Input array is empty
    heap = Heap()
    heap.heapify([])
    if heap.heap != []:
        print("Test 2 failed")
    else:
        print("Test 2 passed")

    # Test 3: Input array is a long, randomly shuffled list of integers
    heap = Heap()
    arr = list(range(1000))
    random.shuffle(arr)
    heap.heapify(arr)
    if not is_heap(heap.heap):
        print("Test 3 failed")
    else:
        print("Test 3 passed")

test_heap()