#Ejercicio 1 
precios_frutas = {"Banana" : 1200, "Anana" : 2500 , "Melon" : 3000 , "Uva" : 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


#Ejercicio 2
precios_frutas = {"Banana" : 1200, "Anana" : 2500 , "Melon" : 3000 , "Uva" : 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1700
precios_frutas["Pera"] = 2300
precios_frutas["Banana"] = 1330
precios_frutas["Melon"] = 2800

print(precios_frutas)


#Ejercicio 3
precios_frutas = {"Banana" : 1200, "Anana" : 2500 , "Melon" : 3000 , "Uva" : 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1700
precios_frutas["Pera"] = 2300
precios_frutas["Banana"] = 1330
precios_frutas["Melon"] = 2800

print(precios_frutas.keys())


#Ejercicio 4
contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    numero= int(input(f"Ingrese el numero de {nombre}: "))
    contactos[nombre] = numero

buscar = input("Ingrese un nombre: ")
if buscar in contactos:
    print(f"El numero de telefono de {buscar} es {contactos[buscar]}.")
else:
    print("No se encuentra nadie con ese nombre. ")


#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras unicas", palabras_unicas)
print("Recuento", recuento)


#Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    print(f"Ingrese las 3 notas de {nombre}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    alumnos[nombre] = nota1 + nota2 + nota3

for nombre, notas in alumnos.items():
    promedio = notas / 3
    print(f"El promedio de {nombre} es: {promedio}")


#Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {6, 7, 8, 9, 4}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


#Ejercicio 8
stock = {"Arroz" : 20, "Fideos" : 35, "Leche" : 12, "Azucar" : 8}

producto = input("Ingrese el nombre de un producto: ")

if producto in stock:
    print(f"El stock de {producto} es {stock[producto]}.")
    unidades = int(input(f"Ingrese las unidades a agregar a {producto}: "))
    stock[producto] += unidades
else:
    print(f"{producto} no existe en el stock.")
    unidades = int(input(f"Ingrese el stock inicial de {producto}: "))
    stock[producto] = unidades

print(f"El nuevo stock de {producto} es {stock[producto]}.")
print(stock)


#Ejercicio 9
agenda = {("Lunes", "10:00") : "Clase de Programacion",
          ("Lunes", "18:00") : "Gimnasio",
          ("Miercoles", "14:00") : "Reunion de grupo",
          ("Viernes", "09:00") : "Parcial de Matematica"}

dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora (HH:MM): ")

if (dia, hora) in agenda:
    print(f"El {dia} a las {hora} tenes: {agenda[(dia, hora)]}.")
else:
    print(f"No hay ninguna actividad el {dia} a las {hora}.")


#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Original:", original)
print("Invertido:", invertido)