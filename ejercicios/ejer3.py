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
        largo.append(i['Nombre']+ ', ' + i['Largo'])
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