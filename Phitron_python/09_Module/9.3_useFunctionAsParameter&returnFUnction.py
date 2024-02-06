# 9-3 Use function as parameter and return function

""" def do_something(x,y):
    print(f"x: {x} y: {y}")
    

do_something(10,20) """

# => এখানে একটা Function এ পেরামিটার এর মধ্যে আরেকটা ফাংশান পাস করা হয়েছে। 
""" def do_something(work):
    print("Start The WOrkd")
    # print(type(work))
    work()
    print("Done with Work")

def practice_coding():
    print("I'm practacing python")
    
do_something(practice_coding) """

# =---------------------------------

""" def do_something(work):
    print("Start Work")
    # print(work)
    # hello_something()
    work()
    print("END Start Work")

def hello_something():
    print("WOrk in the prccesign")
    
do_something(hello_something) """

""" def xyz(info):
    print("xyz Start")
    # print(info)
    info()
    print("xyz End")

def xyz_info():
    print("Learning python")
    
xyz(xyz_info) """

# ===========================================

# * একটু ফাংশন এর মধ্যে আরেকটা ফাংশন ডিক্লিয়ার এবং সেইটা পিন্ট বা রিটার্ন করার নিয়ম 
""" def do_something():
    print("Inside the function do_something")
    def inner_function():
        print("Inside the inner function")
    inner_function()

# do_something()

def first_function():
    print("Inside the first Function")
    def second_function():
        print("Inside the inner Function")
    return second_function """

# first_function()

# first = first_function()
# print(first)

""" first = first_function()
first() 

first_function()()
"""


def first_func():
    print("Inside First Function")
    def inner_fucn():
        print("Inner the First Function")
    # print(inner_fucn()) -> None
    # inner_fucn()
    return inner_fucn #-< Show Nothing
    # return inner_fucn() #-< Show Data

# show_dtata = first_func()
# print(show_dtata) -> Show Memeory Location
# show_dtata() #-> Now Show inner Func data

first_func()() #-> Show first func & inner Func Data