usuarios = {}

def ingresar_usuarios():
    nombre = input(f"\nIngrese el nombre del usuario: ")
    while True:
        try:
            edad = int(input(f"Ingrese la edad de {nombre}: "))
            if 0 <= edad <= 110:
                usuarios[nombre] = edad
                break
            elif edad < 0:
                print("Error: Está ingresando una edad negativa")
            elif edad > 110:
                print("Error: Una persona no vive más de 110 años")
        except ValueError:
            print("Error: Ingrese un número entero para la edad")
    return usuarios

def querer_continuar():
    while True:
        continuar = input("¿Desea continuar agregando usuarios? s/n: ").lstrip().lower()
        if continuar == "s":
            return continuar
        elif continuar == "n":
            return continuar
        else:
            print("Error: Ingrese un dato correcto")

while True:
    usuarios = ingresar_usuarios()
    continuar = querer_continuar()
    if continuar == "n":
        print("\nLos datos ingresados son: ")
        for nombre, edad in usuarios.items():
            print(f"{nombre} tiene {edad} años")
        print("\nHasta luego")
        break
