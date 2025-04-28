import math

# Importante el uso de docstings
def radio_circulo(): # nombrar clase obtener_radio() para mejor claridad
    """Solicita el radio y valida la entrada"""
    while True:
        try:
            radio = float(input("Ingrese el radio del circulo: "))
            if radio > 0:
                return radio
            else:
                print("Error: El radio debe ser un número positivo mayor que cero. ")
        except ValueError:
            print("Error: Ingrese un número válido")

def calculo_area(radio): # nombrar clase calcular_area() para mejor claridad
    """Calcula el área del circulo"""
    area = math.pi * math.pow(radio, 2)
    print(f"El área del circulo es: {round(area, 2)}")

def main():
    """Función principal"""
    radio = radio_circulo()
    calculo_area(radio)

# Ejecutar el programa  
main()