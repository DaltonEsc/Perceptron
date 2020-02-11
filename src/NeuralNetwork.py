import numpy as np


class NeuralNetwork():
    
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3,1)) - 1


    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self, x):
        return x*(1-x)

    def train(self, training_inputs, training_outputs, training_iterations):
       for interation in range(training_iterations):

           outputs = self.think(training_inputs)
           error = training_outputs - outputs
           adjustment = np.dot(training_inputs.T,error * self.sigmoid_derivative(outputs))
           self.synaptic_weights += adjustment

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

