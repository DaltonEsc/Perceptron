import numpy as np

from NeuralNetwork import NeuralNetwork
from Finalize import Finalize

if __name__=='__main__':
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])
    training_outputs = np.array([[0,1,1,0]]).T
    print("Input Data:")
    for i in range(4):
        print(training_inputs[i],training_outputs[i])

    network = NeuralNetwork()
    
    network.train(training_inputs, training_outputs, 10000)

    A = str(input("Input 1:"))
    B = str(input("Input 2:"))
    C = str(input("Input 3:"))

    output=Finalize(network.think(np.array([A,B,C])))
    
    print("Answer is: ", output.final, " with ", output.percent,"% certainty")