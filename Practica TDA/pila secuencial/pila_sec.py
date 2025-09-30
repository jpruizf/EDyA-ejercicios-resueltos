import numpy as np
class Pila_sec1:
    __dim:int
    __cant:int
    __items:np.ndarray

    def __init__(self,dim):
        self.__dim = dim
        self.__tope = -1
        self.__items = np.empty(self.__dim,dtype=int)
        self.__cant = 0
    
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self,x):
        if self.__tope < self.__cant: #ERROR COMETIDO SELF.__DIMENSION
            self.__tope += 1
            self.__items[self.__tope] = x
            #ERROR COMETIDO SELF.__TOPE += 1
            self.__cant += 1
        else:
            print('Pila llena')

    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__tope]#Error cometido self.__tope+1
            #No decrementas el tope
            self.__tope -= 1
            self.__cant -= 1
        else:
            print('Pila vacia')
        return x
    
    def recorrer(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):#correccion range del tope(desde -1 hasta -1)
                print(self.__items[i])
        else:
            print('Pila vacia')