import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def random_task(size):
    arr = list(range(size))
    random.shuffle(arr)
    target = random.choice(arr)
    return arr, target

def measure_performance(size):
    linear_search_times = []
    binary_search_times = []
    for _ in range(100):
        arr, target = random_task(size)
        start_time = time.time()
        linear_search(arr, target)
        linear_search_times.append(time.time() - start_time)
        quicksort(arr)
        start_time = time.time()
        binary_search(arr, target)
        binary_search_times.append(time.time() - start_time)
    return linear_search_times, binary_search_times

def plot_performance(sizes, linear_search_times, binary_search_times):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, linear_search_times, label='Linear Search')
    plt.xlabel('Size')
    plt.ylabel('Time (s)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(sizes, binary_search_times, color='orange', label='Binary Search')
    plt.xlabel('Size')
    plt.ylabel('Time (s)')
    plt.legend()

    plt.tight_layout()
    plt.show()



sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_search_times = []
binary_search_times = []
for size in sizes:
    linear_search_times.append(sum(measure_performance(size)[0]))
    binary_search_times.append(sum(measure_performance(size)[1]))
plot_performance(sizes, linear_search_times, binary_search_times)