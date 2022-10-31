#ejer 4 print(Polinomio.resta)
from ejercicios.ejer4 import Polinomio, agregar_termino, division, mostrar, eliminar_termino, determinar_existe, resta

def main4():
    p1 = Polinomio()
    agregar_termino(p1, 2, 8)
    p2 = Polinomio()
    agregar_termino(p2, 1, 2)

    print("Mostrar ambos polinomios:")
    print(mostrar(p1))
    print(mostrar(p2))

    print("Mostrar su resta:")
    print(mostrar(resta(p1, p2)))

    print("Mostrar su división:")
    print(mostrar(division(p1, p2)))

    print("Determinar si existe el término en cada polinomio: ")
    print(determinar_existe(p1, 2))
    print(determinar_existe(p2, 2))

    
    eliminar_termino(p1, 2)
    eliminar_termino(p2, 2)

    print("Mostrar de nuevo cada polinomio:")
    print(mostrar(p1))
    print(mostrar(p2))
main4()