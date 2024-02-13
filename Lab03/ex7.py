import time
import matplotlib.pyplot as plt

def binary_search(arr, target, initial_midpoint=None):
    low, high = 0, len(arr) - 1
    if initial_midpoint is not None:
        mid = initial_midpoint
    else:
        mid = (low + high) // 2
    while low <= high:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return -1

def time_search_tasks(arr, target, initial_midpoints):
    times = []
    for initial_midpoint in initial_midpoints:
        start_time = time.time()
        binary_search(arr, target, initial_midpoint)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_search_tasks(arr, target, initial_midpoints, times):
    plt.scatter(initial_midpoints, times)
    plt.xlabel('Initial Midpoint')
    plt.ylabel('Time (s)')
    plt.title('Binary Search with Configurable Initial Midpoint')
    plt.show()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
initial_midpoints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
times = time_search_tasks(arr, target, initial_midpoints)
plot_search_tasks(arr, target, initial_midpoints, times)