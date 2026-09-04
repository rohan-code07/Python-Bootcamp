# Recursion 

# A function calling itself to solve a problem.


'''
fibonacci sequence : 0 1 1 2 3 5 8 13
             index : 0 1 2 3 4 5 6 7

             
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(n) = fib(n-2) + fib(n-1)

'''

def fib(n):
    # Base case of RECURSION
    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)

print(fib(6))

fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(5)
0 + 1 + 1 + fib(0) + fib(1) + fib(5)
0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 
8


# Important Notes:

# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.

