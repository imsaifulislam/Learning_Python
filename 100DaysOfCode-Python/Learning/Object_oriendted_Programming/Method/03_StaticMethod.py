# Use for Extra Funsonality

class Employee:

    org_name = "Meta"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def detail():
        print("This is and Employee Class")

    @staticmethod
    def sum(a, b):
        print(a+b)


Employee.detail()
Employee.sum(10,20)


# -----------------------------------

class MyClass:
    
    def method(self):
        print(self, "Instance Method Called")
    
    @classmethod
    def Class_method(cls):
        print(cls, "Class Method Called")
    
    @staticmethod
    def Static_method():
        print("Static Method Caleed")

MyClass()