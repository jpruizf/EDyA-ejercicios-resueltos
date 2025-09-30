import numpy as np

class Lista_Sec:
    __dimension:int
    __cant:int
    __items:np.ndarray

    def __init__(self,dim):
        self.__cant = 0
        self.__dimension = dim
        self.__items = np.zeros(self.__dimension,dtype=int)
    
    def vacia(self):
        return (self.__cant == 0)
    
    def insertar(self,x):
        i = 0
        if self.__dimension == self.__cant-1:
            print('Lista llena')
        elif int(self.__items[i] <= x) and int(x < self.__items[i+1]):
            self.__items[i] = x
            self.__cant += 1
        elif int(x < self.__items[1]):
            self.__items[1] = x
            self.__cant += 1
            i += 1
        elif int(self.__items[i-1] < x):
            self.__items[i-1] = x
            self.__cant += 1
            i += 1 
    
    def recorer(self):
        for indice,fila in enumerate(self.__items):
            print(f'Poscion->{indice}|Elemento de la lista->{fila}')