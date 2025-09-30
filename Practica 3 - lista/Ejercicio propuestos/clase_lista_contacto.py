from clase_nodo import Nodo
from clase_contacto import Contacto
class Lista_Contacto:
    __cabeza:Nodo
    __cant:int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def insertar(self,contacto)->None:
        nuevo = Nodo()

        if self.vacia():
            nuevo.setContacto(contacto)

            self.__cabeza = nuevo

            self.__cant += 1
        else:
            aux = self.__cabeza

            anterior = None

            while aux != None and contacto.getNombre() > aux.getDatosContacto().getNombre():

                anterior = aux

                aux = aux.getSiguiente()

            if anterior is None:

                nuevo.setContacto(contacto)

                nuevo.setSiguiente(self.__cabeza)

                self.__cabeza = nuevo
            else:
                nuevo.setContacto(contacto)

                nuevo.setSiguiente(aux)

                anterior.setSiguiente(nuevo)

            self.__cant += 1

        print('Se Agrego un contacto de forma ordenada en la lista')

    def vacia(self):

        return self.__cant == 0
    
    def eliminarContacto(self,nombre):
        aux = self.__cabeza
        if not self.vacia():
            numero = int(aux.getDatosContacto().getNumero())
            del aux
            self.__cant -= 1

        else:
            numero = self.buscarContacto(nombre)
            aux = self.__cabeza
        if numero != self.__cabeza.getDatosContacto().getNumero() and self.__cabeza is None:
            print('El numero no se encuentra en la lista')
        else:
            return numero
    
    def buscarContacto(self,nombre):
        if not self.vacia():
            if self.__cabeza.getSiguiente() is None and nombre == self.__cabeza.getDatosContacto().getNombre():
                numero = int(self.__cabeza.getDatosContacto().getNumero())
            else:
                bandera = False
                aux = self.__cabeza
                while aux != None and not bandera:
                    if nombre == aux.getDatosContacto().getNombre():
                        numero = int(aux.getDatosContacto().getNumero())
                        bandera = True
                    else:
                        aux = aux.getSiguiente()
        return numero
    def validarContacto(self,unContacto):
        aux = self.__cabeza
        while aux != None:
            if isinstance(unContacto,Contacto):
                if aux.getDatosContacto().getNumero() == unContacto.getNumero():
                    raise ValueError('Contacto Ya Registrado')
            aux = aux.getSiguiente()
    
    def getCantidad(self):
        return self.__cant
    
    def recorrer(self):
        while self.__cabeza is not None:
            print(f'Elementos->{self.__cabeza.getDatosContacto().getNombre()}|{self.__cabeza.getDatosContacto().getNumero()}')
            self.__cabeza = self.__cabeza.getSiguiente()