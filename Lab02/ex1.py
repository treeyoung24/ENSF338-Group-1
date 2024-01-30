'''
Question 1.

The code defines a recursive function called func that takes an interger n and output the nth number in the Fibonacci sequence.
It returns 0 if n is 0 and 1 if n is 1. Otherwise, it returns the sum of the previous two numbers in the sequence.
Example: func(2) = 1 + 0 = 1

Question 2:

No, this is not an example of a divide-and-conquer algorithm. 
A divide-and-conquer algorithm is a recursive algorithm that breaks down a problem into two or more sub-problems of the same or related type
until these become simple enough to be solved directly. This function does not break down the problem into sub-problems. 
This function is rathered called a recursive function. A recursive function is a function that calls itself during its execution.

Question 3:

The time complexity of this function is O(2^n). This is because, in each recursive call, two more recursive calls are made
leading to an exponential growth in the number of function calls and computations.


Question 5:
With memoization, the time complexity of the function is O(n) because the function is called only once for each value of n.

'''





# Original Fibonacci function
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

#Question 4: 
def func_m(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = func_m(n-1, memo) + func_m(n-2, memo)
        return memo[n]


# Question 6:
    
import time
import matplotlib.pyplot as plt

n_values = list(range(36))
original_times = []
memoized_times = []

for n in n_values:
    start_time = time.time()
    func(n)
    end_time = time.time()
    original_times.append(end_time - start_time)

    start_time = time.time()
    func_m(n)
    end_time = time.time()
    memoized_times.append(end_time - start_time)

# Plotting the results
plt.plot(n_values, memoized_times, label='Memoized')
plt.xlabel('Input (n)')
plt.ylabel('Time (s)')
plt.title('Memoized Fibonacci Function Execution Time')
plt.legend()
plt.savefig('ex1.6.2.jpg')
plt.show()

plt.plot(n_values, original_times, label='Original')
plt.xlabel('Input (n)')
plt.ylabel('Time (s)')
plt.title('Original Fibonacci Function Execution Time')
plt.legend()
plt.savefig('ex1.6.1.jpg')
plt.show()

