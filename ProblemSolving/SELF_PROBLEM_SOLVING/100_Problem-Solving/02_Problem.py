# Write a program that will convert celsius value to fahrenheit


def celsiusTofahrenheit(num):
#    num = int((num*1.8)+32)
   num = int((num*9/5)+32)
   return num

celsius = int(input("Enter celsius Value: "))
fahrenheit= celsiusTofahrenheit(celsius)
print("celsius To fahrenheit", fahrenheit,"F")