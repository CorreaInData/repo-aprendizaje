def fecha_actual():
    while True:
        try:
            año_actual = int(input("Ingrese el año actual: "))
            if 1900 <= año_actual <= 2050:
                print("")
                return año_actual
            else:
                print("Ingrese un año válido entre 1900 y 2050.")
        except ValueError:
            print("Ingrese un número válido.")

def valida_año(año_actual):
    while True:
        try:
            año_nacimiento = int(input("Ingrese su año de nacimiento: "))
            if 1900 <= año_nacimiento <= año_actual:
                return año_nacimiento
            else:
                print(f"Por favor, ingrese un año entre 1900 y {año_actual}.")
        except ValueError:
            print("Ingrese un número válido.")

def calcula_edad(año_nacimiento, año_actual):
    edad = año_actual - año_nacimiento
    print(f"Tienes {edad} años.\n")

def continuacion():
    while True:
        continuar = input("¿Desea calcular otra edad? (s/n): ").strip().lower()
        if continuar in ["s", "n"]:
            return continuar
        print("Ingrese una opción válida (s/n).")

# Programa principal
año_actual = fecha_actual()

while True:
    año_nacimiento = valida_año(año_actual)
    calcula_edad(año_nacimiento, año_actual)
    if continuacion() == "n":
        print("Hasta luego.")
        break
