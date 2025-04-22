
animales = ["gato","perro","cocodrilo","tortuga"]
numeros = [15,35,16,21]

# Recorriendo la lista animales
for animal in animales:
    type(animal)
    # print(animal)

# Recorriendo la lista numeros y multiplicando por 10
for numero in numeros:
    resultado = numero * 10
    # print(resultado)

# Iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    type(numero)
    # print(f"recorriendo lista 1: {numero}")
    # print(f"recorriendo lista 2: {animal}")

#
for num in range(5,15):
    type(num)
    # print(num)

# Forma no optima de recorrer una lista
for num in range(len(numeros)):
    type(num)
    # print(numeros[num])

# Forma correcta de recorrer una lista con su indice

for num in enumerate(numeros):
    print(num)
    indice = num[0]
    valor = num[1]
    print(f"El indice es {indice} y el valor es {valor}")

# Usando el for/else
for num in numeros:
    print(f"Ejecutando el último bucle, valor actual: {num}")
else:
    print("El bucle terminó")

# T0do lo anterior sirve para iterar tuplas y listas