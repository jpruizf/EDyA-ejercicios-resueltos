from clase_lista import Lista

def test():
    l = Lista()
    xnum = int(input('Ingrese un numero->'))
    xpos = int(input('Ingrese la posicion->'))
    '''_____funcionando____'''
    l.insertar(xnum,xpos)
    l.recorrer()
    num = int(input('Ingrese un numero->'))
    pos = l.buscar(xnum)
    print(f'Se encuentra {num} | En la posicon {pos}')
    xnum = int(input('Ingrese un numero->'))
    l.primer_elemento(xnum)
    xnum = int(input('Ingrese un numero->'))
    l.ultimo_elemento(xnum)
    xpos = int(input('Ingrese la posicion del elemento->'))
    num = l.recuperar(xpos)
    print(f'En la posicon {xpos} | Se encuentra el {num}')
    num = int(input('Ingresar numero->'))
    sig = l.buscar_siguiente(num)
    print(f'El numero {num} | Se encuentra en la posicion {sig}')
    num = int(input('Ingresar numero->'))
    ant = l.buscar_anterior(num)
    print(f'El numero {num} | Se encuentra en la posicion {ant}')




if __name__ == '__main__':
    test()