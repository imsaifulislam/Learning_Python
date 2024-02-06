# achieve Constructor Overloading
""" 
    যখন একটি ক্লাসে মাল্টিপাল __init__(ইনিট মেথড) থাকে এবং সেই __init__(ইনিট মেথড) গুলো যদি ডিফারেন্ট পেরামিটার্স হত তখন তাকে Constructor Overloading বলে।
"""

""" class Student:
            
    def __init__(self,*info):
        if len(info) == 3:
            self.NameIs = info[0]
            self.IdIs = info[1]
            self.CGPA = info[2]
            
        elif len(info) == 2:
            self.NameIs = info[0]
            self.IdIs = info[1]
            
        elif len(info) == 1:
            self.NameIs = info[0]
            
        print("A Student Object Created")
    
        
    
# ==========================================

s1 = Student("Shanto",354207, 4.0)
s1 = Student("Shanto",354206)
s1 = Student("Shanto")
s1 = Student() """


# *=========================================


class Student:
            
    def __init__(self,**info):
        if len(info) == 3:
            self.NameIs = info['name']
            self.IdIs = info['Id']
            self.CGPA = info['CG']
            
        elif len(info) == 2:
            self.NameIs = info['name']
            self.IdIs = info['Id']
            
        elif len(info) == 1:
            self.NameIs = info['name']
            
        print("A Student Object Created")
    
        
    
# ==========================================

s1 = Student(name="Shanto",Id=354207, CG=4.0)
s1 = Student(name="Shanto",Id=354206)
s1 = Student(name="Shanto")
s1 = Student()