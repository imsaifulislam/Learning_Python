""" square = lambda x:x*x
result = square(6)
print(result)

add = lambda x,y : x+y
print(add(10,20)) """

""" num = [12,45,48,4,86,4,64,4,8]
def doubleIt(x):
    return x * 2

double_it2= lambda x:x*2

# double_num = map(doubleIt,num)
double_num = map(double_it2,num)
print(num)
print(list(double_num)) """


num = [12, 45, 48, 4, 86, 4, 64, 4, 8]
# double_Num = lambda x : x*2
# result_Num = map(double_Num,num)
# print(list(result_Num))
# print(set(result_Num))
# print(tuple(result_Num))

# -> Map
""" num2 = [12, 45, 48, 4, 86, 4, 64, 4, 8]
double_num = map(lambda x: x*2, num2)
square_num = map(lambda x: x*x, num2)
print(list(double_num))
print(list(square_num)) """


# -> Filter
# num2 = [12, 5, 48, 4, 6, 8, 7, 9, 64, 14, 8]
# big_number = filter(lambda num: num <= 10, num2)
# print(list(big_number))
# EVEN_num = filter(lambda num: (num % 2) == 0, num2)
# odd_num = filter(lambda num: (num % 2) != 0, num2)
# print(list(EVEN_num))
# print(list(odd_num))

# -> Filter on List of dict

student = [
    {'name': 'Shanto', 'age':23, 'Dep':'cmt'},
    {'name': 'Liza', 'age':22, 'Dep':'cmt'},
    {'name': 'Abir', 'age':45, 'Dep':'eee'},
    {'name': 'sojib', 'age':37, 'Dep':'cmt'},
]

check_age = filter(lambda AgeIs: AgeIs['age']<30, student)
print(list(check_age))
