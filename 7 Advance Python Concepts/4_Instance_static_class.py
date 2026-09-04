# Instance Methods: These are the most common type of method. They operate on instances of the class (objects) and have access to the instance's data through the self parameter.

# Class Methods: These methods are bound to the class itself, not to any particular instance. They have access to class-level attributes and can be used to modify the class state. They receive the class itself (conventionally named cls) as the first argument.

# Static Methods: These methods are associated with the class, but they don't have access to either the instance (self) or the class (cls). They are essentially regular functions that are logically grouped within a class for organizational purposes.


class Employee:
    Company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance Method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a, b):
        return a + b
    
    @classmethod
    def print_company(cls):
        print(cls.Company)

    @classmethod
    def change_company(cls, new_company):
        cls.Company = new_company

e = Employee("John", 35000)
e.print_info()                 # Instance Method
print(e.sum(25, 32))           # Static Method
e.print_company()              # Class Method
e.change_company("Lenovo")
e.print_company()              # You can do this instead print(Employee.Company)


