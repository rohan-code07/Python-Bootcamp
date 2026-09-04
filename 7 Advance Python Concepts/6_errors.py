while True:
    try :
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("The answer is :", a / b )

    except ValueError:
        print("please do not perform bad typecasts")
    except ZeroDivisionError:
        print("please don't divide by 0")
    except Exception as e:
        print("Some Error Occured!!", e)



# # Raising Exceptions (raise)


# a = int(input("Enter 1st no. : "))
# b = int(input("Enter 2nd no. : "))

# if b == 0:
#     raise ValueError("Please don't divide by zero")

# print("The answer is :", a / b )  



# class InvalidAgeError(Exception):
#     def __init__(self, message = "Your age should be more or equal to 18"):
#         self.message = message
#         super().__init__(self.message)

# def verify_age(age):
#     if age < 18:
#         raise InvalidAgeError()
#     return "You can drive"
# try: 
#     print(verify_age(12))
# except InvalidAgeError as e:
#     print(f"Error : {e}")