#matrix 3x3


print ("Ingrese los valores: \n |a00 a01 a02|\n |a10 a11 a12| \n |a20 a21 a22|")
# defino los valores del la matriz
a00 = float(input('Ingrese el valor a00: '))
a01 = float(input('Ingrese el valor a01: '))
a02 = float(input('Ingrese el valor a02: '))
a10 = float(input('Ingrese el valor a10:'))
a11 = float(input('Ingrese el valor a11: '))
a12 = float(input('Ingrese el valor a12: '))
a20 = float(input('Ingrese el valor a20: '))
a21 = float(input('Ingrese el valor a21: '))
a22 = float(input('Ingrese el valor a22: '))

#hago los cálculos para calcular el determinante por Sarrus
total1=a00*a11*a22 + a10*a21*a02 +a20*a01*a12
total2=total1+(a02*a11*a20)*-1 + (a12*a21*a00)*-1 + (a22*a01*a10)*-1



print("El determinante de la matriz ")
print("|",a00, a01, a02,"|")
print("|",a10, a11, a12,"|")
print("|",a20, a21, a22,"|")
print("es: ",total2)








