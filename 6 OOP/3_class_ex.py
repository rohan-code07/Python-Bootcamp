class rectangle:

    def __init__(self, length, breadth):
        print(length * breadth)

a = rectangle(5, 6)
a.__init__
b = rectangle(4, 5)
b.__init__       


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def display(self):
        print(f"Student name : {self.name}")
        print(f"Student age : {self.age}")

s1 = Student("rohan", 19)
s1.display()


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def intro(self):
        print(f"introducing {self.brand} {self.model} \nLaunched in {self.year}")

c1 = Car("Audi", "m4", 2022)
c2 = Car("Rolls Royce", "ghost", 2020)
c3 = Car("Ferrari", "X3Z", 2019)

print(c1.model)
print(c3.year)
c2.intro()


class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def damage(self, amount):
        self.health -= amount
    
    def heal(self, amount):
        self.health += amount

p1 = Player("Virat", 180)
p1.damage(50)
p1.heal(30)
print(p1.health)


class Book:

    def __init__(self, title, author, price):
        self.title  = title
        self.author = author
        self.price  = price     

    def apply_discount(self, percent):
        self.price -= (self.price * percent / 100)

b1 = Book("How to be an Ideal Man", "Virat Kohli", 9230)
b1.apply_discount(10)
print(b1.price)