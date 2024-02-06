# Write a program that will reverse a four digit number.Also it checks whether the reverse is true. in python


""" user_input = int(input("Enter your four Digit Number: "))

num = user_input

a=num%10
num = num//10

b = num%10
num = num//10

c = num%10
num = num//10

d = num%10
num = num//10

rev = 1000*a + 100*b + 10*c + 1*d
print("Original Num: ",user_input)
print("Reverse Num :", rev)


if user_input == rev:
    print("True")
else:
    print("False") """
    

""" user_input = input("Enter your four Digit Number: ")

num = str(user_input[::-1]) #start:stop:step
print(num)

if user_input == num:
    print("True")
else:
    print("False") """
    
    
user_input = int(input("Enter your four Digit Number: "))

rev_num = 0

while user_input != 0:
    digit = user_input % 10
    rev_num = rev_num * 10 + digit
    user_input //= 10
print("Reversed Number:",rev_num)