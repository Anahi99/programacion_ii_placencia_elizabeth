class Guerrero: 
    nombre: str
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        self.poder_inicial = poder_inicial
        self.horas = horas
        self.nombre = nombre

    def atacar(self):
        print(f"{self.nombre} realiza un ataque")

    def calcular_poder(self):
        return self.poder_inicial
    
class Goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "Utiliza Kamehameha")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*100 

class Vegeta(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas: int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(self.nombre, "Utiliza final flash")

    def calcular_poder(self):
        return self.poder_inicial + self.horas*150 

goku = Goku("Gran Goku", 150, 50)
vegeta = Vegeta("Vegeta", 200 , 80)
goku.atacar()
vegeta.atacar()
print(goku.calcular_poder())
print(vegeta.calcular_poder())


