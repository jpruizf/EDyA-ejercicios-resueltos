from clase_estado import Estado
import numpy as np

class Pila:
    __dimension:int
    __cant:int
    __tope:int
    __items:np.ndarray

    def __init__(self,d):
        self.__dimension = d
        self.__items = np.empty(self.__dimension,dtype=Estado)
        self.__cant = 0
        self.__tope = -1
    
    def insertar(self,x):
        if self.__dimension > self.__cant:
            self.__tope += 1
            self.__items[self.__tope] = x
            self.__cant += 1
        else:
            print('Pila llena')
    
    def vacia(self):
        return(self.__tope == -1)
    
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__tope]
            self.__tope -= 1
        else:
            print('Pila vacia')
        return x
    
    def mostrar(self):
        for indice,fila in enumerate(self.__items):
            print(fila)