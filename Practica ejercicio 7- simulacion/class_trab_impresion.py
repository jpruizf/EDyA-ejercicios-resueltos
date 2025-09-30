import random
class Trabajo_Impresion:
    __cant_pag:int
    __max_pag:int
    __llegada_trab:int
    __velocidad_imp:int
    __tiempo_max:int
    __paginas_restantes:int
    __tiempo_inicio:object
    __tiempo_espera:object

    def __init__(self,llegada):
        self.__cant_pag = random.randint(1, 18)
        self.__max_pag = 100
        self.__velocidad_imp = 10
        self.__llegada_trab = llegada
        self.__tiempo_max = 3
        self.__tiempo_inicio = None
        self.__tiempo_espera = None
    
    def reinicio_imporesora(self,tiempo_actual):
        self.__tiempo_inicio = tiempo_actual
        self.__tiempo_espera = self.__tiempo_inicio - self.__llegada_trab
    
    def getVelImpresion(self):
        return self.__velocidad_imp
    
    def setLLegadaTrab(self,actualizar):
        self.__llegada_trab = actualizar
    
    def setPaginasRes(self,paginas):
        self.__paginas_restantes = paginas

    def getTiempoEspera(self):
        return self.__tiempo_espera

    def getCantidadPag(self):
        return self.__cant_pag

    def getLLegada_Trabajo(self):
        return self.__llegada_trab
    
    def getTiempo_max(self):
        return self.__tiempo_max
    
    def traza(self):
        print(f'Valor paginas->{self.getCantidadPag()}\n|Valor llegada trabajo->{self.getLLegada_Trabajo()}\n|Valor tiempo maximo->{self.getTiempo_max()}\n|Valor tiempo espera->{self.getTiempoEspera()}\n|Valor velocidad impresion->{self.getVelImpresion()}\n')