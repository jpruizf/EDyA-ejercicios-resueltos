from class_simulacion import Simulacion


def test():
    s = Simulacion()
    s.procesar_trabajo()
    sin_atender = s.activar_proceso()
    print(f'Total de trabajos sin atender:{sin_atender}')
    print(s.getReloj())
    s.getTraza()





if __name__ == '__main__':
    test()