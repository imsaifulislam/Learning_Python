""" class dog:
    def __init__(self,name, color):
        self.NameIs = name
        self.ColorIs= color
        
    def update_color(self,ColorIs):
        self.ColorIs = ColorIs
        
    def view(self):
        print(self.ColorIs, self.NameIs, "is Smiling")

# =======================================================

d1 = dog("Rover", "Brown")
# d1.view()
print(d1)
d2 = dog("Tomy","White")
d2.update_color("Pink")
d2.view()

# print(d1.__dict__)
# print(d2.__dict__)

# print(dir(d1))
# print(help(d1))
# print(dir(d2))

# ====================================== """



class studentInfo:
    
    def __init__(self,name,roll,depertemnt):
        self.StudentName = name
        self.StudentRoll = roll
        self.StudentDepertemnt = depertemnt
        
    # => Information update method
    
    def Roll_Update(self,StudentRoll):
        self.StudentRoll = StudentRoll
    
    def Dep_Update(self,StudentDepertemnt):
        self.StudentDepertemnt = StudentDepertemnt
    
    # => Show information
    
    def StudentDetails(self):
        print(f"Studnet Name = {self.StudentName} \nStudnet Roll = {self.StudentRoll} \nStudnet Depertemnt = {self.StudentDepertemnt}")


# ==================================

student1 = studentInfo("Shanto",354206,"CMT")
student1.Dep_Update("EEE")
student1.StudentDetails()

""" print(student1.__dict__)
print(dir(student1))
# print(student1.__doc__) """

