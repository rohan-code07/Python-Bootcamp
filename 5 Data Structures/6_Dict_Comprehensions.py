table_of_5 = {i : 5*i for i in range(1,11)}
print(table_of_5)


square = {i : i**2 for i in range(1,11)}
print(square)

cube = {x : x**3 for x in range(1,6)}
print(cube)


# Create a dictionary from a list of names

names = ["Rohan", "Aman", "Priya"]
length = {name : len(name) for name in names}
print(length)


# Convert all keys to uppercase

d = {"a": 1, "b": 2, "c": 3}
d1 = {key.upper() : value for key, value in d.items()}
print(d1)


# Create a dictionary of even numbers only

even = {i : i**2 for i in range(1, 11) if(i%2==0)}
print(even)


# Create a dictionary from two lists

names = ["Rohan", "Aman", "Priya"]
ages = [19, 20, 18]

dict = {name : age for name, age in zip(names,ages)} # zip() combines elements from multiple iterables position by position.
print(dict)

# Keep only students with marks ≥ 50

marks = {"Rohan": 75, "Aman": 40, "Priya": 60, "Raj": 35}

passed = {name : mark for name,mark in marks.items() if (mark>=50)}
print(passed)


# Reverse keys and values

d = {"a": 1,"b": 2,"c": 3}
d2 = {value : key for key, value in d.items()}
print(d2)

# Create a character frequency dictionary

text = "hello"
hello = {char : text.count(char) for char in text}
print(hello)

# Map numbers to "Even" or "Odd"

no = {num : "odd" if(num %2 != 0) else("even") for num in range(1,6)}
print(no)

# Dictionary of ASCII Values

letters = ["a", "b", "c", "d"]

let = {letter : ord(letter) for letter in letters}
print(let)

# tring to ASCII Dictionary

text = "python"

ascii = {letter : ord(letter) for letter in text}
print(ascii)

# Dictionary with Growing Lists

list = {num : [i for i in (1, num+1)] for num in range (1,5)}
print(list)


# When to Use Each Data Structure? 
 
# Data Structure	        Features           	    Best For
#     List          	Ordered, Mutable	    Storing sequences, dynamic data
#    Tuple              Ordered, Immutable     	Fixed collections, dictionary keys
#     Set	             Unordered, Unique	    Removing duplicates, set operations
#  Dictionary	         Key-Value Pair         Fast lookups, structured data