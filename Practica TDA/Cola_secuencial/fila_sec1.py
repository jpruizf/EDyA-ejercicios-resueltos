import numpy as np

class Cola_Sec1:
    __items:np.ndarray
    __dimension:int
    __ul:int

    def __init__(self,dim):
        self.__dimension = dim
        self.__ul = 0
        self.__items = np.empty(self.__dimension,dtype=int)
    
    def vacia(self):
        return self.__ul == 0
    
    def insertar(self, x, indice):
        if self.__dimension < self.__ul:
            print('Fila llena')
        else:
            self.__items[indice] = x
            self.__ul -= 1
    
    def  suprimir(self):
        #error i = ul
        if not self.vacia():
            x = self.__items[self.__ul]
            self.__ul -= 1
            #error al definir i ya que i -= 1 queda por fuera del arreglo
        else:
            print('Fila vacia')
        return x
    def recorrer(self):
        if not self.vacia():
            for i in reversed(self.__items):
                print(f'Numeros->{i}')
                #i=self.__ul-1 error de redundancia 