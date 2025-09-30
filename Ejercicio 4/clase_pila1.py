import numpy as np
class Pila_1:
    __items:np.ndarray
    __tope:int
    __cant:int
    __dimension:int
    def __init__(self,cant):
        self.__dimension = cant
        self.__cant = 0
        self.__tope = -1
        self.__items = np.empty(self.__dimension,dtype=int)
    
    def insertar(self,x):
        if self.__tope < self.__dimension-1:
            self.__tope += 1
            self.__items[self.__tope] = x
            self.__cant += 1
        else:
            print('Pila llena')
        return x
    def vacia(self):
        return (self.__tope == -1)
    
    def suprimir(self):
        x = 0
        if self.vacia():
            print('Pila Vacia')
        else:
            x = self.__items[self.__tope]
            self.__tope -= 1
            self.__cant -= 1
    def getCant(self):
        return self.__cant
    def getTope(self):
        return self.__tope
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):
                print(f'Movimiento: {i}| Disco->{self.__items[i]}')
        else:
            print('Pila vacia')