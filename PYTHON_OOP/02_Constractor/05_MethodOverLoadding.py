
""" class my_Calculator:
    #* Arived defualt Constractor 
    def product(self,*num):
        Prod = 1
        # print(num)
        for x in num:
            Prod = Prod*x
        print(Prod)

c1 =my_Calculator()
c1.product(5)
c1.product(5,10)
c1.product(5,10,20) """


# ========================================================

# -> Method Overloading With using libeary 
# => https://pypi.org/project/multipledispatch/

""" 
  * মেথড ওভারলোডীং একটি ক্লাসে সেম নামে মাল্টিপাল মেথড থাকবে সাথে মাল্টিপাল পেরামিটার্স থাকবে।
  
  -> Decorator
"""

from multipledispatch import dispatch

class my_claculator:
  
  @dispatch(int)
  def product(self,a):
    print(a)
    
  @dispatch(str,str)
  def product(self,a,b):
    print(int(a)*int(b))
    
  @dispatch(int,int,int)
  def product(self,a,b,c):
    print(a*b*c)
    
  @dispatch(float,float)
  def product(self,a,b):
    print(a*b)
    
  @dispatch(str,int)
  def product(self,a,b):
    print(int(a)*b)

# ====================

c1 = my_claculator()
c1.product(4)
c1.product("4","5")
c1.product(4,5,6)
c1.product(4.5,5.5)
c1.product("5",5)




























# ============================================

""" def sum(*args):
  s = 0
  for i in args:
    s+=i
  return s

x = sum(1,2,3,4,5,6,7)
print(x) """

                    #method Overloadding
""" class A:
  
  def show(self):
    print("Welcome")
  
  def show(self,firstName=""):
    print("Welcome",firstName)
  
  def show(self,firstName="",lastName=""):
    print("Welcome",firstName,lastName) """

""" class A:
  def show(self,firstName="",lastName=""):
    print("Welcome",firstName,lastName)

obj = A()
obj.show()
obj.show("Shanto")
obj.show("saiful Islam","Shanto") """
