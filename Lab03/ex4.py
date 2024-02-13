import time
import matplotlib.pyplot as plt


def partition(arr, low, high):
    num = 1
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return (i+1)

def quick_sort(arr, low, high, num):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        # print(f"for iteration {num}, array is {arr}") # print after every step
        num += 1
        quick_sort(arr, low, pi-1, num)
        quick_sort(arr, pi+1, high, num)

vector = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # worst case = reverse sorted array

quick_sort(vector, 0, len(vector)-1, 1)

print("quicksort for vector is complete. \n")

sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 350, 400, 500, 600, 750, 850, 975]
quicktimes = []

i = 0
for size in sizes:
    reversedlist = list(range(size, 0, -1)) # worst case where list is reversed
    start_time = time.time()
    quick_sort(reversedlist.copy(), 0, len(reversedlist)-1, 1)
    quicktimes.append(time.time() - start_time)
    print(f"Quick sort time for worst case for size {size} is {quicktimes[i]:.5f}")
    i += 1

plt.plot(sizes, quicktimes)
plt.title('Quick Sort Time')
plt.xlabel('Input Size')
plt.ylabel('Time in seconds')
plt.show()
plt.close()


