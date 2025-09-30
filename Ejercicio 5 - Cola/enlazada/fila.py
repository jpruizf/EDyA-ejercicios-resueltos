from clase_nodo import Nodo

class Fila_enlazada:
    __cant:int
    __pr:Nodo
    __ul:Nodo

    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0

    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nuevo = Nodo(x)
        nuevo.setSiguiente(self.__pr)
        if self.__ul is None:
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo)
        self.__ul = nuevo
        self.__cant += 1
    
    def suprimir(self):
        if not self.vacia():
            aux = self.__pr
            dato = self.__pr.getItem()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            del aux
        else:
            print('Fila vacia')
        return dato
    
    def recuperarpr(self):
        return self.__pr
    
    def recorrer(self):
        aux = self.__ul
        if aux != None:
            print(f'Numero de la fila->{aux.getItem()}')
            aux = aux.getSiguiente()