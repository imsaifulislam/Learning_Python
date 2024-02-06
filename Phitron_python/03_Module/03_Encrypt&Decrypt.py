data = "az"
shift = 1
output = ""
for char in data:
    output += chr((ord(char) + shift-97) % 26 + 97)
    # print(type(ord(char)+ shift))

print(output)

# for x in range(65,90):
#     print(f"ASCII value {str(x)}, Character Is : {chr(x)}")
