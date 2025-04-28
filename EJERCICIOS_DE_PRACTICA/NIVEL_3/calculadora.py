def leer_numero(mensaje):
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n📌 Menú de Operaciones:")
    print("1️⃣ Sumar")
    print("2️⃣ Restar")
    print("3️⃣ Multiplicar")
    print("4️⃣ Dividir")
    print("5️⃣ Salir")

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-5): ")

    if opcion == "5":
        print("👋 Hasta luego.")
        break  # Sale del programa

    if opcion in ["1", "2", "3", "4"]:
        num1 = leer_numero("Ingrese el primer número: ")
        num2 = leer_numero("Ingrese el segundo número: ")

        if opcion == "1":
            resultado = num1 + num2
            print(f"✅ Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"✅ Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"✅ Resultado: {num1} × {num2} = {resultado}")
        elif opcion == "4":
            if num2 == 0:
                print("❌ Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"✅ Resultado: {num1} ÷ {num2} = {round(resultado, 2)}")
    else:
        print("⚠️ Opción inválida, seleccione una opción entre 1 y 5.")

