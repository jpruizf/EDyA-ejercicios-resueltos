class Nodo:
    __contacto:object
    __siguiente:object

    def __init__(self):
        self.__contacto = None
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def setContacto(self,UnContacto):
        self.__contacto = UnContacto
    
    def getDatosContacto(self):
        return self.__contacto