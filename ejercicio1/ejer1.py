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


    



