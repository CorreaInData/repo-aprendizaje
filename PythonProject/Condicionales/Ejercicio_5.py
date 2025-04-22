''' Ejercicio 5
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones
1. Ingresar dinero a la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

saldo = 1000
print("           .:Menú:.           ")
print("""1. Ingresar dinero a la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir""")
opcion = int(input("Digite una opción del menú: "))
print("")

if opcion == 1:
    ingresado = float(input("Ingrese la cantidad que quiere ingresar a la cuenta: "))
    saldo += ingresado
    print(f"Dinero ingresado\nEl nuevo saldo disponible es de: {saldo}")
elif opcion == 2:
    retirado = float(input("Ingrese la cantidad que quiere retirar de la cuenta: "))
    if retirado > saldo:
        print("No hay suficiente dinero en la cuenta")
    else:
        saldo -= retirado
        print(f"Dinero retirado\nEl nuevo saldo disponible es de {saldo}")
elif opcion == 3:
    print("El saldo total disponible es: ",saldo)
elif opcion == 4:
    print("Vuelva pronto")
else:
    print("Opción ingresada no válida ")

''' Programa que se repite hasta que el usuario sale del cajero
saldo = 1000

while True:
    print("           .:Menú:.           ")
    print("1. Ingresar dinero a la cuenta\n2. Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir")
    opcion = int(input("Digite una opción del menú: "))
    print("")

    if opcion == 1:
        ingresado = float(input("Ingrese la cantidad que quiere ingresar a la cuenta: "))
        saldo += ingresado
        print(f"Dinero ingresado\nEl nuevo saldo disponible es de: {saldo}\n")
    elif opcion == 2:
        retirado = float(input("Ingrese la cantidad que quiere retirar de la cuenta: "))
        if retirado > saldo:
            print("No hay suficiente dinero en la cuenta\n")
        else:
            saldo -= retirado
            print(f"Dinero retirado\nEl nuevo saldo disponible es de {saldo}\n")
    elif opcion == 3:
        print(f"El saldo total disponible es: {saldo}\n")
    elif opcion == 4:
        print("Vuelva pronto")
        break
    else:
        print("Opción ingresada no válida ")
'''