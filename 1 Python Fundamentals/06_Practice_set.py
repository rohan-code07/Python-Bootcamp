# Create variables to store: Print all of them in one line.

name = "Rohan Jangid"
age = 18
Height = "5'11"
Student = True

print(f"my name is {name}\nI am {age} years old\nI am of {Height}\nI am student : {Student}")

print("Name of the student is :" + name + "\nHe is " + str(age) + " Years old " "\nHis height is : " + str(Height) + "\nStudent : " + str(Student))


# Convert it into an integer.Add 10 to it.Print the result.

num = "15"
print(int(num) + 10)


# WAP to ask the user for their favorite food.

food = input("What is is your fav food : ")

print(f"Wow! I also like {food}.")
print("Wow! I also like " + food)

# Takes two numbers as input from the user.Prints their:Sum,Difference,Product,Quotient.

a = int(input("Enter first no : "))

b = int(input("Enter second no : "))

print("sum is :", a + b)
print("Diffrrence is :", a - b)
print("Product is :", a * b)
print("Quotient is :", a % b)


# Takes an integer as input from the user.Prints the square and cube of that number.

c = int(input("Enter a no :"))

print("square : ", c**2)
print("cube is : ", c**3)