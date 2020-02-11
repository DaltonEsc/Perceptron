import numpy as np

class Finalize():

    def __init__(self, output):
        self.final = 0
        self.percent = 0
        self.readable(output)

    def readable(self, output):
        
        if output >.5:
            self.final = np.ceil(output)
            self.percent = np.dot(output,100)
        else:
            self.final = np.floor(output)
            self.percent = np.dot((1-output), 100)
        