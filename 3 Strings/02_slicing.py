# String Slicing

# Slicing allows you to extract a portion of a string using the syntax string[start:stop:step].

name = "Rohan123456789"

print(name[1:5])        # goes from 1 to 5-1 ie 4

print(name[-10:-3])     # goes from -10 to -3-1 ie -4

print(name[-13:7])      # goes from -13 to 7-1 ie 6

print(name[2:])         # Replace the second empty number with length - 1  # name[2:14]

print(name[:9])         # Replace the first empty no. with 0    # name[0:9]

# print(name[1 : 5 : n])  skips n - 1 characters

print(name[2:13:1])  # skips 0 characters
print(name[2:13:2])  # skips 1 characters
