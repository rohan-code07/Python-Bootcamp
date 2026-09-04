# For Loops:

# For loops are used to iterate over a sequence (e.g., list, string, range).
# They e   xecute a block of code repeatedly for each item in the sequence.


# Using range():
# The range() function generates a sequence of numbers.
# range(start, stop, step)
# Start is included and stop is excluded

for i in range(1, 6):  # In this case range function goes from 1 to (6-1) i.e 5
    print(i)

# Table

for i in range(1, 11):
    print("5 *", i, "=", 5*i)
    print("5 * "+ str(i)+ " = "+ str(5*i))

# While Loops:

# While loops execute a block of code as long as a condition is True.
# They are useful when the number of iterations is not known in advance.

i = 1
while i<6:
    print(i)
    i += 1 

# Table
i = 1
while i<11:
    print("7 *", i, "=", 7*i)
    i += 1


    
# Upside down table
i = 10
while i>0:
    print("7 *", i, "=", 7*i)
    i -= 1


# Infinite Loops: 
# Be careful to avoid infinite loops by ensuring the condition eventually becomes False.
# Ex: 

# i = 1
# while True:
#     print(i)
#     i = i + 1
 