from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

class GestionBarrio:
    @staticmethod
    def main():
        print("====SISTEMA DE GESTIÓN DE BARRIOS====")
        
        barrio_valido = False
        while not barrio_valido:
            nombreBarrio = input("Ingrese el nombre del barrio: ").strip()
            clean_b = nombreBarrio.replace(',', '.')
            if nombreBarrio == "":
                print("Error: El nombre no puede estar vacío.")
            elif clean_b.replace('.', '', 1).lstrip('-+').isdigit() and clean_b.count('.') <= 1 and clean_b != "":
                print("Error: El nombre no puede ser un número.")
            else:
                barrio_valido = True

        empresa_valida = False
        while not empresa_valida:
            empresa = input("Ingrese la empresa constructora: ").strip()
            clean_e = empresa.replace(',', '.')
            if empresa == "":
                print("Error: La empresa no puede estar vacía.")
            elif clean_e.replace('.', '', 1).lstrip('-+').isdigit() and clean_e.count('.') <= 1 and clean_e != "":
                print("Error: La empresa no puede ser un número.")
            else:
                empresa_valida = True

        mi_barrio = Barrio(nombreBarrio, empresa)
        salirViviendas = ""
        while salirViviendas != "SI":
            print("\n--- Carga de Vivienda ---")
            
            calle_valida = False
            while not calle_valida:
                calle = input("Calle: ").strip()
                clean_c = calle.replace(',', '.')
                if calle == "":
                    print("Error: La calle no puede estar vacía.")
                elif clean_c.replace('.', '', 1).lstrip('-+').isdigit() and clean_c.count('.') <= 1 and clean_c != "":
                    print("Error: La calle no puede ser un número.")
                else:
                    calle_valida = True

            num_valido = False
            while not num_valido:
                num_str = input("Número: ").strip()
                if num_str.isdigit() and int(num_str) >= 0:
                    numero = int(num_str)
                    num_valido = True
                else:
                    print("Error: Ingrese un número entero válido (mayor o igual a 0).")

            manzana_valida = False
            while not manzana_valida:
                manzana = input("Manzana: ").strip()
                clean_m = manzana.replace(',', '.')
                if manzana == "":
                    print("Error: La manzana no puede estar vacía.")
                elif clean_m.replace('.', '', 1).lstrip('-+').isdigit() and clean_m.count('.') <= 1 and clean_m != "":
                    print("Error: La manzana no puede ser un número entero puro.")
                else:
                    manzana_valida = True

            nroCasa_valido = False
            while not nroCasa_valido:
                nroCasa_str = input("Nro de Casa: ").strip()
                if nroCasa_str.isdigit() and int(nroCasa_str) > 0:
                    nroCasa = int(nroCasa_str)
                    nroCasa_valido = True
                else:
                    print("Error: Ingrese un número de casa válido mayor a 0.")

            sup_valida = False
            while not sup_valida:
                sup_str = input("Superficie del Terreno (m2): ").strip().replace(',', '.')
                if sup_str.replace('.', '', 1).isdigit() and sup_str.count('.') <= 1 and sup_str != "":
                    superficieTerreno = float(sup_str)
                    if superficieTerreno > 0:
                        sup_valida = True
                    else:
                        print("Error: La superficie debe ser mayor a 0.")
                else:
                    print("Error: Ingrese un valor numérico válido.")

            una_vivienda = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno)
            salirHabitaciones = ""
            while salirHabitaciones != "SI":
                print("\n    -- Carga de Habitación --")
                
                nombreHab_valido = False
                while not nombreHab_valido:
                    nombreHab = input("    Nombre de la habitación: ").strip()
                    clean_nh = nombreHab.replace(',', '.')
                    if nombreHab == "":
                        print("    Error: El nombre no puede estar vacío.")
                    elif clean_nh.replace('.', '', 1).lstrip('-+').isdigit() and clean_nh.count('.') <= 1 and clean_nh != "":
                        print("    Error: El nombre no puede ser un número.")
                    else:
                        nombreHab_valido = True

                mt_valido = False
                while not mt_valido:
                    mt_str = input("    Metros cuadrados: ").strip().replace(',', '.')
                    if mt_str.replace('.', '', 1).isdigit() and mt_str.count('.') <= 1 and mt_str != "":
                        metrosCuadrados = float(mt_str)
                        if metrosCuadrados > 0:
                            mt_valido = True
                        else:
                            print("    Error: Los metros deben ser mayores a 0.")
                    else:
                        print("    Error: Ingrese un valor numérico válido.")

                una_habitacion = Habitacion(nombreHab, metrosCuadrados)
                una_vivienda.habitaciones.append(una_habitacion)
                
                salirHabitaciones = input("    ¿Desea salir de la carga de habitaciones? (SI/NO): ").strip().upper()
                while salirHabitaciones not in ["SI", "NO"]:
                    print("    Por favor responda 'SI' o 'NO'.")
                    salirHabitaciones = input("    ¿Desea salir de la carga de habitaciones? (SI/NO): ").strip().upper()

            mi_barrio.viviendas.append(una_vivienda)
            salirViviendas = input("\n¿Desea salir de la carga de viviendas? (SI/NO): ").strip().upper()
            while salirViviendas not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirViviendas = input("\n¿Desea salir de la carga de viviendas? (SI/NO): ").strip().upper()

        print(f"\n====INFORME DEL BARRIO: {mi_barrio.nombre}====")
        print(f"====Empresa: {mi_barrio.empresaConstructora}====")
        totalTerreno = mi_barrio.getSuperficieTotalTerreno()
        print(f"a) Superficie Total de Terreno del Barrio: {totalTerreno:.2f} m2")

        consultaManzana_valida = False
        while not consultaManzana_valida:
            consultaManzana = input("\nIngrese una Manzana para consultar su superficie de terreno: ").strip()
            if consultaManzana == "":
                print("Error: La manzana a consultar no puede estar vacía.")
            else:
                consultaManzana_valida = True

        totalTerrenoMza = mi_barrio.getSuperficieTotalTerrenoXManzana(consultaManzana)
        print(f"b) Superficie Total de Terreno en Manzana '{consultaManzana}': {totalTerrenoMza:.2f} m2")
        print("\nc) Detalle de Metros Cuadrados Cubiertos por Vivienda:")
        for v in mi_barrio.viviendas:
            cubiertos = v.getMetrosCuadradosCubiertos()
            print(f"   - Casa Nro {v.nroCasa} (Calle {v.calle} {v.numero}, Mza {v.manzana}): {cubiertos:.2f} m2 cubiertos")
        
        totalCubiertaBarrio = mi_barrio.getSuperficieTotalCubierta()
        print(f"\nd) Superficie Total Cubierta del Barrio: {totalCubiertaBarrio:.2f} m2")

if __name__ == "__main__":
    GestionBarrio.main()