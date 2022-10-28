#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
class Naves(object):
    def __init__(self, nombre:str, largo:float, tripul:str, pasajeros:int):
        self.nombre = nombre
        self.largo = largo
        self.tripul = tripul
        self.pasajeros = pasajeros

    def lista(self):
        listan=[]
        listan.append(self.nombre)
        print(listan)
        listal = []
        listal.append(self.largo)
        print(listal)
        
