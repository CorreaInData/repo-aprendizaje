def es_valido(tablero, fila, columna, num):
    """
    Verifica si es válido colocar 'num' en tablero[fila][columna].
    """
    # Verificar la fila
    if num in tablero[fila]:
        return False
    
    # Verificar la columna
    for i in range(9):
        if tablero[i][columna] == num:
            return False

    # Verificar la subcuadrícula 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_columna + j] == num:
                return False

    return True

def encontrar_casilla_vacia(tablero):
    """
    Encuentra la próxima casilla vacía (que contiene un 0) en el Sudoku.
    Devuelve una tupla (fila, columna) o None si no hay casillas vacías.
    """
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j  # Devuelve la primera casilla vacía encontrada
    return None

def resolver_sudoku(tablero):
    """
    Resuelve el Sudoku utilizando backtracking.
    """
    casilla = encontrar_casilla_vacia(tablero)
    
    # Si no hay casilla vacía, el Sudoku está resuelto
    if not casilla:
        return True
    
    fila, columna = casilla

    for num in range(1, 10):  # Intentar números del 1 al 9
        if es_valido(tablero, fila, columna, num):
            tablero[fila][columna] = num  # Colocar número en la casilla
            
            if resolver_sudoku(tablero):  # Llamado recursivo
                return True
            
            tablero[fila][columna] = 0  # Backtrack: Deshacer movimiento

    return False  # No se encontró una solución válida

def imprimir_sudoku(tablero):
    """
    Imprime el Sudoku de manera legible con separadores.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Separador de bloques 3x3
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separador vertical entre bloques 3x3
            
            print(tablero[i][j], end=" ")
        
        print()  # Salto de línea

# Ejemplo de Sudoku a resolver
sudoku = [
    [0, 0, 6, 0, 0, 2, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 5, 2],
    [0, 9, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 4, 0, 0, 0, 0, 0, 6],
    [3, 0, 0, 0, 0, 9, 1, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 0, 1, 4, 3, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 8, 6, 0]
]

print("Sudoku inicial:")
imprimir_sudoku(sudoku)

if resolver_sudoku(sudoku):
    print("\nSudoku resuelto:")
    imprimir_sudoku(sudoku)
else:
    print("No tiene solución.")
