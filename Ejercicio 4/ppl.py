from clase_tablero import Tablero


def test():
    soluciones = [3]
    n = int(input('Ingrese un numero de disco->'))
    potencia = (pow(2,n)-1)
    T=Tablero(potencia)
    pila_origen = int(input('Ingrese la pila origen->'))
    pila_destino = int(input('Ingrese la pila destino->'))
    total = T.mover_disco(pila_origen,pila_destino)
    soluciones.append(total+1)
    print(f'soluciones->{soluciones}')
if __name__ == '__main__':
    test()