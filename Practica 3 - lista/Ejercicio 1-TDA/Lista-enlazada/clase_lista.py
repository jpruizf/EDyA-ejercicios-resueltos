from clase_nodo import Nodo

class Lista:
    __cabeza:Nodo
    __cant:int

    def __init__(self):
        self.__cant = 0
        self.__cabeza = None

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nuevo = Nodo(x)
        if self.vacia():
            self.__cabeza = nuevo
            nuevo.setSiguiente(self.__cabeza)
            self.__cant += 1
        else:
            if self.__cabeza.getItems() <= nuevo.getItems():
                nuevo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevo
                self.__cant += 1
            else:
                aux = self.__cabeza
                anterior = self.__cabeza
                while aux != None and nuevo.getItems() > aux.getItems():
                    anterior = aux
                    aux = aux.getSiguiente()
                anterior.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                self.__cant += 1
                print('El elemento fue insertado en el centro')

    def suprimir(self,x):
        if self.vacia():
            print('Lista vacia')
        elif self.__cabeza.getItems() == x:
            aux = self.__cabeza
            dato = aux.getItems()
            self.__cabeza = self.__cabeza.getSiguiente()
            del aux
            self.__cant -= 1
        else:
            aux = self.__cabeza
            anterior = self.__cabeza
            while (aux != None and aux.getItems() != x):
                anterior = aux
                aux = aux.getSiguiente()
            if aux != None:
                dato = aux.getItems()
                anterior.setSiguiente(aux.getSiguiente())
                del aux
                self.__cant -= 1
        return dato
    def recuperar(self,x):
        aux = self.__cabeza
        indice = 0
        bandera = False
        while aux != None and not bandera:
            if x == indice:
                dato = aux.getItems()
                bandera = True
            else:
                aux = aux.getSiguiente()
                indice += 1
        if bandera is True:
            return dato
        else:
            print('No se encontro el elemento en la posicion ingresada')
    
    def buscar(self,x):
        aux  = self.__cabeza
        indice = 0
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                resultado = indice
                bandera = True
            aux = aux.getSiguiente()
            indice += 1
        if bandera is True:
            return resultado
        else:
            print('Elemento no encontrado')
    
    def recorrer(self):
        aux = self.__cabeza
        indice = 0
        while aux != None and indice < self.__cant:
            print(aux.getItems())
            aux = aux.getSiguiente()
            indice += 1
    
    def primer_elemento(self,x):
        if self.vacia():
            if self.__cabeza.getItems() == x:
                print(f'{x} Es el primer elemento de la lista')
        else:
            aux = self.__cabeza
            bandera = False
            while aux != None and not bandera:
                if x == aux.getItems():
                    print(f'{aux.getItems()} Es el primer elemento de la lista')
                    bandera = True
                else:
                    print(f'{x} No es el primer elemento de la lista')
                    aux = aux.getSiguiente()
    
    def ultimo_elemento(self,x):
        if self.__cabeza is None:
            if self.__cabeza.getItems() == x:
                print(f'{x} Es el ultimo elemento de la lista')
        else:
            aux = self.__cabeza
            bandera = False
            while aux != None and not bandera:
                if x == aux.getItems():
                    print(f'{aux.getItems()} Es el ultimo elemento de la lista')
                    bandera = True
                else:
                    print(f'{x} No es el ultimo elemento de la lista')
                    aux = aux.getSiguiente()

    def buscar_siguiente(self,x):
        aux  = self.__cabeza
        indice = 0
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                resultado = indice
                bandera = True
            aux = aux.getSiguiente()
            indice += 1
        if bandera is True:
            return resultado + 1
        else:
            print('Elemento no encontrado')
    
    def buscar_anterior(self,x):
        aux  = self.__cabeza
        indice = 0
        bandera = False
        while aux != None and not bandera:
            if aux.getItems() == x:
                resultado = indice
                bandera = True
            aux = aux.getSiguiente()
            indice += 1
        if bandera is True:
            return resultado - 1
        else:
            print('Elemento no encontrado')
