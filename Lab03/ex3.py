import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps += 1
    return comparisons, swaps

def test(arr):
    comparisons, swaps = bubble_sort(arr)
    print(f'Sorted array: {arr}\n Number of comparisons: {comparisons}\n Number of swaps: {swaps}')
    return comparisons, swaps

def plot(sizes, comparison_counts, swap_counts):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, comparison_counts, marker='o')
    plt.title('Number of Comparisons')
    plt.xlabel('Input Size')
    plt.ylabel('Comparisons')

    plt.subplot(1, 2, 2)
    plt.plot(sizes, swap_counts, marker='o')
    plt.title('Number of Swaps')
    plt.xlabel('Input Size')
    plt.ylabel('Swaps')

    plt.tight_layout()
    plt.show()

def main():
    sizes = []
    comparison_counts = []
    swap_counts = []

    arr = [30, 22, 7, 20, 14]
    comparisons, swaps = test(arr)
    sizes.append(len(arr))
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

    arr = [38, 29, 5, 49, 18, 11, 1, 23]
    comparisons, swaps = test(arr)
    sizes.append(len(arr))
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

    arr = [14, 2, 17, 40, 15, 23, 11, 36, 4, 29, 33]
    comparisons, swaps = test(arr)
    sizes.append(len(arr))
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

    arr = [10, 17, 30, 13, 21, 20, 42, 28, 19, 7, 29, 4, 38, 47, 11, 36, 45]
    comparisons, swaps = test(arr)
    sizes.append(len(arr))
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

    arr = [45, 49, 37, 39, 21, 22, 26, 32, 47, 12, 4, 5, 20, 11, 7, 48, 41, 30, 15, 1]
    comparisons, swaps = test(arr)
    sizes.append(len(arr))
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

    plot(sizes, comparison_counts, swap_counts)

if __name__ == '__main__':
    main()