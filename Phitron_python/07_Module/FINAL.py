# ===================================================
# => 1

""" def create_string(ListIs):
    result = " ".join(ListIs)
    
    return result

l = ["This", "is", "very", "fantastic"]
list_to_string = create_string(l)
print(list_to_string) """


# ===================================================
# => 4

""" def print_hi():
    return "hi"

print(print_hi()) """


# ===================================================
# => 5

""" def create_list(DictIs):
    
    Dict_to_list = []
    for key,value in DictIs.items():
        Dict_to_list.append(key)
        Dict_to_list.append(value)
    return Dict_to_list

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

output = create_list(d)
print(output) """

# ===================================================
# => 6

""" def clean_string(text):

    remove_Char = ":;,-."
    
    clean_str = ""
    
    for char in text:
        if char not in remove_Char:
            clean_str+=char

    return clean_str
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output) """



# ===================================================
# => 7

def replace_comma_with_space(text):
    add_space =""
    
    for char in text:
        if char == ",":
            char = " "
        add_space += char
    return add_space
    
    
    
    
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
