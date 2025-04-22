# Tuplas

tupla = (4,'hola',6.78,[1,2,3],4)
print("4-",tupla)

'''
Las tuplas son listas que no permiten su modificación, pero si permiten la busqueda de sus elementos
'''

print("\n10-",tupla[1])
print("11-",tupla[0])
print("12-",tupla[-1])
print("13-",tupla[2:4])
print("14-",6.78 in tupla)
print("15-",tupla.index("hola"))
print("16-",tupla.count(4))
print("17-",len(tupla),"\n")

lista = list(tupla) # Genera una copia de la tupla que convierte en lista y la guarda en una nueva variable
print(lista)
tuple = tuple(lista)    # Genera una copia de una lista que convierte en tupla y la guarda en una nueva variable
print(tuple)
