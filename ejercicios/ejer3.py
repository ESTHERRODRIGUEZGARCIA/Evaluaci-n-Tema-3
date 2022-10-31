#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
import csv

with open('naves_sw.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(row)
