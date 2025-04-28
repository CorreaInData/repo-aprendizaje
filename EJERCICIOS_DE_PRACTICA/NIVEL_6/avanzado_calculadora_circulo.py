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

    def obtener_resultados(self):
        """Devuelve los cálculos del círculo en formato de texto."""
        return (f"Radio: {self.radio}\n"
                f"Área: {round(self.calcular_area(), 2)}\n"
                f"Circunferencia: {round(self.calcular_circunferencia(), 2)}\n"
                f"Diámetro: {round(self.calcular_diametro(), 2)}\n"
                "------------------------\n")

def obtener_radio():
    """Solicita al usuario el radio y valida la entrada."""
    while True:
        try:
            radio = float(input("\nIngrese el radio del círculo: "))
            return Circulo(radio)  # Crea el objeto directamente y maneja excepciones
        except ValueError as e:
            print(e)

def guardar_resultados(circulos):
    """Guarda los resultados en un archivo de texto."""
    with open("resultados.txt", "w") as file:
        for circulo in circulos:
            file.write(circulo.obtener_resultados())
    print("\n✅ Resultados guardados en 'resultados.txt'.")

def main():
    """Función principal del programa con menú interactivo."""
    circulos = []  # Lista para almacenar múltiples círculos
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar un nuevo círculo")
        print("2. Mostrar todos los cálculos")
        print("3. Guardar resultados en un archivo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            circulo = obtener_radio()
            circulos.append(circulo)
            print("\n✅ Círculo agregado con éxito.")
        elif opcion == "2":
            if not circulos:
                print("\n⚠️ No hay círculos almacenados.")
            else:
                print("\n--- Resultados ---")
                for circulo in circulos:
                    print(circulo.obtener_resultados())
        elif opcion == "3":
            if not circulos:
                print("\n⚠️ No hay resultados para guardar.")
            else:
                guardar_resultados(circulos)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
