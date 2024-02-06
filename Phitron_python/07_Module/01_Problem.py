""" 
https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
"""

""" def create_string():
    l = ["This", "is", "very", "fantastic"]
    # x = " ".join(str(x) for x in l)
    myString = " "
    
    for x in l:
        myString += x+" "
    
    return print(myString)


create_string() """

# ===================================================

""" def create_string1():
    l = ["This", "is", "very", "fantastic"]
    x = " ".join(l)
    
    return print(x)

create_string1() """

# ===================================================

""" def create_string2():
    l = ["This", "is", "very", "fantastic"]
    x = " ".join(str(x) for x in l)
    
    return print(x)

create_string2() """

# ===================================================
# => এইটায় String এর প্রথমে একটি গেপ দেয়
""" def create_string3():
    l = ["This", "is", "very", "fantastic"]
    myString = " "
    
    for x in l:
        myString += x + " "
    
    return print(myString)

create_string3()  """

# ===================================================

""" def create_string4():
    l = ["This", "is", "very", "fantastic"]
    myString = " ".join(map(str,l))
    
    return print(myString)

create_string4()  """

# ===================================================

""" l = ["This", "is", "very", "fantastic"]
myString = " "

for i in l:
    myString += i + ' '

print(myString)
 """
 
#  ==================================================

def create_string(ListIs):
    result = " ".join(ListIs)
    return result

l = ["This", "is", "very", "fantastic"]
list_To_String = create_string(l)
print(list_To_String)
 