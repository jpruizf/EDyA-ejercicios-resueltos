from clase_pila1 import Pila_1

class Tablero:
    __tablero:list
    __fichas:int
    __movimientos:int
    def __init__(self,n):
        self.__tablero = [Pila_1(n),Pila_1(n),Pila_1(n)]
        self.__fichas = n
        self.__movimientos = 0
    def mover_disco(self,origen,destino):
        origen_pila = self.__tablero[origen]
        destino_pila = self.__tablero[destino]
        disco = origen_pila.getCant()
        while destino_pila.getCant() != self.__fichas:
            if origen == 1:
                destino_pila.insertar(disco)
                origen_pila.suprimir()
                self.__movimientos += 1
                destino_pila.mostrar()
                print('Movimiento exitoso')
            else:             
                origen -= 1
                destino_pila.insertar(disco)
                origen_pila.suprimir()
                self.__movimientos += 1
                destino_pila.mostrar()
                print('Movimiento valido exitoso')

        if destino_pila.getCant() == self.__fichas:
            print('Fin del juego')
        return self.__movimientos
