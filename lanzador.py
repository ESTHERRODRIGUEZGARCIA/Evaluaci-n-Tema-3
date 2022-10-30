#ejer 4 print(Polinomio.resta)
from ejercicio4 import *
import sympy
from ejercicio4.Clases4 import *
from ejercicio4.funciones import *
from ejercicio1 import *

def main4():
    p1 = Polinomio()
    agregar_termino(p1, 2, 8)
    p2 = Polinomio()
    agregar_termino(p2, 2, 8)
    print(mostrar(p1))
    print(mostrar(p2))
    print(mostrar(resta(p1, p2)))
    print(mostrar(dividir(p1, p2)))
    print(determinar_existe(p1, 2))
    print(determinar_existe(p2, 2))
    eliminar_termino(p1, 2)
    eliminar_termino(p2, 2)
    print(mostrar(p1))
    print(mostrar(p2))









    print('Ejercicio 4')
    p1 = input("Primer Polinomio: ")
    p2 = input("Segundo Polinomio: ")
    print("\n")

    #Definimos los simbolos
    sympy.init_printing()
    x,y = sympy.symbols('x,y')

    #Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy
    Poly1 = sympy.Poly(p1)
    Poly2 = sympy.Poly(p2)

    print(Polinomio.resta)
    print(Polinomio.division)
    print(Polinomio.eliminar_termino)
    print(Polinomio.determinar_existe)


def elegir():
    ejercicio1.