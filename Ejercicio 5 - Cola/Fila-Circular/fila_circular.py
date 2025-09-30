import numpy as np

class Cola_Circular:
    __dimension:int
    __pr:int
    __ul:int
    __cant:int
    __items:np.ndarray
    def __init__(self, dim):
        self.__cant = 0
        self.__dimension = dim
        self.__pr = 0
        self.__ul = 0
        self.__items = np.empty(self.__dimension,dtype=int)

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        if self.__cant == self.__dimension:
            print("Fila llena")
        else:
            self.__items[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__dimension
            self.__cant += 1
        return x
    
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__pr]
            self.__pr=(self.__pr+1)%self.__dimension
            self.__cant -= 1
        else:
            print("fila vacia\n")
        return x
    
    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            for i in range(self.__cant):
                print(f'Numero de la fila->{self.__items[i]}')
                i = (i+1)%self.__dimension
