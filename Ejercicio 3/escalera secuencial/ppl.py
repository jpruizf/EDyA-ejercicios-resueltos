from clase_pila_sec import Pila
from clase_estado import Estado

def test():
    n = int(input('Ingrese el numero de peldanios->'))
    pil = Pila(n)
    pil.insertar(Estado(n,''))
    while not pil.vacia():
        actual = pil.suprimir()
        escalon = actual.getEscalon()
        if escalon == 0:
            print(actual.getSolucion())
        elif escalon >= 2:
            pil.insertar(Estado(escalon -2,actual.getSolucion()+'2'))
        elif escalon >= 1:
            pil.insertar(Estado(escalon-1,actual.getSolucion()+'1'))





if __name__ == '__main__':
    test()