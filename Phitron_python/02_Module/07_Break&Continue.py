# num = 1

""" for i in range(num+1):
    if(i==5):
        break
    print(i) """

""" while num <= 25:
    print(num)
    if num == 7:
        break
    num += 1 """


num = 7
while num <= 20:
    num += 1

    if num % 2 == 1:
        continue
    print(num)
