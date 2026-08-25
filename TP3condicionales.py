#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")


#Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprodo")


#Ejercicio 3
numero = int(input("Ingrese un número par: "))
a = numero % 2
if a == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 12:
    print("Eres Niño/a")
elif edad >= 12 and edad < 18:
    print("Eres Adolescente")
elif edad >= 18 and edad < 30:
    print("Eres Adulto/a joven")
else:
    print("Eres Adulto/a")


#Ejercicio 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
a = len(contraseña)
if a >= 8 and a <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Los valores no siguen un patrón")

print("La moda es:",moda)
print("La media es:",media)
print("La mediana es:",mediana)


#Ejercicio 7
palabra = input("Ingrese una palabra o una frase: ")
a = palabra[-1].lower()
if a in "aeiou":
    print(f"{palabra}!") 
else:
    print(palabra)


#Ejercicio 8
nombre = input("Ingrese su nombre: ")
a = nombre.upper()
b = nombre.lower()
c = nombre.title()
print("Escriba un número del 1 al 3, eligiendo que opcion prefriere: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("2. Si quiere su nombre con la primer letra en mayúsculas. Por ejemplo: Pedro.")
numero = int(input("Ingrese el numero: "))
if numero == 1:
    print(a)
elif numero == 2:
    print(b)
elif numero == 3:
    print(c)
else:
    print("Por favor, ingrese un número del 1 al 3")


#Ejercicio 9
magnitud = float(input("Ingrese la magnitud de un terremeto: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("Ingrese una magnitud por favor.")


#Ejercicio 10 
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")

elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")

elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")

elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")