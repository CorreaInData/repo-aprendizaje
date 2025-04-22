# Ejercicio 4
import math

radio = float(input("Ingrese el valor del radio del circulo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El valor del área del circulo es: {area:.2f}") # Lo que va después de la variable, indica que saldrán solo dos decimales
print(f"El valor del perimetro del circulo es: {perimetro:2f}")