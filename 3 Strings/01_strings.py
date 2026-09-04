# STRINGS

# Strings are one of the most fundamental data types in Python. A string is a sequence of characters enclosed within either single quotes ('), double quotes ("), or triple quotes (''' or """).

string = '''Hello 
my 
name
is 
rohan'''


# String Indexing

# Each character in a string has a unique index, starting from 0 for the first character and -1 for the last character.

name = 'Rohan'

# name = R  o  h  a  n
#        0  1  2  3  4
#       -5 -4 -3 -2 -1

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[-1])
print(name[-2])
print(name[-3])  
print(name[-4])     # name[-4+5]   indexing + string length
print(name[-5])