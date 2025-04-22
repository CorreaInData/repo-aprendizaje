''' Ejercicio 1
Hacer un programa que pida dos números y se dé cuenta de cuál de ellos es par o si ambos lo son
'''

a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))

if a%1!=0 or b%1!=0:
    print("Por favor ingrese números enteros")
else:
    if a % 2 == 0 and b % 2 == 0:
        print("Ambos valores ingresados son pares")
    elif a % 2 == 0 and b % 2 != 0:
        print("El primer número es par")
    elif a % 2 != 0 and b % 2 == 0:
        print("El segundo número es par")
    else:
        print("Ningún valor ingresado es par")

''' Mismo programa, pero con condicionales anidados
if a%1!=0 or b%1!=0:
    print("Por favor ingrese números enteros")
else:
    if a % 2 != 0 or b % 2 != 0:
        if a % 2 == 0:
            print("El primer número es par")
        elif b % 2 == 0:
            print("El segundo número es par")
        elif a % 2 != 0 and b % 2 != 0:
            print("Ambos valores ingresados son impares")
    else:
        print("Ambos valores ingresados son pares")
'''
