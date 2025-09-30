from clase_fila import Fila_Circular
from class_trab_impresion import Trabajo_Impresion
class Simulacion:
    __fila_trabajos:Fila_Circular
    __tiempo_simulacion:int
    __prom_espera:int
    __tiempo_impresion:int
    __trabajos_sin_atender:int
    __reloj:int
    __cont_trab:int
    __impresion:Trabajo_Impresion
    __total_espera:int
    def __init__(self):
        self.__reloj = 0
        self.__fila_trabajos = Fila_Circular(100)
        self.__tiempo_simulacion = 60
        self.__prom_espera = 0
        self.__trabajos_sin_atender = 0
        self.__cont_trab = 0
        self.__tiempo_impresion = 0
        self.__impresion = Trabajo_Impresion(0)
        self.__total_espera = 0
    
    def getReloj(self):
        return self.__reloj
    
    def getTiempo(self):
        return self.__tiempo_simulacion
    
    def getTotalEspera(self):
        return self.__total_espera
    
    def getTiempoImpresion(self):
        return self.__tiempo_impresion
    
    def getSinAtender(self):
        return self.__trabajos_sin_atender
    
    def setSinAtender(self,total):
        self.__trabajos_sin_atender = total
    def getTotalTrabajos(self):
        return self.__cont_trab
    
    def setPromEspera(self,valor):
        self.__prom_espera = valor

    def getPromEspera(self):
        return self.__prom_espera
    
    def cargar_trabajo(self)->None:
        Untrabajo = Trabajo_Impresion(self.getReloj())
        self.__fila_trabajos.insertar(Untrabajo)
        self.__cont_trab += 1
    def getTraza(self):
        self.__impresion.traza()
    def procesar_trabajo(self)->None:
        if not self.__fila_trabajos.vacia():
            self.__fila_trabajos.suprimir()
            self.__impresion.reinicio_imporesora(self.getReloj())
            self.__tiempo_impresion = self.__impresion.getCantidadPag() - (self.__impresion.getLLegada_Trabajo() / self.__impresion.getVelImpresion())
            self.__cont_trab += 1

            if self.getTiempoImpresion() < self.getTiempo():
                self.__total_espera += self.getTiempoImpresion()
                self.__cont_trab += 1
            else:
                paginas_restantes = self.__impresion.getCantidadPag() - (self.__impresion.getLLegada_Trabajo() * self.__impresion.getVelImpresion())
                self.__impresion.setPaginasRes(paginas_restantes)
                self.__impresion.reinicio_imporesora(paginas_restantes)
                self.__impresion.setLLegadaTrab(self.__reloj)
                self.__fila_trabajos.insertar(self.__impresion.getLLegada_Trabajo())
        else:
            print('Fila vacia')
    
    def activar_proceso(self):
        while self.getReloj() < self.getTiempo():
            if self.getReloj()%self.__impresion.getCantidadPag() == 0:
                self.cargar_trabajo()
            self.procesar_trabajo()
            self.__reloj += 1
        if self.__cont_trab > 0:
            promedio = self.__total_espera / self.__cont_trab
            self.setPromEspera(promedio)
        else:
            promedio = 0
        print(f'Tiempo de espera promedio->{self.getPromEspera()}')
        self.setSinAtender(self.__impresion.getCantidadPag())
        return self.getSinAtender()