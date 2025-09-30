from clase_fila import Cola_Circular
from clase_estado import Estado
def test(n):
    f = Cola_Circular(n)
    f.insertar(Estado(n,''))
    a = Estado(n,'')
    while not f.vacia():
        actual = f.suprimir()
        escalon = a.getEscalon()
        if escalon == 0:
            print(f'[{actual.getMensaje()}]')
        elif escalon >= 2:
            print(f'[{Estado(escalon-2,a.getMensaje()+'2')}]')
        elif escalon >= 1:
            print(f'[{Estado(escalon-1,a.getMensaje()+'1')}]')

if __name__ == '__main__':
    n = int(input('Ingrese la cantidad de peldaños->'))
    test(n)
    