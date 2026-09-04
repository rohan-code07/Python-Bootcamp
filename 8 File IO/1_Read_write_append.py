# 'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.

f = open("intro.txt", "r")

content = f.read()

print(content)

f.close()



# 'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.

file = open("Harry.txt", "w")

string = '''Harry is my python tutor
he is brilliant teacher
I an studying from his course of python
'''
file.write(string)
file.close()


# 'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.

file1 = open("Harry.txt", "a")

string = '''His channel name is Code With Harry 
He also teaches many languages'''

file1.write(string)

file1.close()