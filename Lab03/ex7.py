import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def timed_binary_search(arr, target, start_mid):
    start_time = time.time()
    result = binary_search(arr, target, start_mid, len(arr) - 1)
    end_time = time.time()
    return result, end_time - start_time

def time_search_tasks(arr, targets, initial_midpoints):
    results = []
    for target in targets:
        task_results = []
        for mid in initial_midpoints:
            result, time_taken = timed_binary_search(arr, target, mid)
            task_results.append((mid, result, time_taken))
        results.append(task_results)
    return results

def get_best_midpoints(results):
    best_midpoints = []
    for task_results in results:
        best_midpoint = min(task_results, key=lambda x: x[2])
        best_midpoints.append(best_midpoint)
    return best_midpoints

def plot_scatterplot(results, best_midpoints):
    plt.figure(figsize=(10, 6))
    for i, task_results in enumerate(results):
        midpoints, times = zip(*[(mid, time) for mid, _, time in task_results])
        plt.scatter(midpoints, times, label=f'Task {i+1}')
    best_midpoints, best_times = zip(*[(mid, time) for mid, _, time in best_midpoints])
    plt.scatter(best_midpoints, best_times, color='red', marker='x', label='Best Midpoints')
    plt.xlabel('Initial Midpoint')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Performance of Binary Search with Different Initial Midpoints')
    plt.legend()
    plt.show()

# Example usage:
arr = sorted(random.sample(range(1, 100), 50))
targets = [random.randint(1, 100) for _ in range(5)]
initial_midpoints = [10, 20, 30, 40, 45]

results = time_search_tasks(arr, targets, initial_midpoints)
best_midpoints = get_best_midpoints(results)
plot_scatterplot(results, best_midpoints)
