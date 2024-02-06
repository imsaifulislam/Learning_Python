""" class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
class Course:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        
class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course =course

class School:
    def __init__(self,name,teachers,courses,students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        
    def get_student(self):
        for students in self.students:
            print(f'Name : {students.name}, Age : {students.age}, Age : {students.id}')
        

schoole_name = 'phitron'
ds_course = Course('Data Structure','Einstine')
teacher_1 = Teacher('Einstine',ds_course)

algo_course = Course('Algorithm','Editosn')
teacher_2 = Teacher('Editosn',algo_course)

student_1 = Student('Shanto',23,45)
student_2 = Student('saiful',25,96)
student_3 = Student('xyz',30,72)

teachers = [teacher_1, teacher_2]
courses = [ds_course,algo_course]
students = [student_1, student_2, student_3]

my_school = School(schoole_name,teachers, courses, students)
print(my_school.__str__)

my_school.get_student() """

# -> multiple  Inheritance => When a child class is derived from then one parent class

""" class prey:
    def flee(self):
        print("This Animal Flees")

class Predator:
    def hunt(self):
        print("This animal is Hunting")
        
class Rabbit(prey):
    # print("Rabbit")
    pass        
class hawk(Predator):
    # print("hawk")
    pass        
class fish(prey,Predator):
    # print("Fish")
    pass    

Rabbit = Rabbit()
Rabbit.flee()

fish = fish()
fish.flee()
fish.hunt()

hawk = hawk()
hawk.hunt() """

# ==================================================

# -> Inharit 1
""" class Father:
    def hobby(self):
        print("Farming")

class Mother:
    def hobby(self):
        print("Gurdaning")
        
class Child:
    def hobby(self):
        Father.hobby(self)
        Mother.hobby(self)
        print("Programming")
        
c = Child()
c.hobby() """



class Father():
    def Father_hobby(self):
        print("Farming")

class Mother():
    def Mother_hobby(self):
        print("Gurdaning")
        
class Child(Father,Mother): #-> Inharit This Class
    def Child_hobby(self):
        print("Programming")
        
c = Child()
c.Father_hobby()
c.Mother_hobby()
c.Child_hobby()