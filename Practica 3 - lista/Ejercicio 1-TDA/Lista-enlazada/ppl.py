from clase_lista import Lista

def test():
    l = Lista()

    num = int(input('Ingrese un numero->'))
    while num != 0:
        l.insertar(num)
        num = int(input('Ingrese otro numero->'))
    l.recorrer()
    sup = int(input('Ingrese el numero que quiere suprimir->'))
    xnum = l.suprimir(sup)
    print(f'Numero eliminado->{xnum}')
    xnum = int(input('Ingrese la posicion del numero que quiere recuperar->'))
    num = l.recuperar(xnum)
    print(f'Numero {num} recuperado')
    xnum = int(input('Ingrese el numero que quiere buscar->'))
    pos = l.buscar(xnum)
    print(f'Posicion del numero encontrado->{pos}')
    pri = int(input('Ingrese un numero->'))
    l.primer_elemento(pri)
    ult = int(input('Ingrese un numero->'))
    l.ultimo_elemento(ult)
    num = int(input('Ingrese un numero->'))
    sig = l.buscar_siguiente(num)
    print(f'La posicion del siguiente elemento es->{sig}')
    num = int(input('Ingrese un numero->'))
    ant = l.buscar_anterior(num)
    print(f'La posicion del elemento anterior es->{ant}')

if __name__ == '__main__':
    test()