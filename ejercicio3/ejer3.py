#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
from naves import *
class Naves(object):
    def __init__(self, nombre:str, largo:float, tripul:int, pasajeros:int):
        self.nombre = nombre
        self.largo = largo
        self.tripul = tripul
        self.pasajeros = pasajeros

    def __str__(self):
        return f"{self.nombre}, {self.largo}, {self.tripul}, {self.pasajeros}"

    def represent(self):
        rep = {'Nombre':self.nombre, 'Largo':self.largo, 'Tripulación':self.trip, 'Pasajeros':self.pasajeros}
        return rep
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_largo(self, largo):
        self.largo = largo
    def set_tripulación(self, tripul):
        self.tripul = tripul
    def set_pasajeros(self, pasajeros):
        self.pasajeros = pasajeros

    def get_nombre(self):
        return self.nombre
    def get_largo(self):
        return self.largo
    def get_tripulación(self):
        return self.tripul
    def get_pasajeros(self):
        return self.pasajeros


class Game(object):

    def lista(self):
        listan = []
        for i in listan:
            listan.append(self.nombre)
            listan.sort()
        print(listan)

        listal = []
        for i in listal:
            listal.append(self.largo)
        print(listal)




