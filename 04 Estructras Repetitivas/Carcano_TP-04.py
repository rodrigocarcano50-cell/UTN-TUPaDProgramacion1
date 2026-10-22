#Ejercicio 1
for i in range(0,101,1):
    print(i)


#Ejercicio 2
n = int(input("Ingrese un número entero: "))
cont = 0
while n > 0.99:
    n = n / 10
    cont += 1
print(f"El número ingresado tiene {cont} digitos.")


#Ejercicio 3
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(n1+1,n2):
    suma += i
print("La suma de todos los numeros enteros comprendidos entre los dos valores es",suma)


#Ejercicio 4
resultado = 0
n = -1
print("Ingrese números enteros para sumar(para frenar ingrese 0)")
while n != 0:
    n = int(input("Ingrese un número: "))
    resultado += n
print("El resultado es: ",resultado)


#Ejercicio 5
import random 
numero_aleatorio = random.randint(1,9)
numero_usuario = int(input("Adivina un  número del 1 al 9: "))
cont = 1
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Incorrecto. Intenta con otro numero: "))
    cont += 1
print(f"Correcto. Adivinaste el número en {cont} intentos.")


#Ejercicio 6
for i in range(100,-1,-2):
    print(i)


#Ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0,n+1):
    suma += i
print("La suma de todos los numeros enteros comprendidos entre 0 y el número ingresado es",suma)


#Ejercicio 8
n_pares = 0
n_impares = 0
n_negativos = 0
n_positivos = 0
for i in range(0,100):
    n = float(input("Ingrese un número: "))
    if n > 0:
        n_positivos +=1
    elif n < 0:
        n_negativos +=1
    if n % 2 == 0:
        n_pares +=1
    else:
        n_impares +=1
print("La cantidad de números pares son",n_pares)
print("La cantidad de números impares son", n_impares)
print("La cantidad de números positivos son", n_positivos)
print("La cantidad de números negativos son", n_negativos)


#Ejercicio 9
cantidad_n = 100
suma = 0
for i in range(0,cantidad_n):
    n = int(input("Ingrese un número entero: "))
    suma += n
media = suma / cantidad_n
print("La media de todos los valores ingresados es", media)


#Ejercicio 10
n = int(input("Ingrese un número: "))
a = n
invertido = 0

while n > 0:
    digito = n % 10         
    invertido = invertido * 10 + digito  
    n = n // 10 
print(f"El número original es {a} y el invertido es {invertido}.")