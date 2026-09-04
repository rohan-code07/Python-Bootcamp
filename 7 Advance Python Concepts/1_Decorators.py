def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("The function is executed")
    return wrapper

@decorator

def say_hello():
    print("Hello World")

# f = decorator(say_hello)
# f()                        instead of this

say_hello() 
'''
f will look like this
def f():
    print("I am about to execute a function...")
    print("Hello World")
    print("The function is executed")
'''