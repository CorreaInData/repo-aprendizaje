''' Escribe un programa en Python que:
1. Pida al usuario su año de nacimiento.
2. Calcule su edad (suponiendo que el año actual es 2025).
3. Muestre la edad en pantalla.
4. Agregar validaciones
'''

while True:
    try:
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
        if 1900 < año_nacimiento <= 2025:
            edad = 2025 - año_nacimiento
            print(f"Tienes {edad} años")
            break
        else:
            print("Por favor ingrese un año coherente e inferior al año actual")
    except ValueError:
        print("Por favor ingrese un año valido")

