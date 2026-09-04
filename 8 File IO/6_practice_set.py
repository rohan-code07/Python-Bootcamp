# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.

with open("notes.txt", "w") as f:
    f.write("Learning Python is fun!")


# Open notes.txt, read its content, and print it to the console.

with open("notes.txt", "r") as file:
    print(file.read())


# Write a program that writes three lines of text to a file tasks.txt.

with open("tasks.txt", "w") as f:
    f.write('''Jaldi utho
Brush kro
dudh pio''')


# Open tasks.txt in append mode and add a new line "Task Completed!".

with open("tasks.txt", "a") as f:
    f.write("\nTask Completed")


# Read the file and print all lines as a list using readlines().

with open("tasks.txt", "r") as f:
    for line in f.readlines():
        print(line)

# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder

import os 
print(os.getcwd())
print(os.listdir())
# os.mkdir("my_folder")
 

# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)

import shutil
# shutil.copy("notes.txt", "my_folder/info.txt")
# shutil.move("notes.txt", "my_folder")
# os.remove("delete_this_file.txt")

# Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

# import sys 

# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())
    
# if __name__ == "__main__":
#     filename = sys.argv[1]
#     num_lines = count_lines(filename)
#     print(f"There are {num_lines} lines in {filename}")


# Write a command-line utility search_word.py that takes two arguments:
# A filename
# A word to search and prints how many times the word appears in the file.

# import sys

# def search_word(string, word):
#     return string.count(word)

# if __name__ == '__main__':
#     filename = sys.argv[1]
#     word = sys.argv[2]
#     with open(filename) as f:
#         string = f.read()
#         n = search_word(string, word)
#         print(f"There are {n} occurances of {word} in the file")


# Write a program that reads a file and creates another file with all words converted to uppercase.

with open("tasks.txt", "r") as f:
    content = f.read()

upper_case = content.upper()

with open("tasks.txt", "w") as file:
    file.write(upper_case)


# Create a script that deletes all .tmp files from the current directory using os and os.remove().

files = os.listdir()

for file in files:
    if file.endswith(".tmp"):
        os.remove(file)
        print(f"{file} is deleted") 