import random
import itertools

deck = list(itertools.product(range(1, 14),
                              [
            "Spade", "Club", "Hearts", "Diamond"
            ]
)
)

# print(deck)
random.shuffle(deck)
print(deck)


for i in range(5):
    print(deck[i][0], "Of", deck[i][1])
