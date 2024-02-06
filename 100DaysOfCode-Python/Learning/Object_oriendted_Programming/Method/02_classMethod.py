""" class Employer:
    org_name = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def info(cls):
        return cls.org_name
    

print(Employer.info()) """

# * --------------------------------------


class Student:

    collageName = "SAIC"  # -> Class Variable

    def __init__(self, name, id):
        self.Name = name
        self.__id = id

    def details(self):  # -> Instance Method
        print(
            f"Name : {self.Name}, ID : {self.__id}, Collage Name : {Student.collageName}")

    @classmethod  # -> Class Method
    def fullNameCollage(cls, collageFullName):
        # -> Class Method Call before create object
        #print("Called in Class Method") 
        cls.collageName = collageFullName


student1 = Student("Shanto", 35)
student1.details()
print(student1.__dict__)

# -> call In class Refarance
Student.fullNameCollage("saic institute of management and technology")

# -> call In object Refarance [Not Recomneded]
# student2.fullNameCollage("saic institute of management and technology")
student2 = Student("Liza", 34)
student2.details()

print(student2.__dict__)

# -> Class Method Call before create object
#Student.fullNameCollage("Saic")