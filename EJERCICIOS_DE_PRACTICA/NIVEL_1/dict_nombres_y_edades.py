usuarios = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    usuarios[nombre] = edad

edad_promedio = sum(usuarios.values()) / len(usuarios)

print("Los datos ingresados son: ")
for nombre, edad in usuarios.items():
    print(f"{nombre} tiene {edad} años")

print(f"La edad promedio de los usuarios es: {round(edad_promedio, 2)} años")


    