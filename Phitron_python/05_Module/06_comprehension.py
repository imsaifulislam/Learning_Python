number = [12, 5, 48, 4, 6, 8, 7, 9, 64, 14, 8]
odd_number = []

# for i in num:
#     if i % 2 == 1:
#         odd_number.append(i)

# print(odd_number)

# odd_number2 = [num*2 for num in number]
# odd_number2 = [num*2 for num in number if num % 2 == 1 if num % 5 == 0]
# print(odd_number2)


names = ['shanto', 'sakib', 'sumon']
ages = [37, 32, 21]

pairs = [(names, ages) for name in names for age in ages if age < 25]
print(pairs)


for name in names:
    print(name)
    for age in ages:
        if age < 25:
         print(name, age)
