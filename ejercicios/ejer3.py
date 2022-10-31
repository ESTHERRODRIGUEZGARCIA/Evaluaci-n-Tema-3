#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
import csv

with open('naves_sw.csv', 'r') as file:
    print("Se muestra la lista de naves para este ejercicio:")
    reader = csv.DictReader(file, delimiter=';')
    starwars = []
    for row in reader:
        starwars.append(row)
    print(starwars)

def lista_nombres():
    nombres = []
    for i in starwars:
        nombres.append(i['Nombre'])
    nombres.sort()
    print("\n\nLa lista de naves ordenadas por su nombre es: ", nombres)
lista_nombres()

def lista_largo():
    largo = []
    for i in starwars:
        largo.append(int(i['Largo']))
    largo.sort()
    largo.reverse()
    print("\n\nLa lista de naves ordenada por longitud es: ", largo)
lista_largo()

def lista_inf():
    for i in starwars:
        if i['Nombre'] == "Halcon Milenario":
            print("\n\nInformación sobre Halcón Milenario: ",i )
        elif i['Nombre'] == "Estrella de la Muerte":
            print("\n\nInformación sobre Estrella de la Muerte: ",i)
lista_inf()

def mayor_pasajeros():
    naves5 = []
    for i in starwars:
        naves5.append(i['Nombre'] + ' ' + i['Pasajeros'])
        naves5.sort()
        naves5.reverse()
    print("\n\nLas cinco naves con mayor cantidad de pasajeros son: ", naves5[:5])
mayor_pasajeros()

def mayor_tripul():
    tripulacion = []
    for i in starwars:
        tripulacion.append(int(i['Tripul']))
    tripulacion.sort()
    tripulacion.reverse()
    for i in starwars:
        if int(i['Tripul']) == tripulacion[0]:
            print("\n\nLa nave que necesita mayor cantidad de tripulación es: ", i['Nombre'])

mayor_tripul()

def naves_at():
    at = []
    for i in starwars:
        if i['Nombre'][:2] == 'AT':
            at.append(i['Nombre'])
    print("\n\nLista de naves que empieza por AT:", at)
naves_at()

def seis_pasajeros():
    pasajeros = []
    for i in starwars:
        if int(i['Pasajeros'])>= 6:
            pasajeros.append(i['Nombre'])
    print("\n\nLas naves que pueden llevar seis o más pasajeros son: ", pasajeros)
seis_pasajeros()

def nave_peque():
    peque = []
    for i in starwars:
        if i['Nombre'] == 'PE':
            peque.append(i['Nombre'])



def nave_peque():
    peque = []
    for i in starwars:
        peque.append(int(i['Largo']))
    peque.sort()
    for i in starwars:
        if int(i['Largo']) == peque[0]:
            print("\n\nLa nave más pequeña es: ", i['Nombre'])

nave_peque()

def nave_grande():
    grande = []
    for i in starwars:
        grande.append(int(i['Largo']))
    grande.sort()
    grande.reverse()
    for i in starwars:
        if int(i['Largo']) == grande[0]:
            print("La nave más grande es: ", i['Nombre'])
nave_grande()


