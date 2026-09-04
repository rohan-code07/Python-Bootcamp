#  Variable Scope : 

# In Python, variables have scope (where they can be accessed) and lifetime (how long they exist). Variables are created when a function is called and destroyed when it returns. Understanding scope helps avoid unintended errors and improves code organization.

# Types of Scope in Python: 

# Local Scope (inside a function) – Variables declared inside a function are accessible only within that function.
# Global Scope (accessible everywhere) – Variables declared outside any function can be used throughout the program.


x = 10              # Global Variable

def function():
    x = 5           # Local Variable, It creates a local variable called x which is destroyed after this function returns
    print(x)        # Output : 5

function()
print(x)            # Output : 10 (global x remains unchanged)


# Using the global Keyword : 

# To modify a global variable inside a function, use the global keyword:

a = 10             # Global Variable
def num():
    global a     # Modifies the global a
    a = 7        # This will refer to global variable and not create a local variable
    return a
num()
print(a)           # Output : 7

# This allows functions to change global variables, but excessive use of global is discouraged as it can make debugging harder.


# Docstrings - Writing Function Documentation: 

# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute.


def sum(a, b):
    '''Returns the sum of two numbers'''
    return a + b

add = sum(5, 6)

print(sum.__doc__)
print(add)

def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add.__doc__)


# Summary: 

# Functions help in reusability and modularity.
# Functions can take arguments and return values.
# Lambda functions are short, inline functions.
# Recursion is a technique where a function calls itself.
# Modules help in organizing code and using external libraries.
# Scope and lifetime of variables decide their accessibility.
# Docstrings are used to document functions, classes, and modules.