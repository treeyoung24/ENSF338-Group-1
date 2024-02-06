# 1. Implement and test both algorithms on input of 20 different sizes. The
# choice of sizes is yours, but it must be such that it evidences for which
# sizes each algorithm is faster [0.2 pts]

# 2. Each test must be repeated on best, worst, and average case scenario for
# both algorithm [0.4 pts]
#   1. Note that “best/worst/average” may mean different things for the two different
#   algorithms

# 3. Generate performance plots for all the six (three?) cases. Performance of
# both algorithms must be visualized in each plot. In the plots, highlight for
# which inputs one algorithm perform better than the other [0.4 pts]

# 4. Choose a threshold (on the input size) that determines whether the input
# is “small” or not. Justify your choice based on the plots. [0.2 pts]

import time
import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):   
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000, 10000]
bubbletimes = []
quicktimes = []

for size in sizes:
    sortedlist = list(range(size)) # best case where list is sorted
    reversedlist = list(range(size, 0, -1)) # worst case where list is reversed
    randomlist = [random.randint(1, size) for i in range(size)] #average case with random list

    start_time = time.time()
    bubble_sort(sortedlist.copy())
    bubbletimes.append(time.time() - start_time)
    print(f"Bubble sort time for best case for size {size} is {bubbletimes[0]}")

    start_time = time.time()
    quick_sort(sortedlist.copy(), 0, len(sortedlist)-1)
    quicktimes.append(time.time() - start_time)
    print(f"Quick sort time for best case for size {size} is {quicktimes[0]}")
    
    start_time = time.time()
    bubble_sort(reversedlist.copy())
    bubbletimes.append(time.time() - start_time)
    print(f"Bubble sort time for worst case for size {size} is {bubbletimes[1]}")

    start_time = time.time()
    quick_sort(reversedlist.copy(), 0, len(reversedlist)-1)
    quicktimes.append(time.time() - start_time)
    print(f"Quick sort time for worst case for size {size} is {quicktimes[1]}")
    
    start_time = time.time()
    bubble_sort(sortedlist.copy())
    bubbletimes.append(time.time() - start_time)
    print(f"Bubble sort time for avg case for size {size} is {bubbletimes[2]}")

    start_time = time.time()
    quick_sort(randomlist.copy(), 0, len(randomlist)-1)
    quicktimes.append(time.time() - start_time)
    print(f"Quick sort time for avg case for size {size} is {quicktimes[2]}")
    
    # arr = [random.randint(1, size) for i in range(size)]
    # start_time = time.time()
    # bubble_sort(arr.copy())
    # bubble_times.append(time.time() - start_time)
    # quickstart_time = time.time()
    # quick_sort(arr.copy(), 0, len(arr)-1)
    # quick_times.append(time.time() - quickstart_time)

plt.plot(sizes, bubbletimes, label='Bubble Sort')
plt.plot(sizes, quicktimes, label='Quick Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()

print("bubble times are as follows:",bubbletimes)
print("quicksort times are as follows:",quicktimes)
print("hello world")