import numpy as np
class Lista:
    __ul:int
    __items:np.ndarray
    __dimension:int

    def __init__(self,dim):
        self.__ul = 0
        self.__dimension = dim
        self.__items = np.empty(self.__dimension,dtype=int)

    def insertar(self,x,p):
        if self.__dimension == self.__ul:
            print('Lista llena')
        else:
            if self.__dimension > 0 and 1 <= p:
                aux = self.__items[p-1]
                self.__items[p-1] = x
                self.__items[p] = aux
                self.__ul += 1
            elif self.__dimension > 0 and p == x+1:
                self.__items[p] = x
                self.__ul += 1
            elif self.__dimension == 0 and p == 1:
                self.__items[self.__ul] = x
                self.__ul += 1

    
    def vacia(self):
        return (self.__ul == 0)
    
    def suprimir(self,p):
        aux = 0
        if not self.vacia():
            if self.__dimension > 0 and 1 <= p <= self.__dimension:
                aux = self.__items[p]
                self.__ul -= 1
        else:
            print('Fila vacia')
        
        return aux
    def buscar(self,x):
        bandera = False
        i = 0
        while i < len(self.__items) and not bandera:
            if x == self.__items[i]:
                bandera = True
                pos = i
            else:
                i += 1
        return pos

    def recuperar(self,p):
        if not self.vacia():
            if self.__dimension > 0 and 1 <= p <= self.__dimension:
                x = self.__items[p]
        else:
            print('Lista vacia')
        return x

    def recorrer(self):
        for fila,indice in enumerate(self.__items):
            print(f'Elementos->{indice}')