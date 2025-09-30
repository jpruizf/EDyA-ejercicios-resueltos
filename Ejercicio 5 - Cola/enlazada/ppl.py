from fila import Fila_enlazada

def test():
    f = Fila_enlazada()
    x = int(input('Ingrese un numero->'))
    f.insertar(x)
    x = int(input('Ingrese un numero->'))
    f.insertar(x)
    suprim = f.suprimir()
    print(f'Numero eliminado->{suprim}')
    f.recorrer()






if __name__ == '__main__':
    test()