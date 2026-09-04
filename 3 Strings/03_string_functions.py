
# Strings are immutable, meaning they cannot be changed after creation.

# Strings Functions

# Changing Case

string = "hello world"
print(len(string))                  # Length of the string
print(string.endswith("rld"))       # give result on true or false
print(string.startswith("hel"))     # give result on true or false
print(string.upper())               # Converts to UPPERCASE
print(string.lower())               # Converts to lowercase
print(string.capitalize())          # make the first character have uppercase & the rest lowercase.
print(string.title())               # first word capital of each letter
print(string.swapcase())            # Swaps upper ↔ lower case

# Removing Whitespace

space = " \nhello world "
print(space.strip())         # Remove whitespace
print(space.lstrip())        # Remove whitespace from left
print(space.rstrip())        # Remove whitespace from right

# Finding, Replacing and counting

text = "python is fun , fun and fun"
print(text.find("fun"))               # Returns index, -1 if not found
print(text.rfind("fun"))              # Finds from right
print(text.index("fun"))              # Returns index, error if not found 
print(text.rindex("fun"))             # Index from right
print(text.replace("fun", "awesome")) # for replacing the word
print(text.count("fun"))              # Counts occurrences

# Splitting and Joining

fruits = "Apple, Pinapple, Mango, Banana"
print(fruits.split(","))
print(",".join(['Apple', ' Pinapple', ' Mango', ' Banana']))


# Checking String Properties 

name = "Python123"
print(name.isalpha())  # check the string is only alphabet or not         # False
print(name.isdigit())  # check the string is only digit(int) or not       # False
print(name.isalnum())  # check the string is alphabet and digit or not    # True
print(name.isspace())  # Return True if the string is a whitespace string, False otherwise.