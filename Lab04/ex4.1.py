# 1. The best case complexity occurs if all the values in the list
# are less than 5. In this case, the if condition will not be satisfied.
# Therefore the time complexity will be O(n) as the outer for loop will run n times.

# The worst case complexity occurs if all the values in the list are greater than 5.
# In this case, the if condition will be satisfied for all the values in the list.
# Therefore the outer for loop will run n times and the inner for loop will run n times.
# So the time complexity will be O(n^2).

# The average case complexity occurs if half of the values in the list are less than 5 and
# half of the values in the list are greater than 5. In this case, the if condition will be
# satisfied for half of the values in the list. Therefore the outer for loop will run n times
# and the inner for loop will run n/2 times. So the time complexity will be O(n^2/2) which is
# equivalent to O(n^2).

# 2. The average, best, and worst case complexity are not the same.
def processdata(li):
    for i in range (len(li)):
        li[i] *= 2