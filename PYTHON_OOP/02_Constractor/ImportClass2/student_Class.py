class Student:
    
    def __init__(self,name,id):
        self.StudentName = name
        self.StudentId = id
        self.semister = "1st"
    
    def set_semister(self,semister):
        self.semister = semister
    
    def get_semister(self):
        return self.semister
    
    def student_Details(self):
        print(f"Student Name: {self.StudentName}\nStudent Id: {self.StudentId}\nStudent Semister: {self.semister}")
        
        

