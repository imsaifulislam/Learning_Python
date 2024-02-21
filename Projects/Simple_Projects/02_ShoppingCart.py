# List[],Set{},Tuple()

foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to buy (Q for Quit): ")
    
    if food.lower() == "q":
        print("❌ Program Quit")
        break
    else:
        price = float(input(f"Enter The Price of a {food} : $"))
        foods.append(food)
        prices.append(price)

print("------- Your Cart -------")
for food in foods:
    print(food,end=" ")

for price in prices:
    total += price
    
print()
print(f"Your Total is: ${total}")

        