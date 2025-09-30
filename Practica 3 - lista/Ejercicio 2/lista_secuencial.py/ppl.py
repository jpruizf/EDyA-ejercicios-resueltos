from clase_lista import Lista_Sec

def test():
    dim = int(input('Ingrese el tamaño->'))
    l = Lista_Sec(dim)
    for i in range(dim):
        elem = int(input('Ingrese un elemento->'))
        l.insertar(elem)
    l.recorer()




if __name__ == '__main__':
    test()