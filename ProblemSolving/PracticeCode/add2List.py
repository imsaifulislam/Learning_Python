inventory = [
    "Crimson Sword",
    "Great Helm"
    "Leather Boots"
]

chest = [
    "Health Potion",
    "Mana Potion",
    "Map of Riches"
]

# for item in chest:
#     inventory.append(item)
    
inventory.extend(chest )

print(inventory)