class NueralNetwork:
    import numpy as np

    training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    def __init__(self):
    

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self x):
        return x*(1-x)

    

    print("Training Data: ")
        for i in range(4):
        print(training_inputs[i], training_outputs[i])


    np.random.seed(1)

    synaptic_weights = 2 * np.random.random((3,1)) - 1



    for interation in range(20000):

        input_layer = training_inputs
        outputs = sigmoid(np.dot(input_layer, synaptic_weights))

        error = training_outputs - outputs

        adjustment = error * sigmoid_derivative(outputs)

        synaptic_weights += np.dot(input_layer.T,adjustment)

    print('Trained weights:')
    print(outputs)