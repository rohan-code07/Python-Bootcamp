# Types of Arguments:

# Positional Arguments

def add(a, b):             # a and b are parameters
    return a + b

print(add(5,4))            # 5 and 4 are arguments


# Default Arguments

def plus(a, b, add = 0):
    return a + b + add

print(plus(5, 6, 7))     # 7 is overwriting in add parameter

def text(name = "Rohan"):
    return f"Hello! How are you {name}"

print(text())


# Keyword Arguments

def multiply(a, b, c):
    return a*b*c

result = multiply(b=5, c=3, a=7)
print(result)