""" class Calculator:
    
    def itemsMullTiplication(self,*nums):
        item = 1
        for i in nums:
            item = item*i
        print(item)
        
    def itemsSum(self,*nums):
        item = 0
        for i in nums:
            item = item+i
        print(item)
    
    def itemsSub(self,*nums):
        item = 0
        for i in nums:
            item = i - item
        print(item)
        
# ============================================

cal1 = Calculator()
cal1.itemsMullTiplication(5,5)
cal1.itemsSum(5,5)
cal1.itemsSub(5,6) """

# ----------------------------------------------------------------------------------

""" from multipledispatch import dispatch

class Calculator:
    
    @dispatch(int,int)
    def items(self,a,b):
        print(a+b)
    
    @dispatch(int,str)
    def items(self,a,b):
        print(a+int(b))
        
    @dispatch(int,int,float)
    def items(self,a,b,c):
        print(a+b+c)
        
# ========================================================

cal1 = Calculator()
cal1.items(5,5)
cal1.items(5,"5")
cal1.items(5,5,2.5) """


# ==========================================================

""" class Calculator:
    
    def sum(self,*num):
        item = 1
        for i in num:
            item = item * i
        print(item)

    def add(self,*num):
        item = 0
        for i in num:
            item = item + i
            print(item)
            
# * ------------------- *

cal1 = Calculator()
cal1.sum(10,2)
cal1.add(10,2) """

# =================================================

from multipledispatch import dispatch

class Calculator:
    
    @dispatch(int,int)
    def num(self,a,b):
        print("Int + int",a+b)
    
    @dispatch(int,float)
    def num(self,a,b):
        print("Int + float",a+b)
    
    @dispatch(int,str)
    def num(self,a,b):
        print("Int + String",a+int(b))
        
cal1 = Calculator()
cal1.num(10,20)
cal1.num(10,2.0)
cal1.num(10,"5")