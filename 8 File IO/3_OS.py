import os

print(os.listdir("."))                # List files and directories in a directory 
#                                       "." represents current directory
print(os.getcwd())                    # Get the current working directory

print(os.path.exists("3 Strings"))    # Check if a file or directory exists

# os.remove("sample.txt")             # Remove a file

# os.rmdir("dir")                     # removes empty directory

# os.rename("Harry.txt", "Tutor.txt") #  Rename a file or directory

# os.mkdir("Sample_directory")        # Create a new directory

os.chdir("6 OOP")             # It changes the current working directory of your Python program.  
print(os.getcwd())
 
print(os.name)                        # tells you which operating system you're using. nt

# os.system("mspaint")                # Open Paint
# os.system("calc")                   # Open Calculator
# os.system("notepad")                # Open Notepad

# os.system("cls")                    # Clear the terminal

os.system("dir")                      # Show all files

os.system("cd")                       # Display the current directory

# os.system("pause")                  # Pause the program

path = os.path.join("intro.txt", "Tutor.txt")

print(path)
