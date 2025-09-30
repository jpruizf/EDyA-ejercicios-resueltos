class Contacto:
    __numero:int
    __nombre:str

    def __init__(self,num,nom):
        self.__numero = num
        self.__nombre = nom
    
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    