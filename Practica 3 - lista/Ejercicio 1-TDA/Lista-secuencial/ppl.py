from lista_sec import Lista


def test():
    dim = int(input('Dimension del arreglo->'))
    l = Lista(dim)
    for i in range(dim):
        n = int(input('Ingrese numero->'))
        l.insertar(n,i)
    pos = int(input('Elimine un elemento en una posicion p->'))
    x = l.suprimir(pos)
    p = int(input('Ingrese la posicion del numero que quiere recuperar->'))
    num = l.recuperar(p)
    print(f'El numero con la posicion {p} ingresada es->{num}')
    l.recorrer()
    print(f'Elemento eliminado->{x}')
    




if __name__ == '__main__':
    test()