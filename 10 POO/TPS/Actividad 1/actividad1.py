class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def obtenerValor(self, fila, columna):
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return c.valor
        return "La fila y la columna indicada no ha sido asignada en ninguna celda"

def pedir_valor():
    while True:
        val = input("Ingrese el valor (o escriba FIN para terminar): ").strip()
        if val.upper() == "FIN":
            return "FIN"
        elif val == "":
            print("Error, el valor no puede estar vacío.")
        elif val.isdigit():
            print("Error, el valor debe ser una cadena de texto (no puede ser un número entero).")
        else:
            return val

matriz = Matriz()

valor = pedir_valor()

while valor != "FIN":
    fila_valida = False
    while not fila_valida:
        fila_str = input("Ingrese la fila (número entero): ").strip()
        if fila_str.isdigit():
            fila = int(fila_str)
            fila_valida = True
        else:
            print("Error, la fila debe ser un número entero válido.")

    columna_valida = False
    while not columna_valida:
        columna_str = input("Ingrese la columna (número entero): ").strip()
        if columna_str.isdigit():
            columna = int(columna_str)
            columna_valida = True
        else:
            print("Error, la columna debe ser un número entero válido.")

    existe = False
    for c in matriz.celdasMatriz:
        if c.fila == fila and c.columna == columna:
            existe = True
            break

    if existe:
        print("Error, esa fila y columna ya fueron cargadas.")
    else:
        nueva = Celda(fila, columna, valor)
        matriz.celdasMatriz.append(nueva)
        print(f"Celda guardada con éxito. Valor ingresado: {valor}")
    
    print()
    valor = pedir_valor()

print("\n=== Valores cargados en la lista ===")
for c in matriz.celdasMatriz:
    print(f"Fila: {c.fila} | Columna: {c.columna} | Valor: {c.valor}")