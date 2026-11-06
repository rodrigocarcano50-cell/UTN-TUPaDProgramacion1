from componente import Componente
from computadora import Computadora

class CotizadorComputadoras:
    @staticmethod
    def main():
        salirPrograma = ""
        while salirPrograma != "NO":
            print("====COTIZADOR DE COMPUTADORAS====")
            marca_valida = False
            while not marca_valida:
                marcaPC = input("Ingrese la marca de la computadora: ").strip()
                clean_marca = marcaPC.replace(',', '.')
                if marcaPC == "":
                    print("Error: La marca no puede estar vacía.")
                elif clean_marca.replace('.', '', 1).lstrip('-+').isdigit() and clean_marca.count('.') <= 1 and clean_marca != "":
                    print("Error: La marca no puede ser un número.")
                else:
                    marca_valida = True
            
            modelo_valido = False
            while not modelo_valido:
                modeloPC = input("Ingrese el modelo de la computadora: ").strip()
                if modeloPC == "":
                    print("Error: El modelo no puede estar vacío.")
                else:
                    modelo_valido = True
            
            computadora = Computadora(marcaPC, modeloPC)
            salirComponentes = ""
            while salirComponentes != "SI":
                print("\n  --- Carga de Componente ---")
                
                nombre_valido = False
                while not nombre_valido:
                    nombreComp = input("  Nombre del componente: ").strip()
                    clean_nombre = nombreComp.replace(',', '.')
                    if nombreComp == "":
                        print("  Error: El nombre no puede estar vacío.")
                    elif clean_nombre.replace('.', '', 1).lstrip('-+').isdigit() and clean_nombre.count('.') <= 1 and clean_nombre != "":
                        print("  Error: El nombre no puede ser un número.")
                    else:
                        nombre_valido = True
                
                marca_comp_valida = False
                while not marca_comp_valida:
                    marcaComp = input("  Marca del componente: ").strip()
                    clean_mcomp = marcaComp.replace(',', '.')
                    if marcaComp == "":
                        print("  Error: La marca no puede estar vacía.")
                    elif clean_mcomp.replace('.', '', 1).lstrip('-+').isdigit() and clean_mcomp.count('.') <= 1 and clean_mcomp != "":
                        print("  Error: La marca no puede ser un número.")
                    else:
                        marca_comp_valida = True
                
                cantidad_valida = False
                while not cantidad_valida:
                    cant_str = input("  Cantidad: ").strip()
                    if cant_str.isdigit() and int(cant_str) > 0:
                        cantidad = int(cant_str)
                        cantidad_valida = True
                    else:
                        print("  Error: Ingrese un número entero válido mayor a 0.")
                
                precio_valido = False
                while not precio_valido:
                    precio_str = input("  Precio por unidad: ").strip().replace(',', '.')
                    if precio_str.replace('.', '', 1).isdigit() and precio_str.count('.') <= 1 and precio_str != "":
                        precioUnitario = float(precio_str)
                        if precioUnitario >= 0:
                            precio_valido = True
                        else:
                            print("  Error: El precio no puede ser negativo.")
                    else:
                        print("  Error: Ingrese un valor numérico válido.")
                
                un_componente = Componente(nombreComp, marcaComp, cantidad, precioUnitario)
                computadora.componentes.append(un_componente)
                
                salirComponentes = input("  ¿Desea salir de la carga de componentes? (SI/NO): ").strip().upper()
                while salirComponentes not in ["SI", "NO"]:
                    print("  Por favor responda 'SI' o 'NO'.")
                    salirComponentes = input("  ¿Desea salir de la carga de componentes? (SI/NO): ").strip().upper()
            
            costoTotal, ganancia, precioVenta = computadora.calcularPrecioVenta()
            print("\n====Computadora====")
            print(f"Marca: {computadora.marca}")
            print(f"Modelo: {computadora.modelo}")
            print("Componentes:")
            print(f"{'Componente':<18} {'Marca':<12} {'Cantidad':<10} {'Precio X Unidad':<16} {'SubTotal'}")
            for comp in computadora.componentes:
                subtotal = comp.calcularSubtotal()
                print(f"{comp.nombre:<18} {comp.marca:<12} {comp.cantidad:<10} {comp.precioUnitario:<16} {subtotal}")
            print("-" * 55)
            print(f"{'Costo Total':<44} {costoTotal}")
            print("-" * 55)
            print(f"El precio sugerido de venta es {costoTotal} + {ganancia:.0f} = {precioVenta:.0f}")
            print("-------------------------------------------------------")
            
            salirPrograma = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()
            while salirPrograma not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirPrograma = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()

if __name__ == "__main__":
    CotizadorComputadoras.main()