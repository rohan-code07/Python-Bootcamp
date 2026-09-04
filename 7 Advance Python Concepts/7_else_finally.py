try: 
    a = int(input("Enter a no : "))
    b = a /10

except Exception as e:
    print("Please enter right values")

else:           # Gets executed when there is no error in try block
    print(b)

finally:        # This is always executed
    print("Program is successfully printed")


def divide(x, y):
    try:
        c = x / y
        return c
    
    except Exception as e:
        return f'Error : {e}'        
    
    finally:             # This is always executed no matter if try completely executes or not
        print("This code is executed")
        
x = int(input("Enter a no : "))
y = int(input("Enter a no : "))
print(divide(x, y))



