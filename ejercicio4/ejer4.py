class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(self, valor, termino, polinomio):
        aux = Nodo()
        dato = datoPolinomio(self.valor, termino)
        aux.info = dato
        