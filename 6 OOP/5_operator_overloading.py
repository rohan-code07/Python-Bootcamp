class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def add(self, p):                                 # OR   def __add__(self, p):
        return Point((self.x + p.x), (self.y  + p.y))
    def Print(self):
        print(f"X is {self.x} and Y is {self.y} ")
    
p1 = Point(2, 3)  
p2 = Point(4, 5)

p = p1.add(p2)          # object.method(argument)     # THEN p1 + p2
p.Print()


# Operator Overloading

class operator:
    def __init__(self, x, y):
        self.x = x
        self.y =y
    
    def __add__(self, b):
        return (self.x + b.x), (self.y + b.y)
    def __sub__(self, b):
        return (self.x - b.x), (self.y - b.y)
    def __mul__(self, b):
        return (self.x * b.x), (self.x * b.y)
    def __truediv__(self, b):
        return (self.x / b.x), (self.y / b.y)   
    def __eq__(self, b):
        return (self.x == b.x), (self.y == b.y) 
    def __ne__(self, b):
        return (self.x != b.x), (self.y != b.y) 
    def __lt__(self, b):
        return (self.x < b.x), (self.y < b.y) 
    def __gt__(self, b):
        return (self.x > b.x), (self.y > b.y)
    def __le__(self, b):
        return (self.x <= b.x), (self.y <= b.y) 
    def __ge__(self, b):
        return (self.x >= b.x), (self.y >= b.y) 
    
a = operator(6, 7)
b = operator(3, 4)

c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)
g = a == b
print(g)
h = a != b
print(h)
i = a < b
print(i)
j = a > b
print(j)
k = a <= b
print(k)
l = a >= b