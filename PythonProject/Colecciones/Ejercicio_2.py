# Ejercicio 2
'''
Escriba un programa que tenga 2 listas y que, a continuación, cree las siguientes listas (en las que no deben haber
repeticiones):
- Listas de palabras que aparecen en las dos listas
- Listas de palabras que aparecen en la primera lista, pero no en la segunda
- Listas de palabras que aparecen en la segunda lista, pero no en la primera
- Listas de palabras que aparecen en ambas listas
'''

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

a = conjunto1 | conjunto2
b = conjunto1 - conjunto2
c = conjunto2 - conjunto1
d = conjunto1 & conjunto2

print(f"Los elementos que están en las dos listas son: {list(a)}")
print(f"Los elementos que están en la primera lista, pero no están en la segunda son: {list(b)}")
print(f"Los elementos que están en la segunda lista, pero no están en la primera son: {list(c)}")
print(f"Los elementos que están en ambas listas: {list(d)}")
