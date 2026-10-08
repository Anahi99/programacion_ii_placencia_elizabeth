#string cadenas de caracteres
jedi = "Luke Skywalker"
aprendiz = "Obi-Wan Kenobi"
droid = "R2-D2"
planeta = "Tatooine"
codigo = "327"

print("El jedi es:" + jedi)
print("El jedi" , type(jedi))
print("El aprendiz es:" + aprendiz)
print("El aprendiz" , type(aprendiz))
print("El droid es:" + droid)
print("El droid" , type(droid))
print("El planeta es:" + planeta)
print("El planeta" , type(planeta)) 
print("El codigo es:" +  codigo)
print("El codigo" , type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre del jedi es:" + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:" + str(longitud_aprendiz))

#mayusculas y minusculas
mensaje = "La federacion de comercio ha establecido un bloqueo en tatooine"
print("El mensaje es:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayusculas es:" + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minusculas es:" + mensaje_minusculas)

#reemplazar palabras en un string
comunidad = "Los jedi son enviados a Tatooine"
print("El mensaje es:" + comunidad)
nuevo_mensaje = comunidad.replace("Tatooine", "Naboo")
print("El nuevo mensaje es:" + nuevo_mensaje)

#Listas de strings
planetas = "Tatooine, Naboo, Coruscant, Alderaan"
planetas_lista = planetas.split(", ") #como lo separas
print(planetas_lista)
print("Los planetas son:" + str(planetas_lista))    
print("El primer planeta es:" + planetas_lista[0]) #muestra el primer elemento de la lista

droids = "R2-D2"
print("El droid es:" + droids)
print("El primer caracter del droid es:" + droids[0]) #muestra el primer caracter del string
print("El segundo caracter del droid es:" + droids[1]) #muestra el segundo caracter del string
print("El tercer caracter del droid es:" + droids[2]) #muestra el tercer caracter del string
print("El cuarto caracter del droid es:" + droids[3]) #muestra el cuarto caracter del string
print("El quinto caracter del droid es:" + droids[4]) #muestra el quinto caracter del string
print("El sexto caracter del droid es:" + droids[-1]) #muestra el ultimo caracter del string

planeta = "Tatooine"
print("El planeta es:" + planeta)   
print("El planeta sin espacios es:" + planeta.strip()) #elimina los espacios al inicio y al final del string
