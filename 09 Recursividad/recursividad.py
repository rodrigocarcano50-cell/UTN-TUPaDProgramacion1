#Ejercicio 1
def numero_factorial (n):
    if n == 0:
        return 1
    else:
        return n * numero_factorial(n-1)

numero = int(input("Ingrese un numero: "))
for i in range(1, numero + 1):
    resultado= numero_factorial(i)
    print(f"El factorial de {i} es: {resultado}")


#Ejercicio 2
def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

posicion_usuario = int(input("Ingresá la posición hasta donde querés ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci desde la posición 0 hasta la {posicion_usuario}:")

for i in range(posicion_usuario + 1):
    resultado = fibonacci_recursivo(i)
    print(f"Posición {i}: {resultado}")


#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")


#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número entero positivo: "))
if numero == 0:
    print("El número en binario es: 0")
else:
    print(f"El número en binario es: {decimal_a_binario(numero)}")


#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[len(palabra) - 1]:
        return False
    else:
        return es_palindromo(palabra[1:len(palabra) - 1])

palabra = input("Ingresá una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")


#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingresá un número entero positivo: "))
print(f"La suma de los dígitos es: {suma_digitos(numero)}")


#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingresá la cantidad de bloques del nivel más bajo: "))
print(f"El total de bloques necesarios es: {contar_bloques(bloques)}")


#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá un dígito entre 0 y 9: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces")
