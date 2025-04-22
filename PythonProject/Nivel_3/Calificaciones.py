# Creación de la lista en la que se guardarán las calificaciones
calificaciones = []

# Solicita al usuario una calificación y valida la entrada.
while True:
    try:
        nota = int(input("Ingresa tu calificacion (0-100): "))
        if   0 <= nota <= 100: # nota < 0 or nota > 100:
            calificaciones.append(nota)
        else:
            print("Por favor ingrese una calificación en el rango indicado (0-100)")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

    seguir = input("¿Quieres seguir ingresando calificaciones? (s/n): ").strip().lower()
    if seguir == "n":
        break

print(f"Calificaciones ingresadas:{calificaciones}")

# Calculo del promedio, a partir de las calificaciones ingresadas y determina si aprobó o reprobó
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)

    # Muestra los resultados
    print("\n📊 Resumen")
    print(f"Calificaciones ingresadas:{calificaciones}")

    if promedio >= 60:
        print(f"Promedio: {promedio:.1f} ✅ APROBADO")
    else:
        print(f"Promedio: {promedio:.1f} ❌ REPROBADO")
else:
    print("No se ingresaron calificaciones. No se puede calcular el promedio")