def seleccionar_unidad():
    while True:
        try:
            seleccion = int(input("Indique que unidades desea convertir:"\
                                "\n1. Temperatura."\
                                "\n2. Longitud."\
                                "\n3. Divisas."\
                                "\n4. Salir."\
                                "\n--> "))
            if seleccion in [1, 2, 3, 4]:
                return seleccion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def convertir_temperatura():
    try:
        print("\nConversor de Temperatura")
        temperatura = float(input("Ingrese la temperatura: "))
        und_temperatura = input("Ingrese la unidad de origen (C/F):").upper()

        if und_temperatura == "C":
            resultado = (temperatura * 9/5) + 32
            print(f"Resultado: {temperatura}°C es igual a {resultado}°F")
        elif und_temperatura == "F":
            resultado = (temperatura - 32) * 5/9
            print(f"Resultado: {temperatura}°F es igual a {resultado}°C")
        else:
            print("Unidad no válida.")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

def convertir_longitud():
    conversiones_longitud = {
        "cm": {"ft": 0.0328084, "in": 0.393701, "m": 0.01, "km": 0.00001, "mi": 0.0000062137},
        "ft": {"cm": 30.48, "in": 12, "m": 0.3048, "km": 0.0003048, "mi": 0.000189394},
        "in": {"cm": 2.54, "ft": 0.0833333, "m": 0.0254, "km": 0.0000254, "mi": 0.000015783},
        "m": {"cm": 100, "ft": 3.28084, "in": 39.3701, "km": 0.001, "mi": 0.000621371},
        "km": {"cm": 100000, "ft": 3280.84, "in": 39370.1, "m": 1000, "mi": 0.621371},
        "mi": {"cm": 160934, "ft": 5280, "in": 63360, "m": 1609.34, "km": 1.60934}
    }
    try:
        print("\nConversor de Longitud")
        longitud = float(input("Ingrese la longitud: "))
        unidad_origen = input("Ingrese la unidad de origen: ").lower()
        unidad_destino = input("Ingrese la unidad de destino: ").lower()

        if unidad_origen in conversiones_longitud and unidad_destino in conversiones_longitud[unidad_origen]:
            resultado = longitud * conversiones_longitud[unidad_origen][unidad_destino]
            print(f"Resultado: {longitud} {unidad_origen} es igual a {resultado} {unidad_destino}")
        else:
            print("Conversión no válida.")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

def convertir_divisas():
    conversiones_divisas = {
        "USD": {"EUR": 0.93, "COP": 4179.04},
        "EUR": {"USD": 1.08, "COP": 4527.2},
        "COP": {"USD": 0.00024, "EUR": 0.00022}
    }
    try:
        print("\nConversor de Divisas")
        cantidad = float(input("Ingrese la cantidad de dinero: "))
        divisa_origen = input("Ingrese la divisa de origen (USD, EUR, COP): ").upper()
        divisa_destino = input("Ingrese la divisa de destino (USD, EUR, COP): ").upper()

        if divisa_origen in conversiones_divisas and divisa_destino in conversiones_divisas[divisa_origen]:
            resultado = cantidad * conversiones_divisas[divisa_origen][divisa_destino]
            print(f"Resultado: {cantidad} {divisa_origen} es igual a {resultado} {divisa_destino}")
        else:
            print("Conversión no válida.")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

def main():
    while True:
        seleccion = seleccionar_unidad()

        if seleccion == 1:
            convertir_temperatura()
        elif seleccion == 2:
            convertir_longitud()
        elif seleccion == 3:
            convertir_divisas()
        elif seleccion == 4:
            print("\n¡Hasta luego!")
            break

        print("------------------------------------------------------")

if __name__ == "__main__":
    main()
