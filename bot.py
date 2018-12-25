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
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)
    
    def forward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.sigmoid(self.z3)

        return o
    
    def sigmoid(self, s):
        return 1/(1+np.exp(-s))
        
    def sigmoidPrime(self, s):
        return s*(1-s)

    def backward(self, X, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error*self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T) 
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta) 

    def train (self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)


NN = AceBot()
o = NN.forward(X)
print(o)
NN.train(X, y)
o = NN.forward(X)
print(o)