list_numero = []
pares = []
impares = []

while True:
    try:
        numero = int(input("Ingrese un número entero positivo (0 para terminar)"))
        if numero > 0: 
            list_numero.append(numero)
        elif numero == 0:
            break
        else:
            print("Por favor ingrese un número entero positivo (0 para terminar)")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

for i in list_numero:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("\n📊 Resumen:")

if pares:
    print(f"Números pares: {pares} (cantidad: {len(pares)}) - promedio: {sum(pares)/len(pares):.2f}")
else:
    print("No se ingresaron números pares.")

if impares:
    print(f"Números impares: {impares} (cantidad: {len(impares)}) - promedio: {sum(impares)/len(impares):.2f}")
else:
    print("No se ingresaron números impares.")