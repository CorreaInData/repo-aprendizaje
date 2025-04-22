# Ejercicio 3
'''
Hacer un programa que pida un caracter e indique si es una vocal o no
'''

caracter = input("Ingrese un solo caracter: ").lower() # .lower es un método que me sirve para convertir los valores ingresados a minusculas
# .lower() no modificará la variable original, por lo que tendría que asignarla a una nueva variable o aplicarla directamente a la variable original si eso es lo que yo quisiera

if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="U":
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado no es una vocal")

# Hay otra forma de hacerlo más rápida que consiste en usar la declaración in en el condicional
''' 
caracter = input("Ingrese un solo caracter: ")

if caracter.lower() in ['a','e','i','o','u']:   # La declaración in se utiliza para verificar si un elemento está presente en una lista determinada
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado no es una vocal")  
'''