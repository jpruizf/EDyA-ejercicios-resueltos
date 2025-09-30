from clase_cola_estatica import Cola_Est


def test():
    dimention = int(input('Ingrese la dimension de la fila->'))
    F = Cola_Est(dimention)
    for i in range(dimention):
        n = int(input('Ingrese un numero->'))
        F.insertar(i,n)
    F.recorrer()
    F.suprimir()
    print('Ejecucion exitosa')






if __name__ == '__main__':
    test()