from pila_sec import Pila_sec1

def test():
    dim = int(input('Ingrese el tamaño->'))
    psec = Pila_sec1(dim)
    for i in range(dim):
        num = int(input('Ingrese un numero->'))
        psec.insertar(num)
    xnum = psec.suprimir()
    print(f'El elemento eliminado fue->{xnum}')
    psec.recorrer()





if __name__ == '__main__':
    test()