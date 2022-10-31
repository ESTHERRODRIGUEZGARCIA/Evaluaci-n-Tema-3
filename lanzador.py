#ejer 4 print(Polinomio.resta)
from ejercicios import Polinomio, agregar_termino, dividir, mostrar, eliminar_termino, determinar_existe, resta



p1 = Polinomio()
agregar_termino(p1, 2, 1)
p2 = Polinomio()
agregar_termino(p2, 1, 2)
nuevo_pol = dividir(p2, p1)
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


