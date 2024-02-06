""" class Claculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def addition(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")
        
    def substraction(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")
        
    def multiplication(self):
        print(f"{self.num1} * {self.num2} = {self.num1 * self.num2}")
        
    def division(self):
        try:
            print(f"{self.num1} / {self.num2} = {self.num1 / self.num2}")
        except ZeroDivisionError:
            print("Zero Can't Be Divide")

count = Claculator(10,20)
count.addition()
count.substraction()
count.multiplication()

x = Claculator(0,0)
x.division()
 """
 
 
 
 
 
 
#  => Using inheritance
 
class Claculator:
    
    def addition(self, num1, num2):
        print (f"{num1} + {num2} = {num1 + num2}")
        
    def substraction(self, num1, num2):
        print (f"{num1} - {num2} = {num1 - num2}")
        
    def multiplication(self, num1, num2):
        print (f"{num1} * {num2} = {num1 * num2}")
        
    def division(self, num1, num2):
        try:
            print (f"{num1} / {num2} = {num1 / num2}")
        except ZeroDivisionError:
            print ("Zero Can't Be Divide")

class supperCalculator(Claculator):
    
    def cube(self,a):
        print (a*a*a)
    
    def square(self,a):
        print (a*a)

""" count = Claculator(10,20)
count.addition()
count.substraction()
count.multiplication()

x = Claculator(0,0)
x.division() """


y = supperCalculator()

y.addition(5,20)
y.substraction(5,20)
y.multiplication(5,20)
y.division(5,20)
y.square(3)
y.cube(3)
