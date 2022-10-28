#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,
class Naves(object):
    def __init__(self, nombre:str, largo:float, tripul:int, pasajeros:int):
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

nave1 = Naves('Nave Esther', 178, 10, 50)
nave2 = Naves('Nave Teresa', 300, 20, 500)
nave3 = Naves('Nave UAX', 100, 10, 20)