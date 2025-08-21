import pandas as pd # type: ignore
import numpy as np # type: ignore
import tensorflow as tf # type: ignore

class NNLib:
    def __init__(self, layers):
        self.XLen = 3 # change this based on the number of features in input data
        self.initializeWB(layers)  # move this to train or fit function (because it uses length of X - input)
        pass

    def initializeWB(self, layers):
        W = {}
        b = {}
        for i in range(0,len(layers)):
            list = []
            if i == 0:
                list = [0 for _ in range(self.XLen)]
            else:
                list = [0 for _ in range(layers[i-1])]

            W[i] = [list for _ in range(layers[i])]
            b[i] = [0 for _ in range(layers[i])]
        
        self.W = W
        self.b = b

    def dense(self):
        pass
