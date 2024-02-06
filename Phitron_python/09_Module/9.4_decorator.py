""" def timer(func):
    def inner():
        print("Time Start")
        func()
        print("Time End")
    return inner

@timer
def get_factorial():
    print("Factorial")
    
# timer(get_factorial)()
get_factorial() """

# ----------------------------------

""" 
    * Decorator ব্যবহার এর সময়, যদি প্রথম ফাংশন এর মধ্যে কোণ আরগুমেন্ট পাস করা হয় তখন inner Argments এর মধ্যে *args এবং **kwargs ব্যবহার করতে হবে। **kwargs ব্যবহার করা টা রিকোমেন্ডেড
"""
""" import math
def timer(func):
    # def inner(): #-> এখানে Error দেখাচ্ছে 
    def inner(*args, **kwargs): #-> Inner Arguments 
        print("Time Start")
        # func() #-> এখানে Error দেখাচ্ছে 
        func(*args, **kwargs) #-> Inner Arguments 
        print("Time End")
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")
    
# timer(get_factorial)()
# get_factorial(5) 
get_factorial(n=5) 

"""



""" import math
import time
def timer(func):
    def inner(**args):
        print("Time Start")
        start = time.time()
        func(**args)
        end = time.time()
        print("Time End", end-start)
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")
    
# timer(get_factorial)()
get_factorial(n=500) """




""" def hello1(func):
    def exec():
        print("Hello World 1")
        func()
        print("Hello World 3")
    return exec

@hello1
def hello2():
    print("Hello World 2")
    
hello2() """







def first_func(x):
    def inner_func():
        print("Hello 01")
        x()
        print("Hello 02")
    return inner_func

@first_func
def sec_funct():
    print("Hello 03")
    
sec_funct()






