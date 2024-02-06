""" def swapIng(num1,num2):
    num1 = num2
    num2 = num1
    temp = num2
    
    return temp

number = swapIng(10,20)
print(number) """


num1 = int(input("ENter 1st NUmber : "))
num2 = int(input("ENter 2st NUmber : "))

print("AFter Swapping num1 => ",num1)
print("AFter Swapping num2 => ",num2)

temp = num1
num1 = num2
num2 = temp

print("before Swapping num1 => ",num1)
print("before Swapping num2 => ",num2)