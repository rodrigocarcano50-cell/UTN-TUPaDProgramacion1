#Actividad 1 
print("Hola Mundo!")




#Actividad 2
a = input("Ingrese su nombre:")
print(f"Hola {a}!")




#Actividad 3
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")




#Actividad 4
pi = 3.1416
radio = int(input("Ingrese el radio de un circulo:"))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El area de tu circulo es {area} y el prerimetro es {perimetro}")




#Activiad 5
segundos = int(input("Ingrese una cantidad de segundos:"))
hora = 1
segundosHora = 3600
resultado = hora /segundosHora * segundos
print(f"Los segundos equivalen a {resultado} en horas.")




#Actividad 6
numero = int(input("Ingrese un numero para sacar la tabla de multiplicacion:"))
for a in range(1,11):
    resultado = numero * a
    print(f"{numero} x {a} = {resultado}")




#Actividad 7
numero1 = int(input("Ingrese un numero que no sea 0:"))
numero2 = int(input("Ingrese un numero que no sea 0:"))
suma = numero1 + numero2
print(f"La suma de los numeros es {suma}")
division = numero1 / numero2
print(f"La division de los numeros es {division}")
multiplicacion = numero1 * numero2
print(f"La multiplicacion de los numeros es {multiplicacion}")
resta = numero1 - numero2
print(f"La resta de los numeros es {resta}")




#Actividad 8
peso = int(input("Ingrese su peso en KG:"))
altura = float(input("Ingrese su altura en Metros:"))
imc = peso / (altura ** 2)#
print(f"Su indice de masa corporal es {imc}")




#Actividad 9
celsius = int(input("Ingrese una temperatura en grados Celsius:"))
fahrenheit = 9 / 5 * celsius + 32
print(f"La temperatura en Fahrenheit es {fahrenheit}°F")#




#Actividad 10
n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese un numero:"))
n3 = int(input("Ingrese un numero:"))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio de esos numeros es {promedio}")