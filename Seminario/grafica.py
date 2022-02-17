import matplotlib.pyplot as plt
import math

class Grafica:
    def __init__(self):
        plt.figure("Practica 1 - Perceptron")

    def establecerEjesCoordenados(self, X):
        x1max = x2max = 2
        x1min = x2min = -2
        for coordena in X: #[0] Horizontal [1] Vertical
            if coordena[0] > x1max:
                x1max = math.ceil(coordena[0]) + 1
            elif coordena[0] < x1min:
                x1min = math.floor(coordena[0]) - 1
            if coordena[1] > x2max:
                x2max = math.ceil(coordena[1]) + 1
            elif coordena[1] < x2min:
                x2min = math.floor(coordena[1]) - 1

        ejeX1 = [x1min,x1max] # eje Horizontal
        ejeX2 = [x2min,x2max] # eje Vertical
        puntoDeOrigen = [0,0]
        plt.plot(ejeX1, puntoDeOrigen, 'k')
        plt.plot(puntoDeOrigen, ejeX2, 'k')

    def pintarPuntos(self, X, m, b, senialesDeActivacion):
        for i in range(len(X)):
            if senialesDeActivacion[i]:
                plt.plot(X[i][0],X[i][1],'og')
            else:
                plt.plot(X[i][0],X[i][1],'or')

        plt.axline((X[0][0], (X[0][0]*m)+b), (X[3][0], (X[3][0]*m)+b), color='#2a9cde')
        plt.show()

    def limpiar(self):
        plt.cla