import sys
import math

def do_stuff(): # sys.argv takes 3 inputs from the command line, converts them to float. It then determines 
                # if there are solutions of the quadratic formula and finds the solutions. 
    a = float(sys.argv[1]) 
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}') # the mistake was that the print statement didn't have 
                                                    # the same quotations at the beginning and end of the statement.
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')
              
do_stuff()