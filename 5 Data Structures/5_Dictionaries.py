# DICTIONARIES

# Dictionaries store key-value pairs and allow fast lookups.

marks = { "Harry": 56, "Rahul": 78, "Neha": 76}

print(marks, type(marks))

print(marks["Harry"])

marks["Neha"] = 80     # Updating
print(marks)

marks["lily"] = 68     # adding
print(marks)


# DICTIONARY METHODS

student = {"name": "Rohit", "age": 19, "cgpa": 8.23, "branch" : "csai"}

print(student.keys())       # dict_keys(['name', 'age', 'cgpa', 'branch'])

print(student.values())     # dict_values(['Rohit', 19, 8.23, 'csai'])

print(student.items())      # dict_items([('name', 'Rohit'), ('age', 19), ('cgpa', 8.23), ('branch', 'csai')])

print(student.get("name"))  # returns the value, if key doesn't exist it gives none unlike student[] which gives error

student.update({"name": "harry", "age": 20, "city": "kota"})
print(student)              # Add or modify entries.  update() can handle multiple keys at once:

new = {"year":2, "course": "B.tech"}

student.update(new)         # use update() when copying or merging multiple key-value pairs.
print(student) 

poped = student.pop("age")  # Remove a key and return its value.
print(poped)
print(student)

print(student.popitem())    # Removes the last inserted key-value pair.
print(student)

dict = {}
key = ['name', 'age', 'height']   # Creates a new dictionary from a list of keys.
d = dict.fromkeys(key, 0)         # dict.fromkeys(keys, value)
print(d)

print(d.setdefault("name", "rohan"))     # If the key exists it returns its current value. It does not overwrite existing value
print(d.setdefault("class", 12))         # If it doesn't exist it create it with default value
                                         # dictionary.setdefault(key, default_value)
                                         
student.clear()           # Removes everthing 
print(student)