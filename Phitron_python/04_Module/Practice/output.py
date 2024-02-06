from Calculator import *
print("Enter The A for Addition")
print("Enter The S for Subtraction")
print("Enter The M for Multiplication")
print("Enter The D for Division")

x = input("Enter The Input : ")
try:
    if x == "A" or x == "a":
        add()
    elif x == "S" or x == "s":
        sub()
    elif x == "M" or x == "m":
        mul()
    elif x == "D" or x == "d":
        div()
    else:
        print("WORNG INPUT")
finally:
    print("Try Again")