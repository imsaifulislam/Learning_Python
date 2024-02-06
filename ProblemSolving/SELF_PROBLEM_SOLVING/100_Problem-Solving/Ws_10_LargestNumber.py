num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 3rd Number : "))

if num1 > num2 and num3<num1:
    print(num1, "is Largets Number")
elif num2> num1 and num3<num2:
    print(num2, "is Largets Number")
else:
    print(num3, "is Largets Number")
    