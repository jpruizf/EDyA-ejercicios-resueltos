from clase_cola2 import Cola2


def test():
    d = int(input('Ingrese la dimension de la fila->'))
    F = Cola2(d)
    for i in range(d):
        n = int(input('Ingrese un numero->'))
        F.insertar(i,n)
    F.recorrer()
    x =F.suprimir()
    print(f'Ejecucion exitosa!| se elemino el numero-> {x}')





if __name__ == '__main__':
    test()