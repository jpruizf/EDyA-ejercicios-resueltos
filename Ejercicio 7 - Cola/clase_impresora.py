import random
class TrabajoImpresion:
    __id:int
    __paginas:int
    __paginas_restante:int
    __tiempo_llegada:int
    __tiempo_inicio:int
    __tiempo_espera:int

    def __init__(self,idx,tiempo_llegada):
        self.__id = idx
        self.__paginas = random.randint(1, 18)
        self.__paginas_restante = self.__paginas
        self.__tiempo_llegada = tiempo_llegada
        self.__tiempo_inicio = None
        self.__tiempo_espera = None

    def registro_inicio(self, tiempo_actual):
        self.__tiempo_inicio = tiempo_actual
        self.__tiempo_espera = self.__tiempo_inicio - self.__tiempo_llegada
        return self.__tiempo_espera
    
    def getPaginasRestantes(self):
        return self.__paginas_restante
    
    def getTiempoEspera(self):
        return self.__tiempo_espera
    
    def getTiempollegada(self):
        return self.__tiempo_llegada
    
    def setTiempollegada(self,llegada):
        self.__tiempo_llegada = llegada