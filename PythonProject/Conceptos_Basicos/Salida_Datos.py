# Salida de datos por consola

nombre = 'Sebastian'
edad = 26

print("Hola",nombre,"tienes",edad,"años.")  # Primera forma para mostrar datos en consola
print("Hola {} tienes {} años.".format(nombre,edad))    # Segunda forma para mostrar datos en consola
print(f"Hola {nombre} tienes {edad} años.") # Tercera forma para mostrar datos en consola
print("")

# Entrada de datos

nombre = input("Digite su nombre: ") # La entrada de datos siempre la va a realizar en tipo texto
print(f"Hola {nombre}")
numero = int(input("Digite un número: "))   # Para guardar número enteros es 'int', si es un racional es con 'float'
print(f"El número es: {numero}")

# Funciones Integradas

e = int("13")   # Para la conversión de texto a entero
print(e)
r = float("13.2")   # Para la conversión de texto a racionales
print(r)
t = str(15.3) # Para la conversión de números (enteros o racionales) a texto
print(t)
b = bin(15) # Para la conversión de base decimal a binaria
print(b)
h = hex(15) # Para la conversión de base decimal a hexagésimal
print(h)
e = int("0b1111",2) # Para la conversión de base binaria a decimal (el 0b en la cadena no es necesario ponerlo, pero la lectura es mejor ponerlo )
print(e)
e = int("0xf",16)   # Para la conversión de base hexagésimal a decimal
print(e)
a = abs(-14)    # Para escribir el valor absoluto de un número
print(a)
r = round(5.36) # Para redondear un número racional hacia su entero más cercano
print(r)
c = len("Sebastian Correa")    # Para contar el número de caracteres que tiene una cadena de texto
print(c)