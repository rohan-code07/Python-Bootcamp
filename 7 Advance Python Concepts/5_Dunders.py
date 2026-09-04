# Magic methods, also called dunder (double underscore) methods, are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__, __add__). 


class string:
    def __init__(self,name):
        self.name = name 

    def __str__(self):                   #  User-friendly
        return f"{self.name}"
    
    def __repr__(self):                  # Unambiguous, for debugging
        return f"Name : {self.name}"
    
    def __len__(self):
        return len(self.name)
    
    def __getitem__(self, index):
        return self.name[index]
    
    def __contains__(self, char):
        return char in self.name
    
    
st = string("rohan")
print(st.name)
print(str(st))    
print(repr(st)) 
print(len(st))
print(st[1])
print("h" in st)



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
    def __floordiv__(self, b):
        return (self.x // b.x), (self.y // b.y) 
    def __pow__(self, b):
        return (self.x ** b.x), (self.y ** b.y) 
    def __mod__(self, b):
        return (self.x %b.x), (self.y % b.y) 
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
g = a // b
print(g)
h = a ** b
print(h)
i = a % b
print(i)
j = a == b
print(j)
k = a != b
print(k)
l = a < b
print(l)
m = a > b
print(m)
n = a <= b
print(n)
o = a >= b
print(o)