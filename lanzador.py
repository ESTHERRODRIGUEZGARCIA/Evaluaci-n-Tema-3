#ejer 4 print(Polinomio.resta)
from ejercicio4 import *
import sympy


def main4():

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
