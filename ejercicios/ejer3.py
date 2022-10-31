#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
import csv

with open('naves_sw.csv', 'r') as file:
    print("Se muestra la lista de naves para este ejercicio:")
    reader = csv.DictReader(file, delimiter=';')
    naves_starwars = list(reader)
    for row in reader:
        print(row)

def lista_nombres():
    nombres = []
    for row in naves_starwars:
        nombres.append(row['nombre'])
    nombres.sort()
    print("La lista de naves ordenadas por su nombre es: ", {nombres})



