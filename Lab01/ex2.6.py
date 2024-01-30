import timeit

def pow2(n):
    return 2 ** n

# Timing the execution of 10000 instances of pow2(10000)
execution_time = timeit.timeit(lambda: pow2(10000), number=10000)

print(f"Execution time for pow2(10000) 10000 times: {execution_time} seconds")

# Computing pow2(n) for n up to 1000 using a for loop
def pow2_for_loop(n):
    result = []
    for i in range(n+1):
        result.append(2 ** i)
    return result

# Computing pow2(n) for n up to 1000 using list comprehension
def pow2_list_comprehension(n):
    return [2 ** i for i in range(n+1)]

# Timing the execution of 1000 instances of pow2_for_loop and pow2_list_comprehension
for_loop_time = timeit.timeit(lambda: pow2_for_loop(1000), number=1000)
list_comprehension_time = timeit.timeit(lambda: pow2_list_comprehension(1000), number=1000)

print(f"Execution time for pow2_for_loop(1000) 1000 times: {for_loop_time} seconds")
print(f"Execution time for pow2_list_comprehension(1000) 1000 times: {list_comprehension_time} seconds")
