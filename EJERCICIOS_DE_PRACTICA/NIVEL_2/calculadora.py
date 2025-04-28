def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

num1 = leer_numero("Ingrese el primer número: ")
num2 = leer_numero("Ingrese el segundo número: ")

suma = num1 + num2

print(f"La suma de {num1} y {num2} es: {suma}")
