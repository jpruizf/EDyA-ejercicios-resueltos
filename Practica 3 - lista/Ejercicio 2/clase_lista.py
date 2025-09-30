from clase_nodo import Nodo

class Lista:
    __cabeza:Nodo
    __cant:int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,xnum):
        nuevo = Nodo(xnum)
        if self.__cabeza is None:
                nuevo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevo
                self.__cant += 1
                self.__cabeza = self.__cabeza.getSiguiente()
        else:
            aux = self.__cabeza
            anterior = self.__cabeza
            while aux != None:
                if xnum >= aux.getItems() and xnum < aux.getSiguiente().getItems():
                    nuevo.setItems(xnum)
                    self.__cant += 1
                    anterior.setSiguiente(nuevo)
                    nuevo.setSiguiente(aux)
                elif aux.getSiguiente() is None and xnum > aux.getItems():
                    nuevo.setItems(xnum)
                    self.__cant += 1
                else:
                    anterior = aux
                    aux = aux.getSiguiente()
        print('Se inserto de forma ordenada elemento en la lista')

    def ordenar(self):
        cota = None
        k = None
        while k != self.__cabeza:
            k = self.__cabeza
            p = self.__cabeza
            while p.getSiguiente() != cota:
                if p.getItems() > p.getSiguiente().getItems():
                    aux = p.getItems()
                    p.setSiguiente(p.getSiguiente().getItems())
                    p.getSiguiente().setItems(aux)
                    k = p
                p = p.getSiguiente()
            cota = k.getSiguiente()
        print('Lista ordenada con exito')
    def getCantidad(self):
        return self.__cant
    def traza(self)->None:
        print('cabeza->',self.__cabeza)
        print('actual.getSiguiente()->| total elementos cargados->',self.__cabeza.getSiguiente(),self.getCantidad())
        print('Tipo de siguiente->',type(self.__cabeza.getSiguiente()))
    def recorrer(self):
        indice = 0
        while self.__cabeza != None and indice < self.__cant:
            print(self.__cabeza.getItems())
            self.__cabeza = self.__cabeza.getSiguiente()
            indice += 1