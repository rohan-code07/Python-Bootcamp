# If-Else Conditional 

age = int(input("Enter your age : "))

if(age>18):
    print("You can drive")
elif(age==18):
    print("Let's Schedule an interview")
else:
    print("You cannot drive")


# Match Case Statements

a = int(input("Enter a lucky no.:"))

match a :
    case 1:
        print("You won a bike")
    case 2:
        print("You won 3$")
    case 3:
        print("You won a buds")
    case _:
        print("Better luck next time")
