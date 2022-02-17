import perceptron
import grafica

def main():
    opc = 0
    plano = grafica.Grafica()

    while (True):
        try:
            w1 = float(input("Ingrese el valor de w1: "))
            w2 = float(input("Ingrese el valor de w2: "))
            theta = float(input("Ingrese el valor de theta: "))

            p = perceptron.Perceptron(w1, w2, theta)

            plano.limpiar()
            plano.establecerEjesCoordenados(p._X)
            plano.pintarPuntos(p._X,p._m,p._b,p.funcionDeActivacion())

            opc = int(input("Digite 0 para ingresar otros valores: "))
            if not opc == 0:
                break
        except:
            print("Error - Intentelo otravez")

if  __name__ == '__main__':
    main()