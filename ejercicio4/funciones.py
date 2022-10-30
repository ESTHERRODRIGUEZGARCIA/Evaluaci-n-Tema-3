from Clases4 import *
from wsgiref.validate import validator

def agregar_termino(self, valor, termino, polinomio):
        aux = Nodo()
        dato = datoPolinomio(self.valor, termino)
        aux.info = dato
        if termino > polinomio.grado:
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

def modificar_termino(polinomio, termino):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino != termino:
        aux = aux.sig
    aux.info.valor = validator


def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino == termino:
        aux = aux.sig
    if aux is not None and aux.infi.termino == termino:
        return aux.info.valor
    else:
        return 0

def mostrar(polinomio):
    aux = polinomio.termino_mayor
    pol = ''
    if aux is not None:
        while aux is not None:
            signo += ''
            if aux.info.valor >= 0:
                signo += '+'
            pol += signo + str(aux.info.valor) + "x^"+ str(aux.info.termino)
            aux = aux.sig
    return pol