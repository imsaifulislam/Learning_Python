""" 
    Clean the data and get a String output "a e i o u"
"""

""" data = "aNtEriOur\n\t>>"
new_data = data.lower()


output_string = ""
char_count = 0
for char in new_data:
    # print(char)
    if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
        # print(f"{char} found")
        output_string += char

        if char_count < 4:
            output_string += "_"
        char_count += 1


print(output_string) """


""" data = "aNtEriOur\n\t>>"
# print(data.lower())

new_data = data.lower()

empt_str = ""
char_count = 0

for char in new_data:
    # print(char)
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        # print(f"{char} Found")
        empt_str += char

        if char_count < 4:
            empt_str += "_"
        char_count += 1

print(empt_str) """


data = "aNtEriOur\\n\\t>>"
new_data = data.upper()
new_Str = ""

for i in new_data:
    if (i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U'):
        new_Str += i + ' '

print(new_Str)
