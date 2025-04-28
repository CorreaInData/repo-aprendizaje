import math
while True:
    try:
        radio = float(input("\nIngrese el radio del circulo: "))
        if radio > 0:
            area = math.pi * math.pow(radio, 2)
            print(f"El área del circulo es: {round(area, 2)}")
            break
        else:
            print("Error: El radio debe ser un número positivo mayor que cero. ")
    except ValueError:
        print("Ingrese un número válido")

