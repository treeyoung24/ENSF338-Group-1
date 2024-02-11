import sys; sys.setrecursionlimit(20000) 

# Import/define stuff we'll need
import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np

# Question 1

#Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Quick sort to sort input array
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Question 2

numTasks = 1000
# Generate random number array
arr = random.sample(range(1, 100000), numTasks)
target = random.choice(arr) # Randomly select a number from the array

random.shuffle(arr)         # Shuffle the array



# Question 3

plt.rcParams['figure.figsize'] = [10, 5]
inputSizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000,
               200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]

linear_search_times = []
binary_search_times = []
avg_linear_times = []
avg_binary_times = []


for size in inputSizes:
    arr = random.sample(range(size * 10), size)
    target = random.choice(arr) # Randomly select a number from the array
    random.shuffle(arr)         # Shuffle the array
    
    linear_search_start = timeit.default_timer()
    linear_search(arr, target)
    linear_search_end = timeit.default_timer()
    linear_search_times.append(linear_search_end - linear_search_start)
    
    binary_search_start = timeit.default_timer()
    binary_search(quick_sort(arr), target)
    binary_search_end = timeit.default_timer()
    binary_search_times.append(binary_search_end - binary_search_start)

plt.figure(figsize=(10, 6))
plt.plot(inputSizes, avg_linear_times, label='Linear Search', marker='o')
plt.plot(inputSizes, avg_binary_times, label='Binary Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Average Time (seconds)')
plt.title('Performance of Linear Search vs Binary Search')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()

