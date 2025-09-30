from clase_lista_contacto import Lista_Contacto
from clase_contacto import Contacto
def test():
    l = Lista_Contacto()
    contacto = Contacto(26441101024,'Pepito')
    contacto2 = Contacto(26468179024,'Pelito')
    l.insertar(contacto)
    l.insertar(contacto2)
    suprimido = l.eliminarContacto('Pelito')
    print(f'El numero->{suprimido}, Fue suprimirdo')
    xnum = l.buscarContacto('Pepito')
    print(f'Numero encontrado:{xnum}, con nombre-> Pepito')
    l.recorrer()


if __name__ == '__main__':
    test()