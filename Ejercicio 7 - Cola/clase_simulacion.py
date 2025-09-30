from clase_fila import Cola_Circular
from clase_impresora import TrabajoImpresion
class Simulacion:
    __reloj:int
    __tiempo_simulacion:int
    __tiempo_llegada:int
    __velocidad_imp:int
    __tiempo_max_imp:int
    __impresora_ocupada:bool
    __fila:Cola_Circular
    __trabajos_impresos:list
    __trabajos_sin_atender:int
    __total_espera:int
    __contar_trabajos:int
    __id:int

    def __init__(self):
        self.__reloj = 0
        self.__tiempo_simulacion = 60
        self.__tiempo_llegada = 5
        self.__velocidad_imp = 10
        self.__tiempo_max_imp = 3
        self.__impresora_ocupada = False
        self.__fila = Cola_Circular(100)
        self.__trabajos_impresos = []
        self.__trabajos_sin_atender = 0
        self.__total_espera = 0
        self.__contar_trabajos = 0
        self.__id = 1
    
    def generar_trabajo(self):
        Untrabajo = TrabajoImpresion(self.__id,self.__reloj)
        self.__fila.insertar(Untrabajo)
        self.__id += 1
    
    def procesar_trabajo(self):
        trabajo = TrabajoImpresion(self.__id,self.__reloj)
        if not self.__fila.vacia():
            self.__fila.suprimir()
            trabajo.registro_inicio(self.__reloj)
            tiempo_impresion = trabajo.getPaginasRestantes() / self.__velocidad_imp

            if tiempo_impresion <= self.__tiempo_max_imp:
                self.__trabajos_impresos.append(trabajo)
                self.__total_espera += trabajo.getTiempoEspera()
                self.__contar_trabajos += 1
            else:
                paginas_restantes = trabajo.getPaginasRestantes() - (self.__tiempo_llegada * self.__velocidad_imp)
                trabajo.registro_inicio(paginas_restantes)
                trabajo.setTiempollegada(self.__reloj)
                self.__fila.insertar(trabajo)
    
    def ejecutar(self):
        while self.__reloj < self.__tiempo_simulacion:
            if self.__reloj % self.__tiempo_llegada == 0:
                self.generar_trabajo()
            
            self.procesar_trabajo()
            self.__reloj += 1

        espera_promedio = self.__total_espera / self.__contar_trabajos if self.__contar_trabajos > 0 else 0
        print(f'Espera promedio->{espera_promedio}')
        trabajo_pendientes = self.__fila.getCant()
        return trabajo_pendientes