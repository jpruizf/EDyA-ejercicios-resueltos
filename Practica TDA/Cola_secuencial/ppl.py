from fila_sec1 import Cola_Sec1

def test():
    dim = int(input('Dimension arreglo->'))
    f = Cola_Sec1(dim)
    for i in range(dim):
        num = int(input('Numero->'))
        indice = int(input('Indice->'))
        f.insertar(num,indice)
    xnum = f.suprimir()
    print(f'Numero eliminado->{xnum}')
    f.recorrer()




if __name__ == '__main__':
    test()