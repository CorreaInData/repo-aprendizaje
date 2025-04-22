# Ejercicio 1
'''
Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos y por último me muestre
la lista
'''

lista = [1,2,3,'Sebastian',1,2,2,3,1,2,'Sebastian']
print(f"la lista inicial es: {lista}")
# lista = list(set(lista))
# print(f"La lista depurada es: {lista}")
print(f"La lista depurada es: {list(set(lista))}")

'''
lista = [1,2,3,'Sebastian',1,2,2,3,1,2,'Sebastian']
print(f"la lista inicial es: {lista}")

conjunto = set(lista)
lista = list(conjunto)

print(f"La lista depurada es: {lista}")
'''

