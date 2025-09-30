class Nodo:
    __items:object
    __siguiente:object

    def __init__(self, xnum):
        self.__items = xnum
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getItems(self):
        return self.__items