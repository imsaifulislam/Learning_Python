# User will input (3ages).Find the oldest one

def find_Olds(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"Is Oldest")
    elif(num2>num1 and num2>num3):
        print(num2,"Is Oldest")
    else:
        print(num3,"Is Oldest")
        

a = int(input("Enter 1st Input: "))
b = int(input("Enter 2st Input: "))
c = int(input("Enter 3st Input: "))

find_Olds(a,b,c)