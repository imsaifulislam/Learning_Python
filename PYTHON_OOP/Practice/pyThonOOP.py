""" 
    Python OOP
    
    |> Class
    |> Constractor
        |-< Instance Variable
        |-< Instance Methods
"""

class Student:
    
    # def __init__(self,name,id):
    def __init__(self):
        self.Name = ""
        self.Id = ""
        
    def viewInfo(self):
        print(f"Student Name : {self.Name} & Student Id: {self.Id}")

# =====================================================================

# |> Creating Object
stu1 = Student()
stu1.viewInfo()

stu2= Student()
stu2.Name = "ShantO"
stu2.Id = 34
stu2.viewInfo()