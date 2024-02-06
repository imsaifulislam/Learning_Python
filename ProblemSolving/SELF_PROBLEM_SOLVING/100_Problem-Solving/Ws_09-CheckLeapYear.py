year = int(input("Enter the Year: "))

if (year % 400 == 0) and (year % 100 == 0) :
    print(year,"Is Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"Is Leap Year")
else:
    print(year,"Is Not Leap Year")