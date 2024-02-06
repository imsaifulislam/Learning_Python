# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter Year: "))

if year % 400 == 0 and year % 100 == 0:
    print(year,"Is Leap Year")
elif year % 4 == 0 and year != 100 == 0:
    print(year,"Is Leap Year")
else:
    print(year,"Is not Leap year")