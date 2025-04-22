# Calculadora que opera dos números 

while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    operacion = input("Ingrese la operación a realizar (+, -, *, /) o 'salir' para terminar: ")

    if operacion == "+":
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == "-":
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == "*":  
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == "/":
        if num2 != 0:
            resultado = round(num1 / num2, 2)
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir por cero")
    elif operacion.lower() == "salir":
        print("¡Calculadora cerrada!")
        break
    else:
        print("Operación no válida, intenta de nuevo.")
# End