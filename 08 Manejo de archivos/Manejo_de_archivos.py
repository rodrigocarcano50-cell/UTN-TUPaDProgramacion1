#Ejercicio 1
productos = [
    "Manzana,1800,10\n",
    "Banana,1300,15\n",
    "Naranja,1500,20\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

#Ejercicio 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")


#Ejercicio 3
nuevoProductoNombre = input("Ingrese el nombre del nuevo producto: ")
nuevoProductoPrecio = int(input("Ingrese el precio del nuevo producto: "))
nuevoProductoCantidad = int(input("Ingrese la cantidad del nuevo producto: "))

with open("productos.txt","a") as archivo:
    archivo.write(f"{nuevoProductoNombre},{nuevoProductoPrecio},{nuevoProductoCantidad}\n")
print("¡Producto agregado con éxito!")


#Ejercicio 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        
        if len(partes) == 3:
            producto_dict = {
                "nombre": partes[0],
                "precio": float(partes[1]),    
                "cantidad": int(partes[2])     
            }         
            productos.append(producto_dict)

print(productos)


#Ejercicio 5 
nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
encontrado = False
for prod in productos:
    if prod["nombre"].lower() == nombre_buscado.lower():
        print("\n¡Producto encontrado!")
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break  
if not encontrado:
    print("\nError: El producto no existe en el registro.")


#Ejercicio 6
with open("productos.txt", "w") as archivo:
    for prod in productos:
        linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n"
        archivo.write(linea)
print("¡El archivo productos.txt ha sido actualizado y guardado correctamente!")
print(productos)