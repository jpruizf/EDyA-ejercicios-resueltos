import numpy as np

class Fila_Circular:
    __items:np.ndarray
    __dim:int
    __pr:int
    __ul:int
    __cant:int

    def __init__(self,dimension):
        self.__cant = 0
        self.__dim = dimension
        self.__pr = 0
        self.__ul = 0
        self.__items = np.empty(self.__dim,dtype=object)

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elem:object)->None:
        if self.__cant < self.__dim:
            self.__items[self.__ul] = elem
            self.__ul = (self.__ul+1)%self.__dim
            self.__cant += 1
        else:
            print('Fila llena')
    
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__pr]
            self.__pr = (self.__pr+1)%self.__dim
            self.__cant -= 1
        else:
            print('Fila vacia')
        return x

    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            for j in range(self.__cant):
                print(f'Elementos en fila->{self.__items[i]}')
                i = (self.__pr+1)%self.__dim