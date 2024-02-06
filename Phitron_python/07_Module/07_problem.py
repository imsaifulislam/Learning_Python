def replace_comma_with_space(text):
    
    add_space = ""
    
    for char in text:
        if char == ",": 
            char = " "
        add_space += char
        
    return add_space

        

s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
