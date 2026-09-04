# Defining Functions :

# Functions help in reusability and modularity in Python.

# Key Points:

# Defined using def keyword.
# Function name should be meaningful.
# Use return to send a value back.

def average(a, b, c):
    d = (a + b + c)/3
    print(d)

average(2, 7, 4)
average(4, 5, 6)


def average(a, b, c):
    d = (a + b + c)/3
    return d

avg1 = average(2, 7, 4)
avg2 = average(4, 5, 6)

print(avg1,avg2,sep="\n")


def greet(name):
    return f"Hello! {name}"

hi = greet("alice")
print(hi)