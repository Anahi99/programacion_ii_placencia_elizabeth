droides = [
    {
        "codigo": "B1-001",
        "Modelo": "B1",
        "Energia": 90,
        "Activo": True
    },
    {
        "codigo": "B1-002",
        "Modelo": "B1",
        "Energia": 40,
        "Activo": False
    },
    {
        "codigo": "B1-001",
        "Modelo": "Droideka",
        "Energia": 80,
        "Activo": True
    },
]
cantidad_droides = len(droides)
print(cantidad_droides)
nuevo_droide = {
    "codigo": "B1-004",
    "Modelo": "B1",
    "Energia": 80,
    "Activo": True
}
#create
droides.append(nuevo_droide)
print(len(droides))
print(droides)
#read
droide = droides[0]
print(f"codigo:{droide["codigo"]}")
print(f"Modelo:{droide["Modelo"]}")
print(f"Energia:{droide["Energia"]}")
print(f"Activo:{droide["Activo"]}")
#update
droide = droides[2]
droide["codigo"]= "DR0-002"
droide["energia"]= 85
droide["activo"]= False
print(f"droides : {droides}")
#delete
eliminado = droides.pop(2)
print(f"droides : {droides}")



