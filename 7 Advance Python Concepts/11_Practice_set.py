# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".

def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello")
say_hello()


# Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

from time import time
def timer(func):
    def wrapper(n):
        t1 = time()
        result = func(n)
        t2 = time() 
        print(t2 - t1)
        return result
    return wrapper

@timer
def summed(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(summed(1000000))


# Create a class Employee with a private attribute _salary.
# Use @property to define a getter for salary.
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.


class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Warning")
        else:
            self._salary = value    
e = Employee(90000)
e.salary = 67000
print(e.salary)


# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."
# Call both methods without creating an objec

class MathUtils:
    operation = "This is a utility class for math operations."
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def description(cls):
        print(cls.operation)

# a = MathUtils()
# a.description()
# print(a.add(56, 6))

MathUtils.description()
print(MathUtils.add(56, 6))


# Create a class Book with attributes title and author.
# Implement __str__() so that printing the object displays "Title by Author".
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return len(self.title)
    
b1 = Book("Rich dad, Poor dad", "Ding dong")
b2 = Book("Personal knowledge", "Mahatma Gandhi")
print(b1)
print(len(b2))


# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a no. :"))
    if(num<0):
        raise NegativeNumberError("PLease enter positve value")
    result = 100/num
    print(f"Reult is : {result}")

except ValueError:
    print("input is not a number")
except ZeroDivisionError:
    print("don't try to divide by zero")
except NegativeNumberError as e:
    print(f"Error : {e}")


# Use map() to convert [1, 2, 3, 4, 5] into their cubes.

digit = [1, 2, 3, 4, 5]
cube = list(map(lambda x:x**3, digit))
print(cube)


# Use filter() to get only even numbers from [10, 11, 12, 13, 14].

def filtering(counting):
    if(counting%2==0):
        return True
    else:
        return False
counting = [10, 11, 12, 13, 14]
even = list(filter(filtering,counting))
# even = [x for x in counting if x%2==0]              Without using filter
# even = list(filter(lambda x : x%2==0,counting))     Using lambda
print(even)


# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].

from functools import reduce
def product(a, b):
    return a * b
element = [1, 2, 3, 4]
reduction = reduce(product, element)
print(reduction)


# Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.

while (a:=input("Enter : "))!="quit":
    print("Entered the wrong code") 


# Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters.

words = ["python", "rocks", "ai","water", "air"]
solution = [w for w in words if(x:=len(w))>=4]
print(solution)


# Write a function sum_all(*args) that accepts any number of integers and returns their sum.

def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum_all(1, 5, 3, 7, 8, 2))


# Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for

def print_details(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key} = {value}")

print_details(name="Alice", age=25, city="Delhi")


# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.

def cricket(*args, **kwargs):
    print(args, kwargs)

cricket(973, 269, king = "Kohli", God = "Sachin")


# Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x ,self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
first = Vector(4, 6)
second = Vector(3, 4)

Third = first + second
print(Third)


# Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing. 

while True:
    try:
        a = int(input("Enter a no. : "))
        b = int(input("Enter a no. : "))
        print(a/b)
    except ValueError:
        print("PLease enter the right values")
    except ZeroDivisionError:
        print("Don't divide by 0")
    except Exception as e:
        print("PLease don't use your 2 kodi ka brain")