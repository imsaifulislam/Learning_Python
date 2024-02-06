# print(Largest_Num)

# nums = {45,89,54,116,-12}
# print(max(nums))
# print(min(nums))
# rev_num = reversed(Largest_Num)
# print(list(rev_num))
Largest_Num = [45, 89, 54, 116, -12]
sorted_num = sorted(Largest_Num)
# print(list(sorted_num))


Largest_Num2 = [45, 89, 54, 116, -12]
sorted_num2 = sorted(Largest_Num2, reverse=True)
# print(list(sorted_num2))


student = [
    {'name': 'Shanto', 'age':23, 'Dep':'cmt'},
    {'name': 'Liza', 'age':22, 'Dep':'cmt'},
    {'name': 'Abir', 'age':45, 'Dep':'eee'},
    {'name': 'sojib', 'age':37, 'Dep':'cmt'},
]

# sorted_student = sorted(student, key = lambda students:students['age'], reverse=True)
# sorted_student = sorted(student, key = lambda students:students['name'], reverse=True)
sorted_student = sorted(student, key = lambda students:students['name'])

# print(sorted_student)

firends = ['Abil','Kabil', 'Mosharrof', 'Badol', 'Noman']
# sorted_firneds = sorted(firends, reverse=True)
sorted_firneds = sorted(firends)
print(sorted_firneds)