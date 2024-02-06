""" 
    Diconary
    https://docs.python.org/3/tutorial/datastructures.html
"""

marks = {'physics': 12, 'math': 35, 'DSA': 100}
print(type(marks))
print(marks)

marks['math'] = 56.5
marks["Bangla"] = 89
# del marks['DSA']
print(marks)
marks_Valus = marks.values()
print(marks_Valus)
marks_keys = marks.keys()
print(marks_keys)
# marks_Clear = marks.clear()
# print(marks_Clear)
print(marks.items())
