# Write a program that will tell whether the number entered by the user is odd or even.


num = int(input("Enter a Number: "))

if num % 2 == 0:
    print(num,"its Even")
else:
    print(num,"its ODD")