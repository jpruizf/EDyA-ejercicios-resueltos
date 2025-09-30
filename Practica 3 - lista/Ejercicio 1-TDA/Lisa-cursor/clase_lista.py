from clase_nodo import Nodo

class Lista:
    __cabeza:Nodo
    __cant:int
    __libre:int

    def __init__(self):
        self.__cabeza = None
        self.__libre = 0
        self.__cant = 0

    def vacio(self):
        return self.__cant == 0
    
    def setLibre(self, xlibre):
        self.__libre = xlibre
    
    def getLibre(self):
        return self.__libre
    
    def insertar(self,x,pos):
        nuevo = Nodo(x,pos)
        if self.vacio() and self.getLibre() != pos:
            print('Espacio libre')
            self.__cabeza = nuevo
            nuevo.setSiguiente(self.__cabeza)
            self.setLibre(pos)
            self.__cant += 1
        else:
            if self.__cabeza.getItems() <= nuevo.getItems():
                nuevo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevo
                self.setLibre(pos)
                self.__cant += 1
            else:
                aux = self.__cabeza
                anterior = self.__cabeza
                while aux != None and nuevo.getItems() > aux.getItems():
                    anterior = aux
                    aux = aux.getSiguiente()
                anterior.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                self.setLibre(pos)
                self.__cant += 1
                print('El elemento fue insertado en el centro')
    
    def suprimir(self,x):
        if self.vacio():
            print('Lista vacia')
        elif self.__cabeza.getItems() == x:
            aux = self.__cabeza
            dato = aux.getItems()
            self.__cabeza = self.__cabeza.getSiguiente()
            del aux
            self.__cant -= 1
            self.__tope -= 1
        else:
            aux = self.__cabeza
            anterior = self.__cabeza
            while aux != None and aux.getItems() != x:
                anterior = aux
                aux = aux.getSiguiente()
            if aux != None:
                dato = aux.getItems()
                anterior.setSiguiente(aux.getSiguiente())
                del aux
                self.__cant -= 1
                self.__tope -= 1
        return dato
    
    def recuperar(self,pos):
        bandera = False
        if self.getLibre() == pos:
            dato = self.__cabeza.getItems()
            self.setLibre(pos)
            bandera = True
        else:
            aux = self.__cabeza
            while aux != None and not bandera:
                if self.getLibre() != pos:
                    aux.setSiguiente(aux.getSiguiente())
                    aux = aux.getSiguiente()
                else:
                    dato = self.__cabeza.getItems()
                    self.setLibre(pos)
                    bandera = True
        if bandera is True:
            return dato
        else:
            print('No se encontro el elemento en la posicion ingresada')
    
    def buscar(self,x):
        aux = self.__cabeza
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                indice = aux.getSiguiente()
                bandera = True
            else:
                aux.setSiguiente(aux.getSiguiente())
                aux = aux.getSiguiente()
        if bandera is True:
            return indice
        else:
            print('No se encontro la posicion del elemento ingresado')

    def primer_elemento(self,x)->None:
        if self.vacio():
            if self.__cabeza.getItems() == x:
                print(f'{x} Es el primer elemento de la lista')
        else:
            aux = self.__cabeza
            bandera = False
            while aux != None and not bandera:
                if x == aux.getItems():
                    print(f'{aux.getItems()} Es el primer elemento de la lista')
                    bandera = True
                else:
                    print(f'{x} No es el primer elemento')
                    aux = aux.getSiguiente()

    def ultimo_elemento(self,x)->None:
        indice  = 0
        if self.__cabeza is None:
            if self.__cabeza.getItems() == x:
                print(f'{x} Es el primer elemento de la lista')
        else:
            aux = self.__cabeza
            bandera = False
            while aux != None and not bandera and indice < self.__cant:
                if x == aux.getItems() and aux is None :
                    print(f'{aux.getItems()} Es el ultimo elemento de la lista')
                    bandera = True
                else:
                    print(f'{x} No es el primer elemento')
                    aux = aux.getSiguiente()
                    indice += 1
    def buscar_siguiente(self,x):
        aux = self.__cabeza
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                indice = self.getLibre()
                bandera = True
            else:
                aux.setSiguiente(aux.getSiguiente())
                aux = aux.getSiguiente()
        if bandera is True:
            return indice + 1
        else:
            print('No se encontro la posicion del elemento ingresado')
    
    def buscar_anterior(self,x):
        aux = self.__cabeza
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                indice = self.getLibre()
                bandera = True
            else:
                aux.setSiguiente(aux.getSiguiente())
                aux = aux.getSiguiente()
        if bandera is True:
            return indice - 1
        else:
            print('No se encontro la posicion del elemento ingresado')
    def recorrer(self)->None:
        aux = self.__cabeza
        while aux != None and self.getLibre() < self.__cant:
            print(f'Elemento->{aux.getItems()}')
            aux = aux.getSiguiente()