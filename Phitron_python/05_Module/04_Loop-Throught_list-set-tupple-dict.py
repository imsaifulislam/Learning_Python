
# >-------- List

""" numbers = [1,2,3,4,5,6,7]
print(type(numbers))

for i in numbers:
    print(i) """


# => Sum of lsiT Item
""" numbers = [1,2,3,4,5,6,7]
total = 0

for i in numbers:
    total += i
    print(i)
print(total) """

# https://docs.python.org/3/library/functions.html#enumerate
# enumerate ;- Index Number সহ প্রিন্ট করে।
numbers = [1, 2, 3, 4, 5, 6, 7]
for num in enumerate(numbers):
    print(num)

# >-------- set

""" numbers = {1,2,3,4,5,6,7}
print(type(numbers))

for i in numbers:
    print(i) """

# >-------- Tuple

""" # numbers = 1,2,3,4,5,6,7
numbers = (1,2,3,4,5,6,7)
print(type(numbers))

for i in numbers:
    print(i) """

# >-------- Dict
""" 
info = {"Shanto": 23, "xyz":24} 
print(type(info))

for i in info.items():
    print("Key & Value: ",i)

for i in info.keys():
    print("KEys: ",i)

for i in info.values():
    print("values: ",i) """

marks = {"Bangla": 35, "English": 55, "DSA": 65, "Math": 90}
# print(marks)
# print(marks.items())
# print(marks.values())

# for mark in marks:
    # value = marks[mark]
    # print(mark, value)


# for sub, mark in marks.items():
    # print(sub,mark)
