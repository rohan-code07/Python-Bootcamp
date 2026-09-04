# Write a function square(num) that returns the square of a given number. Test it with different numbers.

def square(a):
    return a**2

print(square(5))
print(square(7))

sqr = lambda x : x**2
print(sqr(3))


# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

def full_name(first, last):
    return f"{first} {last}"

print(full_name("Rohan", "Jangid"))


# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculate_area(length, width=10):
    return length * width

print(calculate_area(5,3))       # Outout : 15
print(calculate_area(5))         # Output : 50


# Write a lambda function that adds two numbers and test it.

add = lambda x, y : x + y
print(add(3,4))
print(add(6,7))


# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda z : z**2, numbers))
print(squared)

# Write a recursive function factorial(n) that returns the factorial of a number.

# For factorial(5):
# 5 × factorial(4)
# 4 × factorial(3)
# 3 × factorial(2)
# 2 × factorial(1)
# 1 → stops (base case)

def factorial(n):
    if(n == 0 or n == 1):
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(0))
print(factorial(5))
     

# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if(n == 0):
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    
print(sum_of_digits(0))
print(sum_of_digits(3456))

# Find the square root of 144

import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))


# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.

def increment():
    counter = 0
    counter += 1
    print(counter)
 
increment()
increment()
increment()
increment()


# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''Returns the multiple of 2 numbers'''
    return a * b

print(multiply.__doc__)
help(multiply)
print(multiply(3, 4))

# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if(b == 0):
        return "Cannot Divide by Zero"
    else:
        return a / b
    
print(safe_divide(12, 0))
print(safe_divide(12, 3))


# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

import Mymodule
print(Mymodule.is_even(6))
print(Mymodule.is_even(5))
