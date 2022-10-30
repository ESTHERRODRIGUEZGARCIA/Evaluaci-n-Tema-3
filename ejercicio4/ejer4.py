import sympy
from Clases4 import *
from ejercicio4.funciones import *

#Obtenes los dos polinomios introducidos por el usuario
p1 = input("Primer Polinomio: ")
p2 = input("Segundo Polinomio: ")
print("\n")

#Definimos los simbolos
sympy.init_printing()
x,y = sympy.symbols('x,y')

#Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy
Poly1 = sympy.Poly(p1)
Poly2 = sympy.Poly(p2)


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

def eliminar_termino(polinomio, termino):
    pol1 = polinomio.termino_mayor
    while pol1 is not None:
        