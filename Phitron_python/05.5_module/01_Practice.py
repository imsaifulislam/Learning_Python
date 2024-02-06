""" 

Write a program to create a function show_employee() using the following conditions - 
    It should accept the employee’s name and salary and display both using a f string.
    If the salary is missing in the function call then assign default value 9000 to salary
    If the name is missing then assign a default value anonymous


"""

""" 
    * function
    * 

"""


""" def show_employee():
    name = input("Enter your Name : ")
    salary = input("Enter your salary : ")
    print(f"Name is: {name}, Salary Is: {salary}")

    if (name == ""):
        print("anonymous")
    if (salary == ""):
        print(f"9000")

show_employee() """


def show_employee(name = '', salary = 9000):
    
    # print(f"Name is: {name}, Salary Is: {salary}")
    if name == "":
        name= "anonymous"
    
    print(f"Name is: {name}, Salary Is: {salary}")
    

# show_employee("shanto", )
# show_employee("shanto",45000 )
show_employee("",)


