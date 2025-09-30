from fila_circular import Cola_Circular

def test():
    dim = int(input('Ingrese el tamanio de la fila->'))
    cc = Cola_Circular(dim)
    x = int(input('Ingrese un numero->'))
    for x in range(dim):
        cc.insertar(x)
    eliminado = cc.suprimir()
    cc.recorrer()
    print('El numero suprimido fue->',eliminado)






if __name__ == '__main__':
    test()