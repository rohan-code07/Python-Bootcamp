def very_slow():
    print("Hello Batataaa.....")
    print("Hello Batataaa.....")
    print("Hello Batataaa.....")
    print("Hello Batataaa.....")
    print("Hello Batataaa.....")
    return 7

if((a:= very_slow())>10):
    print(a)
else:
    print("It is not greater than 10")




# Without Walrus operator

secret = input("Enter a secret code: ")
while(secret != "Potty"):
    print("Secret code is not detected")
    secret = input("Enter a secret code: ")


# With Walrus operator

while((secret:=input("Enter a secret code: "))!= "Potty"):
    print("Secret code is not detected")
