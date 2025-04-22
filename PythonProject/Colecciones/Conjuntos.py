# Conjuntos

conjunto = set()    # Hay que poner esto PARA UN CONJUNTO VACÍO, porque sino Python creerá que se trata de un diccionario y no un conjunto

conjunto = {1,2,3,'hola',4.56}  # Puede tener t0do tipo de datos, menos otras colecciones y tampoco valores duplicados

print(conjunto,"\n")

conjunto.add(5)
conjunto.add('adios')
conjunto.add('a')
print(conjunto)
print(7 in conjunto)
print(4.56 in conjunto)
print(2 not in conjunto,"\n")

conjunto.discard(2)
conjunto.discard('hola')
print(conjunto)
conjunto.clear()
print(conjunto,"\n")

# Operaciones entre conjuntos

a = {1,2,3}
b = {3,4,5}
print(a == b)   # Igualdad entre los conjuntos

c = a | b   # Unión entre conjuntos
print(c)
c = a & b   # Intersección entre conjuntos
print(c)
c = a - b   # Diferencia entre conjuntos
print(c)
c = a ^ b   # Diferencia simétrica entre conjuntos (elementos que están en ambos conjuntos pero no en la intersección)
print(c,"\n")

c = {1,2,3,4,5}
print(a.issubset(c))    # Verifica si a es un subconjunto de c
print(b.issubset(c),"\n")
c.discard(4)
print(b.issubset(c))    # Verifica si c es un superconjunto de a
print(c.issuperset(a))
print(c.issuperset(b),"\n")
print(a.isdisjoint(b))  # verifica si los conjuntos tienen algo en común
a.discard(3)
a.add(7)
print(a.isdisjoint(b),"\n")

d = frozenset({'a','b','c','d'})
print(d)

