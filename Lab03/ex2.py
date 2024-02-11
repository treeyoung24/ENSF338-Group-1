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
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 350, 400, 500, 600, 750, 850, 975]
# sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
bubblebest = []
bubbleworst = []
bubbleavg = []
quickbest = []
quickworst = []
quickavg = []

i = 0
for size in sizes:
    sortedlist = list(range(size)) # best case where list is sorted
    reversedlist = list(range(size, 0, -1)) # worst case where list is reversed
    randomlist = [random.randint(1, size) for i in range(size)] #average case with random list

    start_time = time.time()
    bubble_sort(sortedlist.copy())
    bubblebest.append(time.time() - start_time)
    print(f"Bubble sort time for best case for size {size} is {bubblebest[i]:.5f}")

    start_time = time.time()
    quick_sort(randomlist.copy(), 0, len(randomlist)-1)
    quickbest.append(time.time() - start_time)
    print(f"Quick sort time for best case for size {size} is {quickbest[i]:.5f}") # best case the same as average case, they are both in random order
    
    start_time = time.time()
    bubble_sort(reversedlist.copy())
    bubbleworst.append(time.time() - start_time)
    print(f"Bubble sort time for worst case for size {size} is {bubbleworst[i]:.5f}")

    start_time = time.time()
    quick_sort(reversedlist.copy(), 0, len(reversedlist)-1)
    quickworst.append(time.time() - start_time)
    print(f"Quick sort time for worst case for size {size} is {quickworst[i]:.5f}") # worst case is when array is already sorted, ascending or descending
    
    start_time = time.time()
    bubble_sort(randomlist.copy())
    bubbleavg.append(time.time() - start_time)
    print(f"Bubble sort time for avg case for size {size} is {bubbleavg[i]:.5f}")

    start_time = time.time()
    quick_sort(randomlist.copy(), 0, len(randomlist)-1)
    quickavg.append(time.time() - start_time)
    print(f"Quick sort time for avg case for size {size} is {quickavg[i]:.5f}") # best and average case are same, randomized lists

    i += 1;

plt.plot(sizes, bubblebest, label='Bubble Sort')
plt.plot(sizes, quickbest, label='Quick Sort')
plt.title('Best case')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
plt.close()

plt.plot(sizes, bubbleworst, label='Bubble Sort')
plt.plot(sizes, quickworst, label='Quick Sort')
plt.title('Worst case')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
plt.close()

plt.plot(sizes, bubbleavg, label='Bubble Sort')
plt.plot(sizes, quickavg, label='Quick Sort')
plt.title('Average case')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
plt.close()

# 4. Choose a threshold (on the input size) that determines whether the input
# is “small” or not. Justify your choice based on the plots. [0.2 pts]

# The threshold determined from the plots is around 100 inputs. This number is chosen because in serveral plots that 
# are created, the bubble sort is sometimes faster than quick sort for inputs less than 100. After a list passes 100 elements, quick 
# sort is faster than bubble sort. This is the threshold that determines whether the input is "small" or not.
