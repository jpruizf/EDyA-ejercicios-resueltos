class Estado:
    __escalones:int
    __solucines:str

    def __init__(self,e,s):
        self.__escalones = e
        self.__solucines = s

    def getEscalon(self):
        return self.__escalones
    
    def getSolucion(self):
        return self.__solucines