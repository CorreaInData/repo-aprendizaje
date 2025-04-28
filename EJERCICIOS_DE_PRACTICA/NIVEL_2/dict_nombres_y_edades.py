usuarios = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
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

edad_promedio = sum(usuarios.values()) / len(usuarios)

print("Los datos ingresados son: ")
for nombre, edad in usuarios.items():
    print(f"{nombre} tiene {edad} años")

print(f"La edad promedio de los usuarios es: {round(edad_promedio, 2)} años")