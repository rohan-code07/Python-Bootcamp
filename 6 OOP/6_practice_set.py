# Create a class Car with a method drive() that prints "Car is moving".Create an object of Car and call drive().

class Car:
    def drive(self):
        print(f"Car is moving")
        
c = Car()
c.drive()


# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Rohit", 19)
print(p.name)
print(p.age)


# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some Sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

b = Dog()    
b.sound()