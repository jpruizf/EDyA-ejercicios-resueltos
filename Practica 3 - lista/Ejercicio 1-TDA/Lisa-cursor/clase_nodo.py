
class Nodo:
    __items:int
    __siguiente:int

    def __init__(self,num,indice = -1):
        self.__items = num
        self.__siguiente = indice

    def setSiguiente(self,indice):
        self.__siguiente = indice

    def getSiguiente(self)->int:
        return self.__siguiente
    
    def getItems(self):
        return self.__items
