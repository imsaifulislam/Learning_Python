# ==============================>
# => Class & Constractor

class xyz:
    
    def __init__(self,name,roll,subject,semister,age):
        self.name = name #-> Instance Variable
        self.roll = roll
        self.subject = subject
        self.semister = semister
        self.age = age
        
    
    def Update_roll(self,UProll):
        self.roll = UProll
    
    def Update_semister(self,UPsemister):
        self.semister = UPsemister
    
    def Update_subject(self,UPsubject):
        self.subject = UPsubject
        
    def showInfo(self): #-> Instance Methods
        print(f"Name is: {self.name}\nRoll is : {self.roll}\nSubject Is : {self.subject}\nSemister Is : {self.semister}\nStudent Age IS : {self.age}")
    
    
    # => Pass by Reference 
    def checksubject(self,subjects):
        if self.subject == subjects.subject:
            print(f"subject Is Same")
        else:
            print("subject Not Same")
    
        

student1 = xyz("Shanto",25,"CSE","6th",24) #-> Object
student1.showInfo()

print("\n==========================\n")

student2 = xyz("XYZER",25,"CSE","7th",25) #-> Object
student2.showInfo()

print("\n==========================\n")

# => Pass by Reference 
student1.checksubject(student2)

""" student1.Update_roll(15)
student1.Update_subject("CSE")
student1.Update_semister("7th")
student1.showInfo() """

print("\n==========================\n")



# print(student1.__dict__) #-> Show Perameter Data
# -> Pass by Reffarence 

# student1.checkAge(age)