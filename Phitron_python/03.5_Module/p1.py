""" WordIs = str(input("Enter a Word : "))

lowerToUpper = WordIs.upper()
UpperTolower = WordIs.lower()

print(lowerToUpper)
print(UpperTolower) """

""" num = int(input("Enter a Number : "))

for row in range(1, num+1):
    for col in range(1,row+1):
        print(col, end= " ")
    print() """


# asciiData = ord(data)
# print(ord(data))

# if (asciiData >= 64 and asciiData <= 90):
    # print("Uppercase")

def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    return uppercase_count, lowercase_count, digit_count, symbol_count

input_string = "P@#yn26at^&i5ve"
upper, lower, digits, symbols = count_characters(input_string)

print("Uppercase =", upper)
print("Lowercase =", lower)
print("Digits =", digits)
print("Symbols =", symbols)
