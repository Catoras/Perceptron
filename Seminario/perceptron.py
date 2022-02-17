import archivo
import numpy as np

class Perceptron:
    def __init__(self, w1, w2, theta):
        self._W = [w1,w2]
        self._theta = theta
        self._X = archivo.getXDesdeArchivo('inputs.txt')

        if not self._X:
            raise Exception("Problema al intentar leer los inputs")

        self._m = -self._W[0]/self._W[1]
        self._b = self._theta/self._W[1]

    def funcionDeActivacion(self):
        return (np.dot(self._X,self._W) - self._theta) >= 0

