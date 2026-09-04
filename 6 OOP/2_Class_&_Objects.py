# Class : Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name.

# Object : Specific instances created from the template(class). Eg. Form which contains the data.

class Employee:
    company = "HP"

    def get_salary(self):    # self is important here because self is a way to reference the object of the class which is being created
        return 34000
    
e1 = Employee()          # An Object of class Employee is created here
print(e1.get_salary())   # Employee e1's get_salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)

    

class Dog:

    color = "Black"      # Class attribute

    def __init__(self, name, breed, color):  # The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.
        self.name = name              # Instance attribute
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} say woff!"
    
my_dog = Dog("Tommy", "Bulldog", "White")
print(my_dog.name)
print(my_dog.bark())
print(my_dog.color)           # will always print instance attribute whenever present
print(Dog.color)              # this will print class attribute

another_dog = Dog("Cutie", "Pug", "Brown")
print(another_dog.breed)
print(another_dog.bark())
my_dog.__init__("Lucy", "Pitbull", "Grey")
print(my_dog.name)


# Object Introspection

print(dir(my_dog))


