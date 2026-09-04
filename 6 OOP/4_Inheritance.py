# Inheritance: Building Upon Existing Classes

# Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes and methods) from its parent class (or superclass). This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code.


class Animal:         # Parent class (superclass)

    location = "Australia"

    def __init__(self, name, color):
        self.name = name
        self.color = color 

    def speak(self):
        print("speaking now.....")

class Dog(Animal):        # Dog inherits from Animal (Dog is a subclass of Animal)

    def speak(self):      # overriding
        super().speak()   # We are using the speak function of the parent class
        print("Woof")

class Cat(Animal):        # Cat also inherits from Animal

    def speak(self):
        print("Meow")


d1 = Dog("Fluffy", "White")
c1 = Cat("Squeezy", "Brown")
print(d1.name)
print(c1.color)
print(c1.location)
d1.speak()


# Method Overriding: 

# Method overriding is how polymorphism is achieved in inheritance. When a child class defines a method with the same name as a method in its parent class, the child's version overrides the parent's version for objects of the child class. This allows specialized behavior in subclasses. The parent class's method is still available (using super()), but when you call the method on a child class object, the child's version is executed.


# super(): Inside a child class, super() lets you call methods from the parent class. This is useful when you want to extend the parent's behavior instead of completely replacing it. It's especially important when initializing the parent class's part of a child object.