# Concatenate two strings: "Hello" and "World" with a space in between.

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)
print(str1,str2)



# Given text = "Python Programming", do the following:

# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string

text = "Python Programming"

print(text[0:7])
print(text[-6:])
print(text[::2])

# Reverse the string text using slicing.

print(text[::-1])


# Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Check if the string is alphanumeric

string = "  i love python programming "

print(string.strip())
print(string.title())
print(string.count("o"))
print(string.isalnum())


# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
# Do the same using f-strings.

name = 'john'
age = 25

print("My name is {} and I am {} years old.".format(name,age))
print(f"My name is {name} and I am {age} years old.")


# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it

sentence = "Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.find("Python"))
print(sentence.index("Python"))
print(sentence.upper())


# Write a program that counts how many vowels are in a given string.

sentence = ("Once I am done, I will be gone, you won't see me for a while")
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence.lower():
    if (char in vowels):
        sum+=1

print("No. of vowels are :",sum)  


# Take a user input string and check if it is a palindrome (same forwards and backwards).

str = "madam"

if (str == str[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")