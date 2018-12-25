import numpy as np
# input     ["Card Number", "Number of player"]     or [2, 13]
# output    ["Swap/Stay"]                           or [0]

X = np.array((  [2, 13], 
                [4, 3],
                [2, 12]), dtype=float)

y = np.array((  [0], 
                [0], 
                [1]), dtype=float)

class AceBot:
    def __init__(self):
        self.inputSize =  2
        self.outputSize =  1
        self.hiddenSize =  3
  
        self.w0 = np.random.randn(self.inputSize, self.hiddenSize) # weights for the input to hidde n
        self.w1 = np.random.randn(self.hiddenSize, self.outputSize) # weights for hidden to output
    
    def forward(self, X):
        self.h = np.dot(X, self.w0)  # mult the weights with the input, then add them together 
        self.h = self.sigmoid(self.h) # activation function
        self.o = np.dot(self.h, self.w1) # mult the hidden layer with the hidden weights the add 
        o = self.sigmoid(self.o) # activation function 

        return o
    
    def sigmoid(self, s):
        return 1/(1+np.exp(-s)) 
    def sigmoidPrime(self, s):
        return s*(1-s)

    def backward(self, X, y, o):
        o_error = y-o # error of output
        o_delta = o_error * self.sigmoidPrime(self.o)

        h_error = np.dot(o_error, self.w1.T) 
        h_delta = h_error * self.sigmoidPrime(self.h)

        self.w0 += np.dot(X[:,None], np.reshape(h_delta, (1,3)))
        self.w1 += np.dot(self.h[:,None], o_delta)[:,None]

    def getMove(self, X):
        buff = self.forward(X)
        if buff > 0.5:
            return 1
        else:
            return 0

    def isCorrect(self, didWin, move):
        buff = np.bitwise_xor(move.astype(int), np.array(([1]), dtype=int))
        buff = buff.astype(float)
        if didWin:
            self.train(cardAndPlayers, move) # If it won than feed it the move it did
        else:
            self.train(cardAndPlayers, buff)

    def train (self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

#Example definition

aceBot = AceBot()  # New instance of bot
cardAndPlayers = np.array(([1, 13]), dtype=float)  # Define the card value and the number of players

prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
prediction = aceBot.forward(cardAndPlayers)  # Shows the prediction of the results
print("prediction be: ", prediction)
move = np.around(aceBot.forward(cardAndPlayers))   # Same value as prediction but rounds up or down
print("move be: ", move)

aceBot.isCorrect(True, move) #after the game is done use the isCorrect to tell the bot if the move was good or not so it can train
