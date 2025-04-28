''' Escribe un programa en Python que:
1. Pida al usuario su año de nacimiento.
2. Calcule su edad (suponiendo que el año actual es 2025).
3. Muestre la edad en pantalla.
'''
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

edad = 2025 - año_nacimiento

print(f"Tienes {edad} años")
