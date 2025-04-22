diccionario = {
    'nombre' : 'Sebastian',
    'apellido' : 'Correa',
    'edad' : 26
}

print(diccionario)

# Devolver las claves del diccionario iterable (dict_keys)
claves = diccionario.keys()
print(claves)

# Devolver el valor correspondiente a una clave
obtener = diccionario.get("apellido")   # Si no lo encuentra devuelve none
print(obtener)

# Eliminar un elemento del diccionario
diccionario.pop('nombre')
print(diccionario)

# Obtener un elemento del diccionario
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

# Eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)
