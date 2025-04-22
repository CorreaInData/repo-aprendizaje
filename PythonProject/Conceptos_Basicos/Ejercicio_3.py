# Ejercicio 3

a = input("Ingrese un valor para a: ")
b = input("Ingrese un valor para b: ")
c = input("Ingrese un valor para c: ")
print("")

''' La forma tradicional de hacerlo
c = a
a = b
b = c
'''

a,b,c = b,c,a   # La forma en que Python puede hacerlo de forma más sencilla y rápida

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
print(f"El nuevo valor de c es: {c}")