def sum(*args):
    # arg will be a tuple of all the values passd to sum
    total = 0
    for item in args:
        total += item
    return total

print(sum(23, 5, 3, 7, 9))



def marks(**kwargs):
    # kwargs is a dictionary with all the key values pairs which wese passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
    
marks(Rohan=87, Rohit=90, Shresth=83, Shriya=80)



def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, 4, "Hello", Riya=94, Sarthak=78, )