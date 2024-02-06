""" 
    * https://wiki.python.org/moin/Decorators
    * https://www.scaler.com/topics/python/python-decorators/
    * https://www.scaler.com/topics/python/python-property/
    
    * => ক্লাস এর মধ্যে কোন ফাংশন Method যদি অব্জেক্ট এর মধ্যে দেওয়া হয় (ব্রকেট ছাড়া) তাহলে সেইটাকে এট্রিবিউট বলে।  -> print(mark.fullName)
    
    * => @property ব্যবহার করলে ক্লাস এর মধ্যে কোন ফাংশন Method কে এট্রিবিউট হিসেবে কল করা যায়। --> print(mark.fullName)
    
    * => Getter     : it is used to access the value of the attribute
    * => Setter     : Data Set করবে
    * => deleter    : Data Del করবে
"""

# class user:
#     def __init__(self, fName, lName):
#         self.first = fName
#         self.last = lName
#         self.email = f"{self.first}.{self.last}@user.com"
    
#     @property
#     def fullName (self):
#         return f"{self.first} {self.last}"
    
    
#     @fullName.setter
#     def fullName(self,value):
#         """ self.first = value.split(" ")[0]
#         self.last = value.split(" ")[1] """
        
#         first,last = value.split(" ")
#         self.first = first
#         self.last = last
#         self.email= f"{self.first}{self.last}@user.com"
#         # pass
        
#     @fullName.deleter
#     def fullName(self):
#         del self.first
#         del self.last
     
#     def get_email(self):
#         return self.email
        
# mark = user('mark',"zuku")
# print(mark.first)
# print(mark.last)
# # mark.email = "HEllo@gmail.com"
# print(mark.email)
# print(mark.get_email())
# # print(mark.fullName) ==< Attribute fullName
# # print(mark.fullName())
# print(mark.fullName)

# mark.fullName = "Saiful islam"
# print(mark.fullName)

# # del mark.fullName
# print(mark.first)
# print(mark.last)
# print(mark.email)

# ==================================================

# -> peroparty / getter / setter / deleter

class Student:
    
    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname
        self.email = f"{self.first}{self.last}@user.com"
    
    @property
    def fullName(self):
        return f"{self.first} {self.last}"
    
    
    # -> Setter Data
    
    @fullName.setter
    def fullName(self,value):
        self.first = value.split(" ")[0]
        self.last = value.split(" ")[1]
        self.email = f"{self.first}{self.last}@user.com"
        
        
    # -> Delete Data
    
    @fullName.deleter
    def fullName(self):
        del self.first
        del self.last
        del self.email
        
        

Student1 = Student("Saiful islam","Shanto")
print("👉 Old Data")
print(Student1.first)
print(Student1.last)
print(Student1.email)

#* 👉 Print full Name after user @property Decorator
print(Student1.fullName)

print("\n🚀 New Data")

Student1.fullName = "Shanto Studio"
print(Student1.fullName)
print(Student1.email)

print("\n❌ Delete Data")

Student1.fullName = "Shanto Studio"

# del Student1.fullName
del Student1.email
print(Student1.fullName)
print(Student1.email)