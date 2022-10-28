#Torre de Hanoi

def movimiento(tf, td):
    global torres
    texto = str(torres[tf][-1])+ '=' + tf + '=>' + td 
    torres[td].append(torres[tf][-1])

    del torres[tf][-1]
    movimiento.append(texto)



