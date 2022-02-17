def getXDesdeArchivo(nombreDelArchivo):
    X = []
    try:
        with open(nombreDelArchivo) as f:
            lines = f.readlines()

        for line in lines:
            vector = line.rstrip("\n").split(',')
            vector[0] = float(vector[0])
            vector[1] = float(vector[1])
            X.append(vector)
    except:
        print("No existe el archivo con los inputs")

    return X