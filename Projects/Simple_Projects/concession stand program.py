""" # concession stand program

menu = {"pizza":3.00,
        "nachis": 4.50,
        "popcorn": 6.00,
        "fries":2.50,
        "Pretzel":3.50,
        "chips": 1.00,
        "soda": 3.00,
        "Lamonda": 4.25
        }

cart = []
total = 0

print("-------- MENU --------\n")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    
print("\n-------- END MENU --------")


while True:
    food = input("Select an item (Q to quit): ").lower()
    
    if food == "q":
        break 
    elif menu.get(food) is not None:
        cart.append(food)
        
# print(cart)

print("\n----- Your ORDER -----")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print("\n----- TOTLA -----")
print(f"Total is: ${total:.2f}")
 """


# -------------------------------------------------
# => একটি মেনু তেরি করে সেইটার থেকে কি কি ওর্ডার করা হয়েছে সেইটার লিস্ট এবং টিটাল টা প্রিন্ট করো 


# menu

menu = {"pizza": 2.50,
        "popcorn":3.50,
        "soda": 4.20,
        "water": 1.00,
        "nachos":2.50,
        "chips":1.50}

cart=[]
total = 0

print("----- MENU LIST -----")

for value,key in menu.items():
    print(f"{value:10} : ${key:.2f}") #-> :10 is for SPace & .2f is after decimal point show only 2 digit 


# -> User Input & Add food in the cart
while True:
    foodIs = input("Add an food from the menu - (q for quit) : ").lower()
    if foodIs == "q":
        break
    elif menu.get(foodIs) is not None:
        cart.append(foodIs)

print("\n---------- 🛒 Your Order ----------")
for foodIs in cart:
    total += menu.get(foodIs)
    print(foodIs(menu),end=" ")

print("\n---------- 💰 TOTAL Bill ----------")
print(f"Total bill is : ${total}")