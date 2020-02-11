import numpy as np
from NeuralNetwork import NeuralNetwork

        

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
    print(network.synaptic_weights)
    network.train(training_inputs, training_outputs, 10000)
    print(network.synaptic_weights)
    A = str(input("Input 1:"))
    B = str(input("Input 1:"))
    C = str(input("Input 1:"))

    print("New Situation: Input = ", A,B,C)
    print("Output Data:")
    print(network.think(np.array([A,B,C])))