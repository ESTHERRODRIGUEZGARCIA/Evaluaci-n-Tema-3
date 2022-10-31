
import re
from ejercicios import ejer1, ejer2, ejer3


def ejecutar():
    eleccion = int(input('¿Qué ejercicio 1-5 desea ejecutar? \nPara finalizar introduzca 6. '))
    if eleccion == 1:
        ejer1()
    elif eleccion == 2:
        ejer2()
    elif eleccion == 3:
        ejer3()
    elif eleccion == 4:
        pass
    elif eleccion == 5:
        pass
    elif eleccion == 6:
        print("Finished. ")

