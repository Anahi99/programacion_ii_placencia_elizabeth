#ciclo for

naves = [ "Caza N-1",
         "Nave real de Naboo",
         "Transporte"
         ]
for nave in naves:
    print("Inspeccionando ", nave)
print("Inspección completa")

rondas = range(1, 6)

print("Tipo de Rondas:", type(rondas))
for ronda in rondas:
    print(f"Ronda vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")

droides = range(1,17, 2) #SE SALTA 2 NUMEROS HASTA EL 17

print("Tipo de Droides:", type(droides))
for droide in droides:
    print(f"Reparar: droide B1-{droide}")
    print(f"Tipo de dato droide: {type(droide)}")

planetas = ["Tatooine", 
            "Naboo", 
            "Coruscant"
            ]
recorrido = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipo de dato {type(posicion)} : {type(planeta)}")

paises = ["Ecuador",
          "Venezuela",
          "Chile",
          "Colombia",
          "Brasil",
          "Estados Unidos"
          ]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"País visitado: {pais}")

jedi = {}
jedi_activo = { 
    "nombre": "Luke Skywalker",
    "fuerza": "120",
    "estilo": "Caballero Jedi",
    "mision": [" Rescatar a la princesa Leia", "Derrotar al Imperio Galáctico", "Restaurar la paz en la galaxia"],
    "descripcion": {
        "estatura": "1.72 m",
        "especie": "Humano"
    }
}  
print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad=8, turbo_laser=2)
print(nave)

jedi ["nombre"] = "Obi-Wan Kenobi"
jedi ["fuerza"] = "100"
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave}: {valor}")