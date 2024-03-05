import random
import timeit


#1.
class PriorityQueueMergeSort:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.items = self._merge_sort(self.items)  # Sort the items after insertion

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = self._merge_sort(left_half)
        right_half = self._merge_sort(right_half)

        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

#2.
class PriorityQueueSortedInsertion:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if not self.items:
            self.items.append(item)
        else:
            index = 0
            while index < len(self.items) and item > self.items[index]:
                index += 1
            self.items.insert(index, item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

#3.
def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

def time_queue(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)
        elif task == 'dequeue':
            queue.dequeue()
#4.
def measure_performance(queue_impl):
    total_time = 0
    for _ in range(100):
        tasks = generate_random_tasks()
        queue = queue_impl()
        time_taken = timeit.timeit(lambda: time_queue(queue, tasks), number=1)
        total_time += time_taken
    avg_time = total_time / 100
    print(f"Average time taken for {queue_impl.__name__}: {avg_time:.6f} seconds")

#5.


if __name__ == "__main__":
    print("Using PriorityQueueMergeSort:")
    measure_performance(PriorityQueueMergeSort)

    print("\nUsing PriorityQueueSortedInsertion:")
    measure_performance(PriorityQueueSortedInsertion)