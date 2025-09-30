import numpy as np
class Cola2:
    __dimension: int
    __items:np.ndarray
    __pr:int
    __ul:int
    def __init__(self,d):
        self.__dimension = d
        self.__items = np.empty(self.__dimension,dtype=object)
        self.__pr = 0
        self.__ul = 0

    def vacia(self):
        return (self.__ul == -1)
    
    def insertar(self, indice,dato):
        if indice < self.__dimension and self.__dimension == self.__ul:
            print('Fila llena')
        else:
            self.__items[indice] = dato
            self.__ul -= 1
            self.__pr += 1
        
        return dato

    def suprimir(self):
        if self.vacia():
            print('Fila Vacia')
        else:
            x = self.__items[self.__ul]
            self.__ul -= 1
            self.__pr += 1
        
        return x
    
    def recorrer(self):
        for j in range(self.__dimension):
            print(f'Salieron los Numeros->{self.__items[j]}')