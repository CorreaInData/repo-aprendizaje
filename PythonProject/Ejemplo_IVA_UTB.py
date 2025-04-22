# Constantes
IVA = 0.19

# Función para calcular el subtotal, IVA, total y descuentos
def calcular_factura(cantidad, precio_con_iva):
    # Calculamos el subtotal sin IVA
    subtotal = cantidad * (precio_con_iva / (1 + IVA))

    # Calculamos el valor del IVA
    valor_iva = subtotal * IVA

    # Aplicamos los descuentos dependiendo del subtotal
    # descuento = 0
    if 500000 <= subtotal <= 999999:
        descuento = subtotal * 0.10
    elif 1000000 <= subtotal <= 1999999:
        descuento = subtotal * 0.20
    elif subtotal >= 2000000:
        descuento = subtotal * 0.30
    else:
        descuento=0
    # Calculamos el total con el descuento aplicado
    total = (subtotal - descuento) + valor_iva

    # Retornamos los valores calculados
    return subtotal, valor_iva, descuento, total

# Capturamos los datos del usuario
cantidad = int(input("Ingrese la cantidad de productos: "))
precio_con_iva = float(input("Ingrese el precio del producto con IVA incluido: "))

# Realizamos los cálculos
subtotal, valor_iva, descuento, total = calcular_factura(cantidad, precio_con_iva)

# Mostramos los resultados
print(f"\nSubtotal (sin IVA): ${subtotal:,.2f}")
print(f"Valor del IVA: ${valor_iva:,.2f}")
print(f"Descuento aplicado: ${descuento:,.2f}")
print(f"Total a pagar: ${total:,.2f}")
