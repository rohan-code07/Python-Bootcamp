try:
    file = open("Harry.txt", "r")
    for line in file:
        print(line)
    file.close() 
except FileNotFoundError:
    print("File not found")


with open("intro.txt", "r") as f:
    content = f.read()
    print(content)
#   It automatically closes the file, even if errors occur.



with open("intro.txt", "w") as info:
    info.write("I am persuing Btech in branch of CSAI")
    print(info)