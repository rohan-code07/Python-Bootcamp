# Typecasting in Python
# Typecasting is the process of converting one data type to another.

# Python provides built-in functions for typecasting:
# int(): Converts to integer.
# float(): Converts to float.
# str(): Converts to string.
# bool(): Converts to boolean.

a = 67       # Integer

b = "67"     # String

print(a)
print(type(a))

print(b)
print(type(b))

c = int(b)   # Converting str into int

print(c)
print(type(c))

d = 45.18     # Float

print(d)
print(type(d))

e = int(d)    # Converting float into int

print(e)
print(type(e))

f = float(e)    # Converting int into float

print(f)
print(type(f))

g = bool(f)    # Converting float into boolean

print(g)             #   0 ---> False   
print(type(g))       #   Any non-zero value ---> True