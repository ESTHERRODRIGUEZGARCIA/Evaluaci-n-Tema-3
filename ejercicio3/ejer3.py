#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
from naves import *
class Naves(object):
    def __init__(self, nombre:str, largo:float, tripul:int, pasajeros:int):
        self.nombre = nombre
        self.largo = largo
        self.tripul = tripul
        self.pasajeros = pasajeros

    def lista(self):
        listan=[]
        listan.append(self.nombre)
        listan.sort()
        print(listan)

        listal = []
        listal.append(self.largo)
        listal = sorted(reverse = True)
        print(listal)


