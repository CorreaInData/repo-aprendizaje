def fecha_actual():
    while True:
        try:
            año_actual = int(input("Ingrese el año actual: "))
            if 1899 < año_actual <2050: # if 1900 <= año_actual <= 2050:
                print("")
                return año_actual
            else:
                print("Ingrese un año valido") # print("Ingrese un año válido entre 1900 y 2050.")
        except ValueError:
            print("Ingrese una entrada valida")

def valida_año():
    while True:
        try:
            año_nacimiento = int(input("Ingrese su año de nacimiento: "))
            if 1900 < año_nacimiento <= año_actual:
                return año_nacimiento
            else:
                print(f"Por favor ingrese un año entre 1900 y {año_actual}")
        except ValueError:
            print("Ingrese una entrada valida")

def calcula_edad():
    edad = año_actual - año_nacimiento
    print(f"Tienes {edad} años\n") 

def continuacion():
    while True:
        continuar = input("¿Desea continuar calculando edades s/n?: ").lower()
        if continuar == "s":
            return continuar
        elif continuar == "n":
            return continuar
        else:
            print("Ingrese una opción valida")
    
año_actual = fecha_actual()

while True:
    año_nacimiento = valida_año()
    calcula_edad()
    continuar = continuacion()
    if continuar == "n":
        print("Hasta luego")
        break

