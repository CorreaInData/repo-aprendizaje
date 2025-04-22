# Ejercicio 2
'''
Hacer un programa que pida 3 números y determine cual es el mayor
'''

num1 = float(input("Ingrese el primer número "))
num2 = float(input("Ingrese el segundo número "))
num3 = float(input("Ingrese el tercer número "))

if num1>=num2 and num1>=num3:
    print(f"{num1} es el número más grande")
elif num2>=num1 and num2>=num3:
    print(f"{num2} es el número más grande")
elif num3>=num1 and num3>=num2:
    print(f"{num3} es el número más grande")

''' Mismo programa pero complicandome más
if num1!=num2 or num2!=num3:
    if num1>=num2:
        if num1>num3:
            print(f"{num1} es el número más grande")
        else:
            print(f"{num3} es el número más grande")
    else:
        if num2>num3:
            print(f"{num2} es el número más grande")
        else:
            print(f"{num3} es el número más grande")
else:
    print("Todos los números son iguales")
'''
