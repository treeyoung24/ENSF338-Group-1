import cProfile
import timeit
def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]
test_function()
third_function()

# 1. A profiler is a module that provides an execution profile for a given program. This includes information such as where the most time is being spent, which method takes the most time, and which method is called the most.
# 2. While benchmarking is used to measure elapsed time for a code region of interest, profiling is used to measure relative system statistics.
# 3.
cProfile.run('test_function()')
cProfile.run('third_function()')
# 4. The execution time goes in the cumtime column. The cumtime column is the cumulative time spent in this and all subfunctions.