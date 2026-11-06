from ingredientes import Ingrediente
from plato import Plato

class MenuRestaurant:
    @staticmethod
    def main():
        platosMenu = []
        salirPlato = ""
        while salirPlato != "SI":
            print("===CARGA DE PLATOS===")
            nombre_valido = False
            while not nombre_valido:
                nombrePlato = input("Ingrese el nombre completo del plato: ").strip()
                if nombrePlato == "":
                    print("Error: El nombre del plato no puede estar vacío.")
                elif nombrePlato.isdigit():
                    print("Error: El nombre del plato no puede ser un número entero.")
                else:
                    nombre_valido = True
            precio_valido = False
            while not precio_valido:
                precio_str = input("Ingrese el precio: ").strip().replace(',', '.')
                if precio_str.replace('.', '', 1).isdigit() and precio_str.count('.') <= 1 and precio_str != "":
                    precio = float(precio_str)
                    precio_valido = True
                else:
                    print("Error: Ingrese un valor numérico válido para el precio.")
            bebida_str = input("¿Es una bebida? (SI/NO): ").strip().upper()
            while bebida_str not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                bebida_str = input("¿Es una bebida? (SI/NO): ").strip().upper()
            bebida = (bebida_str == "SI")
            un_plato = Plato(nombrePlato, precio, bebida)
            if not un_plato.esBebida:
                salirIngredientes = ""
                while salirIngredientes != "SI":
                    print("\n  --- Carga de Ingrediente ---")
                    ingrediente_valido = False
                    while not ingrediente_valido:
                        nombreIngrediente = input("  Nombre del ingrediente: ").strip()
                        if nombreIngrediente == "":
                            print("  Error: El nombre del ingrediente no puede estar vacío.")
                        elif nombreIngrediente.isdigit():
                            print("  Error: El nombre del ingrediente no puede ser un número entero.")
                        else:
                            ingrediente_valido = True
                    cantidad_valida = False
                    while not cantidad_valida:
                        cant_str = input("  Cantidad: ").strip().replace(',', '.')
                        if cant_str.replace('.', '', 1).isdigit() and cant_str.count('.') <= 1 and cant_str != "":
                            cantidad = float(cant_str)
                            cantidad_valida = True
                        else:
                            print("  Error: Ingrese un valor numérico válido para la cantidad.")
                    unidad_valida = False
                    while not unidad_valida:
                        unidadMedida = input("  Unidad de medida (ej. gramos, unidad): ").strip()
                        if unidadMedida == "":
                            print("  Error: La unidad de medida no puede estar vacía.")
                        elif unidadMedida.isdigit():
                            print("  Error: La unidad de medida no puede ser un número entero.")
                        else:
                            unidad_valida = True
                    un_ingrediente = Ingrediente(nombreIngrediente, cantidad, unidadMedida)
                    un_plato.ingredientes.append(un_ingrediente)
                    salirIngredientes = input("  ¿Desea salir de la carga de ingredientes? (SI/NO): ").strip().upper()
                    while salirIngredientes not in ["SI", "NO"]:
                        print("  Por favor responda 'SI' o 'NO'.")
                        salirIngredientes = input("  ¿Desea salir de la carga de ingredientes? (SI/NO): ").strip().upper()
            platosMenu.append(un_plato)
            salirPlato = input("\n¿Desea salir de la carga de platos? (SI/NO): ").strip().upper()
            while salirPlato not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirPlato = input("\n¿Desea salir de la carga de platos? (SI/NO): ").strip().upper()
        print("\n" + "-----------MENÚ----------------")
        for plato in platosMenu:
            print(f"{plato.nombreCompleto}")
            print(f"Precio: $ {plato.precio}")
            if not plato.esBebida and len(plato.ingredientes) > 0:
                print("Ingredientes:")
                print(f"Nombre\t\tCantidad\tUnidad de Medida")
                for ing in plato.ingredientes:
                    print(f"{ing.nombre}\t\t{ing.cantidad}\t\t{ing.unidadMedida}")
            print("-" * 34)
if __name__ == "__main__":
    MenuRestaurant.main()