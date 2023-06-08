import random

coin = random.choice(['heads', 'tails'])
print(coin)

myRandint = random.randint(1, 10)
print(myRandint)

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)
