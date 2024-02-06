# Write a program that will give you the sum of 3 digits

""" num1 = int(input("Enter A number: "))
num2 = int(input("Enter B number: "))
num3 = int(input("Enter C number: "))

sumOf = num1+num2+num3
print("Sum of 3 Number is: ", sumOf) """


""" num = int(input("Enter 3 Number: "))

a = num%10      # = [345%10 = 5]
num = num//10   # = [345//10 = 34]    
b = num%10      # = [34%10 = 10]
c = num//10     # = [345//10 = 3]


res = a+b+c
print("Sum of Three Digits: ", res) """



num = int(input("Enter 3 Number: "))
sum = 0

while num>0:
    sum =sum+ num % 10
    num = num //10
print("Sum of Digits = ",sum)

""" 
    https://www.youtube.com/watch?v=-PPkWv2D2K0

"""