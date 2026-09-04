# TUPLES 

# Tuples are ordered but immutable collections (cannot be changed after creation).

tuples = (3, 5, 6)

print(tuples)
print(tuples[2])

single_element = (7, )     # Tuple with one element (comma required)


# Tuple Unpacking:

# Tuple unpacking is a feature in Python that lets you assign the elements of a tuple (or other iterable) to multiple variables in a single statement.

points = (3, 5, 9)
a, b, c = points

print(a)      # 3 is assigned to a
print(b)      # 5 is assigned to b
print(c)      # 9 is assigned to c


numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5


person = ("Alice", 35)
name, age = person

print(name)
print(age)

# for loops :

students = [("Rohan", 19),("Aman", 20),("Priya", 18)]

for student in students:
    print(student[0], student[1])

for name,age in students:
    if(age >= 18):
        print(name, age)


# Tuple Methods:

my_tuple = (1, 5, 7, 45, 32, 5)

print(my_tuple.count(5))     # Returns the number of times element appears in the tuple	

print(my_tuple.index(45))    # Returns the index of the first occurrence of element


# Why Use Tuples?

# Faster than lists (since they are immutable)
# Used as dictionary keys (since they are hashable)
# Safe from unintended modifications