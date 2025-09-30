from clase_lista import Lista

def test():
    l = Lista()
    xnum = int(input('Ingrese un numero->'))
    l.insertar(xnum)
    xnum = int(input('Ingrese un numero->'))
    l.insertar(xnum)
    xnum = int(input('Ingrese un numero->'))
    l.insertar(xnum)
    #l.ordenar()
    #l.traza()
    l.recorrer()




if __name__ == '__main__':
    test()