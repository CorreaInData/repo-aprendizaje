# Condicionales

numero = int(input("Digite un número: "))

if numero>0:
    print("El número es positivo")
elif numero==0: # Condicional Si entonces, para un valor especial
    print("El numero es cero")
else:
    print("El número es negativo")

# Condicionales combinados

edad = int(input("Por favor digite su edad: "))

if 0<edad<100:  # Es lo mismo que: edad>0 and edad<100
    if edad>=18:    # Condicional anidado
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Edad incorrecta")
