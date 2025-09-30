from clase_simulacion import Simulacion
import random
def test():
    s = Simulacion()
    pendientes = s.ejecutar()
    print(f'Trabajos pendientes->{pendientes}')
if __name__ == '__main__':
    test()