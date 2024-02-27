# 3.
# Inneficient Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 4. 
# The worst-case complexity of the inneficient implementation is O(n) because the
# for loop will run n times in the case that the target is the last element in the list. 
# The worst-case complexity of the efficient implementation is O(log n) because the while loop
# will run log n times in the case that the target is not in the middle of the list.

# 5.
# 1) 
import random
import timeit

import matplotlib.pyplot as plt


def main():
    num_elements = 1000
    num_measurements = 100
    arr = sorted(random.sample(range(num_elements), num_elements))
    target = random.randint(0, num_elements - 1)

    linear_times = []
    binary_times = []

    for i in range(num_measurements):
        linear_time = timeit.timeit(lambda: linear_search(arr, target), number=1)
        linear_times.append(linear_time)
        binary_time = timeit.timeit(lambda: binary_search(arr, target), number=1)
        binary_times.append(binary_time)

    plt.hist(linear_times, bins=20, alpha=0.5, label='Linear Search')
    plt.hist(binary_times, bins=20, alpha=0.5, label='Binary Search')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Comparison of Linear and Binary Search')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()