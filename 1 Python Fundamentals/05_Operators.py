a = 25

b = 2 

# Arthematic Operators

print("Arthematic Operators:")
print("a + b = ", a + b)        # Addition
print("a - b = ", a - b)        # Subtraction
print("a * b = ", a * b)        # Multiplication
print("a / b = ", a / b)        # Division
print("a ** b = ", a ** b)      # Power
print("a // b = ", a // b)      # Floor Division
print("a % b = ", a % b)        # Modulus    

#  Conditional Operators

print("\nConditional Operators:")
print( a > 4)
print( a < 4)
print( a >= 4)
print( a <= 4)
print( a == 4)      # is a is equal to 4?
print( a == 25)     # Is a is equal to 25? 
print( a != 4)      # Is a is not equal to 4?

# Logical Operators

print("\nLogical Operator:\n")
print("For and operator")

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("\nFor or operator")

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("\nnot operator")

print(not True)
print(not(False))

# Assignment Operator

print("\nAssignment Operator:")
c = 5
print(c)

c += 5
print(c)

c -= 2
print(c)

c *= 2
print(c)

c /= 2
print(c)

c **= 2
print(c)

c //= 5
print(c)

c %= 7
print(c)

# Membership Operators:

# in, not in.

print("\nMembership Operators:")
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True

# Identity Operators:

# is, is not.

print("\nIdentity Operators:")
x = 10
y = 10
print(x is y)  # Output: True
