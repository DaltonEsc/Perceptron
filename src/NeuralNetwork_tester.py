import numpy as np
from NeuralNetwork import NeuralNetwork

class NeuralNetwork_tester():

    def __init__(self):
        training_inputs = np.array([[0,0,1],
                                    [1,1,1],
                                    [1,0,1],
                                    [0,1,1]])
        training_outputs = np.array([[0,1,1,0]]).T
        print("Input Data:")
        for i in range(4):
            print(training_inputs[i],training_outputs[i])

if __name__=='__main__':
    runner = NeuralNetwork_tester()
    network = NeuralNetwork()
        
