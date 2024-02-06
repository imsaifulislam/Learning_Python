""" def add(num1,num2, *numbers):
    print(num1)
    print(num2)
    print(numbers)


add(3, 4, 5, 6, 7) """


# **kargs
# -> key : args
# -> Key & Value আকারে ডাটা নেয় এবং dictonary টাইপে রাখে ডাটা।

def fullName(f_name, l_name):
    name = f"{f_name} {l_name}"
    return name


nameIs = fullName(l_name="Shanto", f_name="Saiful islam")
# print(nameIs)


def long_Name(**kargs):
    print(kargs)

# long_Name(first = "saiful", middle = "Islam", last = "shanto")


""" def name_mixed(first, last, **name_parts):
    print(first, last, name_parts)


nameIs = name_mixed(first="Saiful ", last="Shanto", middle="islam")
print(nameIs) """

""" 
def all_type(name, *args, **kargs):
    print(name)
    print(args)
    print(kargs)


nameIS = all_type("shanto","abc","xyz","ijk",pl="python",pl2="c",pl3="c++") """


def all_type(name, *args, **kargs):
    print(name)
    for i in args:
        print(i)
    print(kargs)
    for key, value in kargs.items():
        print(key, value)


nameIS = all_type("shanto", "abc", "xyz", "ijk",
                  pl="python", pl2="c", pl3="c++")
