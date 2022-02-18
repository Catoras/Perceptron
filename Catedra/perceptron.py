import numpy as np

class Perceptron:
    def __init__(self):
        self._W = []
        self._theta = self._m = self._b = float(0)

    def establecerValores(self, w1, w2, theta):
        self._W     = [w1, w2]
        self._theta = theta
        self._m     = -self._W[0]/self._W[1]
        self._b     = self._theta/self._W[1]

    def funcionDeActivacion(self, X):
        seniales = (np.dot(X,self._W) - self._theta) >= 0
        return seniales, self._m, self._b
