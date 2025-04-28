import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * math.pow(self.radio, 2)

    def mostrar_area(self):
        """Muestra el área del círculo con 2 decimales."""
        print(f"El área del círculo es: {round(self.calcular_area(), 2)}")

def obtener_radio():
    """Solicita al usuario el radio y valida la entrada."""
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio > 0:
                return radio
            else:
                print("Error: El radio debe ser un número positivo mayor que cero.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    """Función principal del programa."""
    radio = obtener_radio()
    circulo = Circulo(radio)
    circulo.mostrar_area()

if __name__ == "__main__":
    main()
