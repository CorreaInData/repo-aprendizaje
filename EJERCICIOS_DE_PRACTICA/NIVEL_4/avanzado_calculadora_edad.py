import datetime

class Persona:
    def __init__(self, nombre, año_nacimiento):
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento

    def calcular_edad(self):
        año_actual = datetime.datetime.now().year
        return año_actual - self.año_nacimiento

def obtener_año_nacimiento():
    while True:
        try:
            año = int(input("Ingrese su año de nacimiento: "))
            año_actual = datetime.datetime.now().year
            if 1900 <= año <= año_actual:
                return año
            else:
                print(f"Ingrese un año válido entre 1900 y {año_actual}.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        año_nacimiento = obtener_año_nacimiento()
        
        persona = Persona(nombre, año_nacimiento)
        print(f"{persona.nombre} tiene {persona.calcular_edad()} años.\n")
        
        continuar = input("¿Desea calcular otra edad? (s/n): ").strip().lower()
        if continuar == "n":
            print("Hasta luego.")
            break

main()
