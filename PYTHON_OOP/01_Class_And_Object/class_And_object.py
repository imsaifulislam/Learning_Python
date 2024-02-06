class student: #class / Design / BlurPrint
    def __init__(self,Name,Id): #constactor
        print("An Object is created!")
        # name = Name  #-> Local Variable
        # id = Id     #-> Local Variable
        # print(name,id)
        print(self)
        self.name = Name  #Instance Variable
        self.id = Id  #Instance Variable
        
    def details(self): #instance Method
        print(self.name,self.id)
                 
# -----------------------------------------

# x = 4 -> systme Defined

S1 = student("Shanto",14)          #object / Instance
S1.name = "Saiful islam Shanto"
S1.details()
print("====================")






"""
class Student:
    def __init__(self,name,id,dep):
        self.name = name
        self.id = id
        self.dep = dep
        
    def display:
        print("Student Name : ", self.name)
        print("Student Name : ", self.name) 
"""
# <===============================================
""" class studnet:
    def __init__(self):
        print(self)
        print("This Is Create Object")
        
s1 = studnet()
print(s1)

s2 = studnet()
print(s2) """
# <===============================================
""" class stuent:
    def __init__(self, name, id):
        self.Name = name  # instance Variable
        self.Id = id


stu1 = stuent("Shanto", 24)
stu2 = stuent("Xyz", 44)
print(stu1.Name, stu1.Id)

print(stu2.Name, stu2.Id)
stu2.Name = "LIZA"
print(stu2.Name, stu2.Id) """
# <===============================================
""" class stuent:
    def __init__(self, name, id):
        self.Name = name  # <=== instance Variable
        self.Id = id
     
    # <=== Create Instance Method
    def details(self):
        print("Name:", self.Name, "ID:", self.Id)


# <=== Createing Object 
stu1 = stuent("Shanto", 24)
stu2 = stuent("Xyz", 44)

stu1.Id = 35
stu2.Id = 45
stu1.details()
stu2.details() """