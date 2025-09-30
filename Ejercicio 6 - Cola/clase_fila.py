import numpy as np

class Cola_Circular:
    __dimension:int
    __pr:int
    __ul:int
    __cant:int
    __items:np.ndarray

    def __init__(self,dim):
        self.__cant = 0
        self.__dimension = dim
        self.__pr = 0
        self.__ul = -1
        self.__items = np.empty(self.__dimension,dtype=object)

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        if self.__cant < self.__dimension:
            self.__items[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__dimension
            self.__cant += 1
            print('Elemento insertado en la fila')
        else:
            print('Fila llena')
        return x
    def suprimir(self):
        if self.vacia():
            print('Fila vacia')
        else:
            x = self.__items[self.__pr]
            self.__pr =(self.__pr+1)%self.__dimension
            self.__cant -= 1
            return x
    
    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            for j in range(self.__cant):
                i=(i+1)%self.__dimension
                print(f'Elementos de la fila->{self.__items[i]}')