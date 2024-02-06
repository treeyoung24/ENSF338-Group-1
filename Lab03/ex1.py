import sys sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# The first while loop compares the elements from the left and right subarrays and is run for n times for each element.
# The second and third while loops make sure the merge implementation continues even if one of the subarrays
# is empty. The second while loop is run for n/2 times and the third while loop is run for n/2 times.
# The time complexity of the merge function is O(n) and since the time complexity of the dividing step is O(log n),
# the overall algorithm has a worst-case complexity of O(n log n).
            
arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(arr, 0, len(arr) - 1)
print(arr)