# String Formatting and f-Strings


# String formatting is a powerful feature in Python that allows you to insert variables and expressions into strings in a structured way. Python provides multiple ways to format strings, including the older .format() method and the modern f-strings.


# Using .format() Method 

# The .format() method allows inserting values into placeholders {}:

name = input("Enter your name : ")
company = input("Enters company's name : ")

print("Hello {}, you are hired in {}".format(name,company))

# You can also specify positional and keyword arguments:

print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python
print("{name1} is {age} years old".format(name1="Bob", age=25))


# Strings (Formatted String Literals)

# Introduced in Python 3.6, f-strings are the most concise and readable way to format strings:

x = 23
y = 34

print(f"sum of {x} and {y} is : {x + y}")


# Formatting numbers

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")


# Padding and Alignment

text = "Python"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align


# Character Encoding

print(ord("A"))
print(chr(65))