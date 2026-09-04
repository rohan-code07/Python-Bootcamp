# Lambda Functions

# Lambda functions are anonymous, inline functions.

square = lambda x : x * x

print(square(4))

cube = lambda x : x * x * x

print(cube(3))

sum = lambda x, y, z : x + y + z

print(sum(7,8,9))

text = lambda name : f"Hello ! {name}"

print(text("Rohan"))


# map()

# map() is a built-in function in Python used to apply a function to every item in a list (or any iterable).
# map() does NOT return a list directly.It returns a map object (iterator)

# map(function, iterable)
# function → what you want to do
# iterable → list/tuple etc.

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


def sqr(a):
    return a**2

digit = [1, 2, 3, 4]

print(list(map(sqr, digit)))

