def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(5)
def say_hello(a):
    print(f"Hello {a}")

say_hello("Rohan")

# Chaining Multiple Decorators


def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
    
def exclaimed(func):
    def wrapper():
        return func() + "!!"
    return wrapper

@uppercase
@exclaimed

def function():
    return "hello"

print(function())

    
