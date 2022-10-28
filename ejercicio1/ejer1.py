#Torre de Hanoi

def movimiento(tf, td):
    global torres
    texto = str(torres[tf][-1])+ '=' + tf + '=>' + td 
    torres[td].append(torres[tf][-1])

    del torres[tf][-1]
    movimiento.append(texto)

def validar(tf, td):
    try:
        if torres[tf] != []:
            if torres[td] == []:
                return True
            elif torres[tf][-1] < torres[td][-1]:
                return True
            else:
                return False

    except:
        return False


def out():
    for i  in range(num-1,-1,-1):
        try:
            a = torres['A'][i]
        except:
            a = '|'
        try:
            b = torres['B'][i]
        except:
            b = '|'
        try:
            c = torres['C'][i]
        except:
            c = '|'
        print("   ", a, "   ", b, "   ", c, sep="")
    print("--------------------------\n    A    B    C")

print(" Instrucciones: \n Para realizar un movimiento hay que escribir en mayusculas la letra de la torre en la que esta la ficha seguida de la letra de la torre a donde quieres moverla ficha. Ejemplo: AB")
print("El numero de fichas indica la altura que tendrá la torre. ")
print(" Si quieres salir del juego pulsa 'q'. \n")



