"""
Question 1

According to the code the strategy being used to grow arrays when full is called over-allocation
and it is used to reduce the number of times the array needs to be resized when elements are added to the list. 


new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;

from the line above, it can be seemn that newsize >> 3 is equivalent to newsize/8. so the new size is the old size plus
about 1/8 of the old size. Therefore it has a growth factor of 1.125

The + 6 and & ~(size_t)3 parts are used to round up the new size to the nearest multiple of 4.

The code also includes a check to prevent over-allocation when the new size is closer to the over-allocated size than to the old size:

if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize))
    new_allocated = ((size_t)newsize + 3) & ~(size_t)3;

In this case, the new size is rounded up to the nearest multiple of 4 without the additional growth factor.

This strategy of over-allocation helps to achieve linear-time amortized performance over a sequence of append operations, even if the system's realloc function performs poorly.
"""

# Question 2

import sys

# Create an empty list
list = []

# Initialize the size of the list
old_size = sys.getsizeof(list)

# Loop from 0 to 63
for i in range(64):
    # Add an integer to the list
    list.append(i)

    # Get the new size of the list
    new_size = sys.getsizeof(list)

    # If the size has changed, print a message
    if new_size != old_size:
        print(f"Capacity changed after adding element {i}, new capacity: {new_size // 28}") # Assume each interger takes 28 bytes
        S = i
        old_size = new_size

    

# Question 3
import sys
import timeit

# Create an empty list
list = []

# Initialize the size of the list
old_size = sys.getsizeof(list)

# Measure the time it takes to grow the array from size S to S+1
times = []

for i in range(1000):
    # Add an integer to the list
    list.append(i)

    # Measure the time it takes to grow the array from size S to S+1
    start_time = timeit.default_timer()
    list.append(i + 1)
    end_time = timeit.default_timer()
    times.append(end_time - start_time)

# Print the distribution of the measurements
avg_time = sum(times) / len(times)
print(avg_time)

# Question 4

import sys
import timeit

# Create an empty list
list = []

# Initialize the size of the list
old_size = sys.getsizeof(list)

# Measure the time it takes to grow the array from size S-1 to S
times = []

for i in range(1000):
    # Add an integer to the list
    list.append(i)

    # Measure the time it takes to grow the array from size S-1 to S
    start_time = timeit.default_timer()
    list.append(i + 1)
    list.pop()
    end_time = timeit.default_timer()
    times.append(end_time - start_time)

# Print the distribution of the measurements
avg_time = sum(times) / len(times)
print(avg_time)


# Question 5

import matplotlib.pyplot as plt

# Measure the time it takes to grow the array from size S to S+1
times1 = []
for i in range(1000):
    start_time = timeit.default_timer()
    list.append(i)
    end_time = timeit.default_timer()
    times1.append(end_time - start_time)

# Measure the time it takes to grow the array from size S-1 to S
times2 = []
for i in range(1000):
    start_time = timeit.default_timer()
    list.append(i)
    list.pop()
    end_time = timeit.default_timer()
    times2.append(end_time - start_time)

# Plot the distribution of both measurements
plt.hist(times1, bins=100, alpha=0.5, label='S to S+1')
plt.hist(times2, bins=100, alpha=0.5, label='S-1 to S')
plt.legend(loc='upper right')
plt.show()


