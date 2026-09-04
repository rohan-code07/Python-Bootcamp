# Create a list fruits = ["apple", "banana", "cherry"].
# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.

fruits = ["apple", "banana", "cherry"]

print(fruits[0])
fruits[1] = "orange"
print(len(fruits))
print(fruits) 


# Create a list of numbers from 1 to 10.
# Print the first three numbers using slicing.
# Print the last three numbers using slicing.

numbers = [i for i in range(1,11)]
print(numbers[:3]) 
print(numbers[-3:])


# Start with numbers = [5, 2, 9, 1, 7] and do the following:
# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.

number = [5, 2, 9, 1, 7]

number.sort()
number.append(10)
number.remove(2)
print(number)


# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)


# Create a tuple coordinates = (10, 20) and print both elements.

coordinates = (10, 20)

print(coordinates[0],coordinates[1])
# coordinates[0] = 50            # not possible 

colist = list(coordinates)
colist[0] = 50
coordinates = tuple(colist)
print(coordinates)


# Create a set Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)and print it. (What happens to duplicate 3?)
# Add 5 to the set, remove 2, and check if 4 is in the set.
 
my_set = {1, 2, 3, 3, 4}
print(my_set)                   # no duplications

my_set.add(5)
my_set.remove(2)
print(4 in my_set)
print(my_set)


# Create two sets: a = {1, 2, 3}, b = {3, 4, 5}. Find their: Union, Intersection, Difference (a - b)

a = {1, 2, 3} 
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)


# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".

student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
print(student.get("name"))
student.update({"grade": "A+", "city" : "kota"})      # student["grade"] = "A+", student["city"] = "kota"
print(student)


# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

friends = {"Rohan" : 9698699393, "Shresth" : 9867564321, "Rohit" : 7563421452}

print(friends.keys())
print(friends.values())
print(friends.items())

for key, value in friends.items():
    print(key, value)


# Write a program that takes a list of numbers and removes all duplicates using a set.

# for user input
numbers = list(map(int, input("Enter a no :").split()))
unique_no = list(set(numbers))
print(unique_no)

# for defined list
no = [1, 2, 3, 3, 4, 3, 4, 5, 6]
no1 = list(set(no))
print(no1)


# Given a dictionary of products and their prices, find the product with the highest price.

products = {
    "Laptop": 50000,
    "Phone": 30000,
    "Tablet": 20000,
    "Watch": 10000
}

#       max(iterable, key=function)
price = max(products, key=products.get) # - products.get("Laptop")  # 50000
#                            ^------------  products.get("Phone")   # 30000 
#                             ------------  products.get("Tablet")  # 20000 
print(price, products[price])


# Find the item whose function result is largest.

words = ["cat", "elephant", "dog"]
print(max(words, key = len))


# Create a dictionary from two lists

devices = {"Laptop","Phone","Tablet","Watch"}
amounts = [55000, 34000, 54000, 12000]

shop = {device : amount for device,amount in zip(devices,amounts)}
print(shop)


# Write a program that merges two dictionaries into one.


dict1 = {"name": "Rohan", "age": 19}
dict2 = {"city": "Jaipur", "height": 180}

dict1.update(dict2)
print(dict1)
