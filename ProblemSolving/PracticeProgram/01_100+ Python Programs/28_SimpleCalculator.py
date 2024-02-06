print("~~~~~Simple Caclulator~~~~~")

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter second Number : "))

print("Press 1 for Addition \nPress 2 for subtraction \nPress 3 for Multiplication \nPress 4 for Division")

choice = int(input("Enter your choice from 1-4 : "))

if choice == 1:
    print("Addition : ", num1+num2)
elif choice == 2:
    print("subtraction :", num1-num2)
elif choice == 3:
    print("Multiplication :", num1*num2)
elif choice == 4:
    print("Division :", num1/num2)
else:
    print("Wrong Input, Select 1-4")
