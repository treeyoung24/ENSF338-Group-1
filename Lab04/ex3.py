"""
Question 1

The strategy being used here to grow arrays when there are not enough capacity to accomdate new elements is copy the elements from the old array
to a new array. The growth factor is determined by the "list_resize" function which in this case is around 1.125. Meaning the new array
will be approximately 1.125 times the size of the old array. This is done to ensure that the amortized time complexity of appending an element to the list is O(1)

The formula used for overallocation is: new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
The growth factor of 1.125 can be found in the following code: (newsize + (newsize >> 3)), where (newsize >> 3) adds 12.5% of the current size to itself


"""

# Question 2
import sys
my_list = []
old_capacity = sys.getsizeof(my_list)
for i in range(64):
    my_list.append(i)
    new_capacity = sys.getsizeof(my_list)
    if new_capacity != old_capacity:
        print(f"Capacity changed from {old_capacity//4} to {new_capacity//4}")
        old_capacity = new_capacity

    

# Question 3

import timeit

add_times = []

for i in range(1000):
    start_time = timeit.default_timer()
    my_list.append(1)
    end_time = timeit.default_timer()
    add_times.append(end_time-start_time)
    my_list.pop()



# Question 4

sub_times = []

for i in range(1000):
    my_list.pop()
    start_time = timeit.default_timer()
    my_list.append(1)
    end_time = timeit.default_timer()
    sub_times.append(end_time-start_time)

# Print the average time
import matplotlib.pyplot as plt
plt.hist(add_times, bins=100, alpha=0.3, label='From S to S+1')
plt.hist(sub_times, bins=100, alpha=0.3, label='From S-1 to S')
plt.ylabel('Frequency')
plt.xlabel('Time (s)')
plt.xlim(0, 0.0000005)
plt.ylim(0, 1000)
plt.legend(loc='upper right')
plt.show()

"""
The difference in the distribution of both measurements is that the time it takes to grow the array from size S to S+1 is generally 
bigger than the time it takes to grow the array from size S-1 to S. This is because in order to append an element to the array,
the array has to be resized if it does not have enough capacity to accomodate the new element. This resizing process involves copying
all elements to a new array which might incur O(n) time complexity, resulting in the process of appending taking longer.

"""

