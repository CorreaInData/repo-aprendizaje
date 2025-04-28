'''
# Esto es una variable global (como el tesoro en el Palacio Real)
tesoro = "Oro"

def mi_casa():
    # Esto es una variable local (como el juguete en tu casa)
    juguete = "Pelota"
    print("En mi casa tengo:", juguete)
    print("Y también sé que en el Palacio Real hay:", tesoro)

# Llamamos a la función "mi_casa"
mi_casa()

# Intentamos usar la variable local "juguete" fuera de la función
#print("¿Puedo usar el juguete aquí?", juguete)  # ¡Error! El juguete no existe aquí.
'''


# Variable global (fuera de la función)
tesoro = "Oro"

def mi_casa(juguete):  # "juguete" es un parámetro (variable local)
    print("En mi casa tengo:", juguete)
    print("Y también sé que en el Palacio Real hay:", tesoro)

# Llamamos a la función y le pasamos un valor para el parámetro "juguete"
mi_casa("Pelota")

# Intentamos usar el parámetro "juguete" fuera de la función
#print("¿Puedo usar el juguete aquí?", juguete)  # ¡Error! El juguete no existe aquí.