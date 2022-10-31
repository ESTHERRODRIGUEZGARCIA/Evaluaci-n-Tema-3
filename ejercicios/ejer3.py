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
    print("La lista de naves ordenadas por su nombre es: ", nombres)
lista_nombres()

def lista_largo():
    largo = []
    for row in reader:
        largo.append(row['largo'])
    largo.sort()