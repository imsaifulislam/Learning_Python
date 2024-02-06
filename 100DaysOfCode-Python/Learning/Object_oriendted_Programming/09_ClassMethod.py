class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and Working ON {self.company} company")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Shanto"
e1.show()

e1.changeCompany("Google")
e1.show()

print(Employee.company)
