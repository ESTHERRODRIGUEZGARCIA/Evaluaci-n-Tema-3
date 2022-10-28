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
        if termino > polinomio.grado:
            aux.sig = polinomio.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    
        