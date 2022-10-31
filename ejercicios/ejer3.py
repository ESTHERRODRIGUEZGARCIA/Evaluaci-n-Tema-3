#naves de Star Wars
#nombre, largo, tripulación y cantidad de pasajeros,

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


def naves_completas():
    nave1 = ejer3.Naves('Halcón Milenario', 178, 10, 50)
    nave2 = ejer3.Naves('Ala-X', 300, 20, 500)
    nave3 = ejer3.Naves('Destructor Estelar', 100, 10, 20)
    nave4 = ejer3.Naves('Lanzadera imperial', 30, 5, 15)
    nave5 = ejer3.Naves('Supremacy', 500, 20, 1000)
    nave6 = ejer3.Naves('Estrella de la Muerte', 5, 20, 100)

def mostrar_naves():
    #ealizar un listado ordenado por nombre de las naves de manera ascendente
    #y largo de las mismas de manera descendente
    lista_naves = [nave1, nave2, nave3, nave4, nave5, nave6]
    print("Se muestra la lista de naves... ")
    for i in range(len(lista_naves)):
        print(lista_naves[i].nombre, lista_naves[i].manejo)

def ordenar_naves():
    lst_naves = []
    for i in range(len(lista_naves)):
        lst_naves.append(lista_naves[i].nombre)
        lst_naves.sort()
        print("Las naves ordenadas por nombre: "\n, {lst_naves})
        


    #mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
    print(nave1)
    print(nave6)

    #• determinar cuáles son las cinco naves con mayor cantidad de pasajeros;

