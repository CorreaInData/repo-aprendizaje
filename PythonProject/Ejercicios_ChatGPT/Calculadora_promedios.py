''' Ejercicio: Calculadora de promedio
Escribe un programa en Python que solicite al usuario ingresar una lista de números separados por espacios
y calcule el promedio de esos números. El programa debe mostrar el resultado del promedio en pantalla.
'''

numeros = input('''Ingrese una lista de números a promediar, separados por espacios: 
-> ''')

lista = numeros.split(" ")
lista = lista.float()


print()