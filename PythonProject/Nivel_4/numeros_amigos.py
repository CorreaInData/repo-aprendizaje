def divisores_propios(x):
    divisores = []
    for i in range(1, x):
        if x % i == 0:
            divisores.append(i)
    return divisores

while True:
    try:
        numero_1 = int(input("Ingrese el primer número: "))
        numero_2 = int(input("Ingrese el segundo número: "))
        if numero_1 > 0 and numero_2 > 0:
            break
        else:
            print("Por favor ingrese un número entero positivo")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

divisores_1 = divisores_propios(numero_1)
divisores_2 = divisores_propios(numero_2)

if sum(divisores_1) == numero_2 and sum(divisores_2) == numero_1:
    print(f"{numero_1} y {numero_2} son números amigos")
else:
    print(f"{numero_1} y {numero_2} no son números amigos")

