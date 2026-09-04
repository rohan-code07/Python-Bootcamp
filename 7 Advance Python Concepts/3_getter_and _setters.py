class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    
    def set_first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e1 = Employee("Rohit Sharma", 56000)
e1.products = 6
print(e1.products)
print(e1.first_name())
print(e1.name)
e1.set_first_name("Rahul")
print(e1.name)



# INSTEAD OF THIS:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e1 = Employee("Rohit Sharma", 56000)
print(e1.first_name)
e1.first_name = "Rahul"
print(e1.name)



class Person:
    def __init__(self, name):
        self.name = name 
    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self, new_name):
        self.name  = new_name
    
p = Person("Ronaldo")
print(p.Name)
p.Name = "Messi"
print(p.Name)


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def Radius(self):
        return self.radius
    
    @property
    def area(self):
        return 3.14 * self.radius * self.radius
    
c = Circle(5)
print(c.Radius)
print(c.area)