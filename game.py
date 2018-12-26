from array import array
from random import randint

##gets a random card from a deck
#
#def randomCard (deck = []):
#    ri = randint(0,12)
#    while deck[ri] == 0:
#        ri = randint(0,12)
#    deck[ri] -= 1
#    return ri
#
##print("Enter number of players")
#
#nop = int(input())
#
#deck = []
#
#for i in range(13):
#    deck.append(4)
#
#players = []
#
#for i in range(nop):
#    players.append(randomCard(deck))
#
##print(deck)
#
##print(players)
#
#for i in range(nop):
#    #print("Player ", i+1, " would you like to switch or keep (1/0)")
#    choice = int(input())
#    if choice == 1:
#        if i == nop-1:
#            players[i] = randomCard(deck)
#            print(players)
#        else:
#            temp = players[i]
#            players[i] = players[i+1]
#            players[i+1] = temp
#            print(players)
#
#lowest = min(players)
#
#print (lowest)
#
#losers = []
#
#for i in range(nop):
#    print(i)
#    if players[i] == lowest:
#        losers.append(i+1)
#
##print ("losers are: ", losers)

class gameplay:
    def __init__(self):
        self.losers = []
        self.players = []
        self.deck = []
        self.nop = randint(2,10)
        self.botPos = randint(0,self.nop-1)
        self.info = []
        for i in range(13):
            self.deck.append(4)
        for i in range(self.nop):
            self.players.append(self.randomCard(self.deck))
        self.info.append(self.players[self.botPos])
        self.info.append(self.nop)
        self.info.append(self.botPos)
    def getInfo(self):
        return self.info
    def play(self, botChoice):
        for i in range(self.nop):
            #print("Player ", i+1, " would you like to switch or keep (1/0)")
            if i == self.botPos:
                choice = botChoice
            else:
                choice = randint(0,1)
            if choice == 1:
                if i == self.nop-1:
                    self.players[i] = self.randomCard(self.deck)
                    #print(self.players)
                else:
                    temp = self.players[i]
                    self.players[i] = self.players[i+1]
                    self.players[i+1] = temp
                    #print(self.players)
        lowest = min(self.players)
        
        if self.players[self.botPos] == lowest:
            return False
        else:
            return True
        #print (lowest)

        #for i in range(nop):
        #    print(i)
        #    if self.players[i] == lowest:
        #        self.losers.append(i+1)
    def randomCard(self, deck = []):
        ri = randint(0,12)
        while self.deck[ri] == 0:
            ri = randint(0,1)
        self.deck[ri] -= 1
        return ri

#test = gameplay()
#
#print(test.getInfo())
#
#print(test.play(1))