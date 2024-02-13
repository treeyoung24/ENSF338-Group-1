import time

import matplotlib.pyplot as plt
import numpy as np


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, item, start, end):
    if start == end:
        return start if arr[start] > item else start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < item:
        return binary_search(arr, item, mid + 1, end)
    elif arr[mid] > item:
        return binary_search(arr, item, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = binary_search(arr, item, 0, i - 1)
        while i > j:
            arr[i] = arr[i - 1]
            i -= 1
        arr[j] = item
    return arr

def main():
    arrays = [list(np.random.randint(1, 1000, size)) for size in range(1000, 20000, 5000)]
    insertion_sort_times = []
    binary_insertion_sort_times = []

    for arr in arrays:
        arr_copy = arr.copy()

        start = time.time()
        insertion_sort(arr)
        end = time.time()
        insertion_sort_times.append(end - start)

        start = time.time()
        binary_insertion_sort(arr_copy)
        end = time.time()
        binary_insertion_sort_times.append(end - start)

    lengths = [len(arr) for arr in arrays]
    plt.plot(lengths, insertion_sort_times, label='Insertion Sort')
    plt.plot(lengths, binary_insertion_sort_times, label='Binary Insertion Sort')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()

# Traditional insertion sort becomes exponentially faster than binary insertion sort for larger arrays. 
# This is because binary insertion sort goes through the whole array to find the correct position for the 
# element to be inserted, which is O(n). However, the traditional insertion sort only goes through the array 
# elements that are to the left of the current element being inserted, which is O(n) in the worst case. 
# Therefore, binary insertion sort is slower than traditional insertion sort for larger arrays.