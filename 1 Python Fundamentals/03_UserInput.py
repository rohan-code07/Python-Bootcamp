# Taking User Input in Python: 

# Using the input() Function
# The input() function allows you to take user input from the keyboard.
# By default, input() returns a string. You can convert it to other data types as needed


a = input("Enter your name : ")
print(a)

age = int(input("Enter your age : "))

print(type(age))


# f-strings are used to:

# Insert variables into a string easily
# Format values (like decimals, alignment, etc.)
# Write cleaner and more readable code

name = input("Enter your name : ")
gender = input("Enter your gender : ")

print(f"Hello myself {name}, and I am {gender}.")


# Sum of 2 numbers
no1 = int(input("Enter your first no. : "))
no2 = int(input("Enter your second no. : "))

sum = (no1 + no2)
print("Sum is : ", sum)


# Old Methods

# % Formatting (Oldest method)    [Similar to C]
name2 = "Rohan"
age2 = 20
print("My name is %s and I am %d years old" % (name2, age2))


# .format() Method
# This came after % formatting and is more flexible.
name3 = "Rohit"
age3 = 22
print("My name is {} and I am {} years old".format(name3, age3))

# With indexing
print("My name is {0} and I am {1}".format(name3, age3))

# With names
print("My name is {n} and I am {a}".format(n=name3, a=age3))