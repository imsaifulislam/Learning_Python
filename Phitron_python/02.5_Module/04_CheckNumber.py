""" Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program. """

while True:
    User_input = input("Enter a Number, Quit for Exit : ")

    if User_input.lower() == "quit":
        print("Program Is Exit")
        break

    try:
        number = float(User_input)
        if number == 0:
            print("ZERO")
        elif number > 0:
            print("Positive")
        else:
            print("Nagative")
            
    except ValueError:
        print("Invalid Input, Quit for Exit")
