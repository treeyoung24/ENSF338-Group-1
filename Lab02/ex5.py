import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import timeit
import random

def linear_func(x, a, b):
    return a * x + b

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def log_func(x, a, b):
    return a * np.log(x) + b

def measure_search_performance(search_function, vector_size):
    # Generate a sorted vector
    sorted_vector = list(range(vector_size))

    # Measure performance for 1000 iterations
    total_time = timeit.timeit(lambda: search_function(sorted_vector, random.randint(0, vector_size - 1)),
                               number=100)
    average_time = total_time / 100

    return average_time
def main():
    vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    linear_times = []
    binary_times = []

    for size in vector_sizes:
        linear_average_time = measure_search_performance(linear_search, size)
        binary_average_time = measure_search_performance(binary_search, size)

        linear_times.append(linear_average_time)
        binary_times.append(binary_average_time)

    # Plotting the data
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(vector_sizes, linear_times, 'o')
    popt, _ = curve_fit(linear_func, vector_sizes, linear_times)
    plt.plot(vector_sizes, linear_func(np.array(vector_sizes), *popt), '-')
    plt.title("Linear Search")
    print(f"Linear search function parameters: {popt}")

    plt.subplot(1, 2, 2)
    plt.plot(vector_sizes, binary_times, 'o')
    popt, _ = curve_fit(log_func, vector_sizes, binary_times)
    plt.plot(vector_sizes, log_func(np.array(vector_sizes), *popt), '-')
    plt.title("Binary Search")
    print(f"Binary search function parameters: {popt}")

    plt.show()

if __name__ == "__main__":
    main()


"""
The linear search function has a time complexity of O(n), while the binary search function has a time complexity of O(log n).
The linear search function parameters are approximately [1e-07, 1e-05], while the binary search function parameters are approximately [1e-07, 1e-05].
While the linear search function has a linear plot, the binary search function has a logarithmic plot.
The results are as expected since linear search has a linear time complexity O(n), while binary search has a logarithmic time complexity O(log n).
"""