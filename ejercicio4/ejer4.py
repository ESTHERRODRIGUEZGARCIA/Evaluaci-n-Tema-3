from wsgiref.validate import validator
import sympy

#Obtenes los dos polinomios introducidos por el usuario
P1 = input("Primer Polinomio: ")
P2 = input("Segundo Polinomio: ")
print("\n")

#Definimos los simbolos
sympy.init_printing()
x,y = sympy.symbols('x,y')

#Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy
Poly1 = sympy.Poly(P1)
Poly2 = sympy.Poly(P2)

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

    def resta(p1, p2):
        paux = Polinomio()
        mayor = p1 if (p1.grado > p2.grado) else p2
        for i in range(0, mayor.grado+1):
            total = obtener_valor(p1, i) - obtener_valor(p2, i) 
            if total != 0:
                agregar_termino(paux, i, total)
        return paux



    def division(p1, p2):
        paux = Polinomio()
        pol1 = p1.termino_mayor

        while pol1 is not None:
            pol2 = p2.termino_mayor
            while pol2 is not None:
                termino = pol1.info.termino - pol2.info.termino
                valor = pol1.info.valor // pol2.info.valor
                if obtener_valor(paux, termino) !=0:
                    valor += obtener_valor(paux,termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                    pol2 = pol2.sig
                pol1 = pol1.sig
            return paux
        
        
print(Polinomio.resta)