from Notas import Nota
from alumnos import Alumno

class CargaNotas:
    @staticmethod
    def main(): 
        alumnos = []
        salirAlumno = ""
        
        while salirAlumno != "SI":
            print("\n=== Ingrese datos del alumno ===")
            
            nombre_valido = False
            while not nombre_valido:
                nombreCompleto = input("Ingrese el nombre completo: ").strip()
                if nombreCompleto == "":
                    print("Error, no puede quedar vacío.")
                elif any(caracter.isdigit() for caracter in nombreCompleto):
                    print("Error, el nombre no puede contener números.")
                else:
                    nombre_valido = True
            
            legajo_valido = False
            while not legajo_valido:
                legajo1 = input("Ingrese el legajo del alumno: ").strip()
                if legajo1.isdigit():
                    legajo = int(legajo1)
                    legajo_valido = True
                else:
                    print("Error, el legajo debe ser un número entero válido.")
            
            alumno = Alumno(nombreCompleto, legajo)
            salirNotas = ""
            
            while salirNotas != "SI":
                print("\n--- Carga de Notas ---")
                
                catedra_valida = False
                while not catedra_valida:
                    nombreCatedra = input("Ingrese el nombre de cátedra: ").strip()
                    if nombreCatedra == "":
                        print("Error, la cátedra no puede estar vacía.")
                    elif nombreCatedra.isdigit():
                        print("Error, la cátedra no puede ser un número entero.")
                    else:
                        catedra_valida = True
                
                nota_valida = False
                while not nota_valida:
                    nota1 = input("Nota (ej: 8.5 o 9): ").strip().replace(',', '.')
                    if nota1.replace('.', '', 1).isdigit() and nota1.count('.') <= 1 and nota1 != "":
                        notaExamen = float(nota1)
                        nota_valida = True
                    else:
                        print("Error: Ingrese un valor numérico válido para la nota.")
                
                nota = Nota(nombreCatedra, notaExamen)
                alumno.notas.append(nota)
                
                salirNotas = input("¿Desea salir de la carga de notas? (SI/NO): ").strip().upper()
                while salirNotas not in ["SI", "NO"]:
                    print("Por favor responda 'SI' o 'NO'.")
                    salirNotas = input("¿Desea salir de la carga de notas? (SI/NO): ").strip().upper()
            
            alumnos.append(alumno)
            
            salirAlumno = input("¿Desea salir de la carga de alumnos? (SI/NO): ").strip().upper()
            while salirAlumno not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirAlumno = input("¿Desea salir de la carga de alumnos? (SI/NO): ").strip().upper()
        
        print("\n" + "="*10 + " INFORMACIÓN CARGADA DE ALUMNOS " + "="*10)
        for alumno in alumnos:
            print(f"\nDatos Alumno: {alumno.nombreCompleto} (Legajo: {alumno.legajo})")
            for nota in alumno.notas:
                print(f"  * Cátedra: {nota.catedra} | Nota: {nota.notaExamen}")
            promedio = alumno.calcularPromedio()
            print(f"  -> El promedio del alumno es: {promedio:.2f}")

if __name__ == "__main__":
    CargaNotas.main()