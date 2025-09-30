class Nodo:
    __item:int
    __siguiente:object

    def __init__(self,number):
        self.__item = number
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getItem(self):
        return self.__item