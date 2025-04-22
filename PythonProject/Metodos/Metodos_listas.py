lista = list(["Computador","Python","Programación",43,12,36])   # Se puede hacer una lista desde el método list (aunque no es lo más óptimo)

print(lista)

lista = ["Hola","Pepe",51,32,45,16,False]

# Devolver la cantidad de elementos en una lista
cantidad_elementos = len(lista)

# Agregar elementos a la lista
lista.append("Wild Rift")

# Agregar elemento a la lista, en un índice específico
lista.insert(2,"Grillo")

# agregar una lista a una lista
lista.extend([2,45,"Monteria"])

# Eliminar un elemento de la lista (por el índice específico)
lista.pop(6)    # Si se deja vacío o se pone -1, se elimina el último elemento, -2 el penúltimo y así sucesivamente

# Remover un elemento de la lista, por su valor
lista.remove("Wild Rift")   # Si no encuentra el elemento, generará una excepción

print(lista)

# Eliminar todos los elementos de la lista
lista.clear()

lista = [8,9,2,5,4,3,8,1,9,2,9,2,17,2,26,184,37,5,False,True,False]

# Ordernar la lista de forma ascendente (Si se pone el parametro reverse=True, la lista se ordenará de forma descendente)
lista.sort()

# Invertir los elementos de una lista (no importa si esta ordenada o no)
lista.reverse()

print(lista)

print(dir(lista))   # El método dir, permite validar las "operaciones" que podemos realizar con un tipo de variable en especifio
