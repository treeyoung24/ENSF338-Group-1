import timeit
import random

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

    for size in vector_sizes:
        linear_average_time = measure_search_performance(linear_search, size)
        binary_average_time = measure_search_performance(binary_search, size)

        print(f"Vector size: {size}")
        print(f"Linear Search Average Time: {linear_average_time} seconds")
        print(f"Binary Search Average Time: {binary_average_time} seconds")
        print()
    
if __name__ == "__main__":
    main()