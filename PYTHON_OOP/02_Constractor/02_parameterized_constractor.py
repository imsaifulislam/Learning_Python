""" class Employee:
    
    # parameterized Constractor
    def __init__(self,name,age):
        self.name = name #instance Variable
        print(self.name, "Created")
        self.age = age #instance Variable
        print(self.age, "Years Old")
        
emp1=Employee("Jone","29")
emp2=Employee("David","30")
 """
""" 
__init__ :- 
"""


class Employee:

    # parameterized Constractor
    def __init__(self, name, age):
        self.name = name  # instance Variable
        self.age = age  # instance Variable

    def display(self):
        print("Name is:", self.name, "Age is", self.age)


emp1 = Employee("Jone", 29)
emp2 = Employee("David", 30)


emp1.display()
emp2.display()
