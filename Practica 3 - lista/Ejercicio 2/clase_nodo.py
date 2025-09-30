class Nodo:
    __items:object
    __siguiente:object

    def __init__(self,num):
        self.__items = num
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        if siguiente is not None and isinstance(siguiente,Nodo):
            raise TypeError('Debe ser si o si un Nodo o None')
        else:
            self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setItems(self,num):
        self.__items = num
        
    def getItems(self):
        return self.__items