''' Ejercicio 4
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones
aritméticas básicas (suma, resta, multiplicación y división). El usuario debe especificar la operación con el primer
caracter del nombre de la operación.
'''

num1 = float(input("Por favor ingrese un número que desee operar: "))
num2 = float(input("Por favor ingrese un número que desee operar: "))
ope = input("Por favor ingrese la inicial de la operación que desee realizar: ").upper()

if  ope == 'S':
    res = num1 + num2
    print(f"El resultado de la suma es: {res}")
elif ope == 'R':
    res = num1 - num2
    print(f"El resultado de la resta es: {res}")
elif ope == 'M' or ope == 'P':
    res = num1 * num2
    print(f"El resultado de la multiplicación es: {res}")
elif ope == 'D':
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        res = num1 / num2
        print(f"El resultado de la división es: {res}")
else:
    print("La letra ingresada no corresponde a la inicial de alguna de las operaciones aritméticas básicas")
