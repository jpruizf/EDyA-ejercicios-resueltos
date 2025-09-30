class Estado:
    __cadena:str
    __escalon:int

    def __init__(self,esc,cadena):
        self.__cadena = cadena
        self.__escalon = esc

    def getEscalon(self):
        return self.__escalon
    
    def getMensaje(self):
        return self.__cadena
    
    def __str__(self):
        return self.getMensaje()