#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()


#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
nombre_ingresado = input("Ingrese su nombre: ")
saludar_usuario(nombre_ingresado)


#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4
def calcular_area_circulo(radio):
    area = (radio ** 2) * 3.1416
    print("El area del circulo es: ",area)
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    print("El perimetro del circulo es: ",perimetro)

radio = float(input("Ingrese el radio: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


#Ejercicio 5
def segundos_a_horas(segundos):
    resultado = segundos / 3600
    print("Los segundos ingresados convertido en hora son: ", resultado)

segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)


#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)


#Ejercicio 7
def operaciones_basicas(a, b):
    tupla = ( a + b, a - b, a * b, a / b)
    print(f"La suma es {tupla[0]}, la resta es {tupla[1]}, la multiplicacion es {tupla[2]} y la division es {tupla[3]}.")

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

operaciones_basicas(a,b)


#Ejercicio 8
def calcular_imc(peso):
    imc = peso / (altura ** 2)
    print("El IMC es: ", imc)
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso)


#Ejercicio 9
def celsius_a_fahrenheit(celcius):
    total = (celcius * 1.8) + 32
    print("La temperatura en Fahrenheit es: ", total)
celcius = float(input("Ingrese una temperatura en Celcius (C°): "))

celsius_a_fahrenheit(celcius)


#Ejercicio 10 
def calcular_promedio(a, b, c):
    total = (a + b + c) / 3
    print("El promedio es: ", total)
    
a = float(input("Ingrese la nota A: "))
b = float(input("Ingrese la nota B: "))
c = float(input("Ingrese la nota C: "))

calcular_promedio(a, b, c)