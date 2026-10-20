from abc import ABC, abstractmethod

class NaveEspacial(ABC): #no se puede instanciar cuando es abstracto
    modelo: str
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def despegar(self):
        pass

class NaveCapsula(NaveEspacial): 
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "Despega con motores de Capsule Corp")

class NaveSaiyajin(NaveEspacial):
    def __init__(self, modelo: str):
        super().__init__(modelo)

    def despegar(self):
        print(self.modelo, "Despega inmediata")

nave_bulma = NaveCapsula("Nave Bulma")
nave_vegeta = NaveSaiyajin("Capsula Sayijin")
nave_bulma.despegar()
nave_vegeta.despegar()

