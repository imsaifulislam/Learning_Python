# Python Variable Scope
""" def add_number():
    # local scope is Sum
    sum = 5+4
    return sum

print(add_number()) """


""" 
* Python Local Variables
 -> message variable is local to the greet() function, so it can only be accessed within the function.
 
def greet():
    #local variable
    
    message = "Hello"
    print(("Local", message))
    
greet()
print(message) 

"""

# *****************************************************************

""" 
* Python Global Variables
-> This time we can access the message variable from outside of the greet() function. This is because we have created the message variable as the global variable.

message = "Variable "
def greet():
    print("Local", message)

greet()
print("Global", message) """


""" message = "Global"
def outer():
    message = "Local"

    # nested Function
    def inner():
        nonlocal message
        message = "NonLocal"
        print("Inner: ", message)

    inner()
    print("Outer: ", message)


outer()
print(message) """

""" 
def total_cost(price, Quantity):
    cost = price * Quantity
    return cost


pay = total_cost(10, 3)
print(f"Please apy : {pay}") """


balance = 580  # -> Global variavle


def total_cost(price, Quantity):
    global balance
    cost = price * Quantity
    # balance = 100 #-> Local variavle
    # remaiing = balance - cost
    # balance = remaiing
    balance = balance - cost
    # print(remaiing)
    return cost


print(f"Blance Outside Before is: {balance}")
pay = total_cost(10, 3)
print(f"Please apy : {pay}")

print(f"Blance Outside After is: {balance}")
