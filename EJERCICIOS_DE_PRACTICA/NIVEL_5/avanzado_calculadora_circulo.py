import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("Error: El radio debe ser un número positivo mayor que cero.")
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * math.pow(self.radio, 2)

    def calcular_circunferencia(self):
        """Calcula la circunferencia del círculo."""
        return 2 * math.pi * self.radio

    def calcular_diametro(self):
        """Calcula el diámetro del círculo."""
        return 2 * self.radio

    def mostrar_resultados(self):
        """Muestra todas las propiedades del círculo."""
        print(f"\nCírculo con radio: {self.radio}")
        print(f"Área: {round(self.calcular_area(), 2)}")
        print(f"Circunferencia: {round(self.calcular_circunferencia(), 2)}")
        print(f"Diámetro: {round(self.calcular_diametro(), 2)}\n")

def obtener_radio():
    """Solicita al usuario el radio y valida la entrada."""
    while True:
        try:
            radio = float(input("\nIngrese el radio del círculo: "))
            return Circulo(radio)  # Crea el objeto directamente y maneja excepciones
        except ValueError as e:
            print(e)

def main():
    """Función principal del programa con menú interactivo."""
    circulo = obtener_radio()
    
    while True:
        print("\n--- Menú ---")
        print("1. Calcular Área")
        print("2. Calcular Circunferencia")
        print("3. Calcular Diámetro")
        print("4. Mostrar Todo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Área: {round(circulo.calcular_area(), 2)}")
        elif opcion == "2":
            print(f"Circunferencia: {round(circulo.calcular_circunferencia(), 2)}")
        elif opcion == "3":
            print(f"Diámetro: {round(circulo.calcular_diametro(), 2)}")
        elif opcion == "4":
            circulo.mostrar_resultados()
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
