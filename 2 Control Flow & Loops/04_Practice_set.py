# If-Else Conditional Statements :


# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
 
a = int(input("Enter an Interger :"))

if a>0:
    print("Postive")
elif a==0:
    print("Zero")
else:
    print("Negative")


# Create a program that checks if a person is eligible to vote (age >= 18).

age = int(input("Enter your age : "))

if age >= 18:
    print("Eligible to vote")
elif age ==18:
    print("Apply for voter id")
else:
    print("Minorrrrrrrrrr")


# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

no = int(input("Enter a no : "))

if no % 2 == 0:
    print("Even")
else:
    print("odd")


# Match Case Statements :

# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

day = int(input("Enter no between 1 to 7 : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

num1 = int(input(("Enter first no : ")))
num2 = int(input(("Enter second no : ")))

operation = input("Choose operation :")

match operation:
    case "+" :
        print(num1 + num2)
    case "-" :
        print(num1 - num2)
    case "*" :
        print(num1 * num2)
    case "/" :
        print(num1 / num2)
 

# For Loops


# Calculate the sum of all numbers from 1 to 100 using a for loop.

sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# Print the following pattern using a for loop:

for i in range(1, 7):
    print("*"*i)


# While Loops


# Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "rohan"
entered_pass = input("Enter your password : ")

while entered_pass != password:
    entered_pass = input("Try again and Enter password : ")

print("Successful")


# Use a while loop and str slincing to reverse a given number (e.g., 123 → 321).

number = int(input("Enter a no :"))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print(("Reversed no. is : ", reverse))

#str slicing
aaaahhhh = 1234
print("Reversed no is : ", int(str(aaaahhhh)[::-1]))       # It is converted into str as slicing does not work on int after that it is converted back to int  [start:stop:step(-1 means backward)]


# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
 
for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)