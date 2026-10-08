#Condicional if
#Simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")

#Condicional if-else

creditos = int(input("Ingresa la cantidad de créditos: "))
precio_repuesto = int(input("Ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No puedes comprar el repuesto")

#if anidado
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran créditos")
    else:
        print("No te sobran créditos")
else:
    print("No puedes comprar el repuesto")

#Condicional if-elif-else
if creditos > precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto pero no te sobran créditos")
else:       
    print("No puedes comprar el repuesto")

tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("El repuesto es un motor")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("El repuesto es un ala")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("El repuesto es un escudo")
else:
    print("El repuesto no es válido")