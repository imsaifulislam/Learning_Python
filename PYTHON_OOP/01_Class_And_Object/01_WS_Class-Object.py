""" class Student:
    
    def __init__(self,name,id,subject):
        self.name = name
        self.id = id
        self.subject = subject
        self.email = f"{self.name}@gmail.com"
    
    
    def get_Student_info(self):
        print(f"Student Name : {self.name}\nStudent Id: {self.id}\nTechnology : {self.subject}\nStudent Email : {self.email}")
    

S1 = Student("Shanto",35,"Cmt")
S1.get_Student_info()
 """
# -------------------------

class xyz:
    
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
    def showInfo(self):
        print(f"Name is: {self.name} and Roll is : {self.roll}")
        

student1 = xyz("Shanto",24)
student1.showInfo()