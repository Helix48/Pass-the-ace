from array import array
from random import randint

#gets a random card from a deck

def randomCard (deck = []):
    ri = randint(0,12)
    while deck[ri] == 0:
        ri = randint(0,12)
    deck[ri] -= 1
    return ri

print("Enter number of players")

nop = int(input())

deck = []

for i in range(13):
    deck.append(4)

players = []

for i in range(nop):
    players.append(randomCard(deck))

print(deck)

print(players)

for i in range(nop):
    print("Player ", i+1, " would you like to switch or keep (1/0)")
    choice = int(input())
    if choice == 1:
        if i == nop-1:
            players[i] = randomCard(deck)
            print(players)
        else:
            temp = players[i]
            players[i] = players[i+1]
            players[i+1] = temp
            print(players)