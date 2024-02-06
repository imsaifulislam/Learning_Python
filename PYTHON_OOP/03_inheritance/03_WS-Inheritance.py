""" 
    * Singel Inheritance
    * Multilevel Inheritance
    * Multiple Inheritance
"""

""" class A:
    def displayA(self):
        print("Hello A Python Inheritance")

class B(A):
    def displayB(self):
        print("Hello B Python Inheritance")
        

obj = B()
obj.displayA()
obj.displayB() """

# ================================
# => Multilevel Inheritance
""" class A:
    def displayA(self):
        print("Hello A Python Inheritance")

class B(A):
    def displayB(self):
        print("Hello B Python Inheritance")

class C(B):
    def displayC(self):
        print("Hello C Python Inheritance")
        

obj = C()
obj.displayA()
obj.displayB()
obj.displayC() """

# ================================


# => Multiple Inheritance
class A:
    def displayA(self):
        print("Hello A Python Inheritance")

class B:
    def displayB(self):
        print("Hello B Python Inheritance")

class C(A,B):
    def displayC(self):
        print("Hello C Python Inheritance")
        

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()