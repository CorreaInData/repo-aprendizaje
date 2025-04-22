import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de productos tecnológicos con precios realistas
productos = {
    "MacBook Pro 14\"": 1999.00,
    "iPhone 15 Pro": 999.00,
    "Samsung Galaxy S23": 899.99,
    "Dell XPS 15": 1499.99,
    "iPad Air (5ta Gen)": 599.00,
    "AirPods Pro (2da Gen)": 249.00,
    "Logitech MX Master 3S": 99.99,
    "Sony WH-1000XM5": 399.99,
    "HP Spectre x360": 1299.00,
    "Google Pixel 7 Pro": 899.00,
    "Microsoft Surface Laptop 5": 1299.00,
    "Apple Watch Series 8": 399.00,
    "Samsung Galaxy Tab S8": 699.99,
    "PlayStation 5": 499.99,
    "Xbox Series X": 499.00,
    "Nintendo Switch OLED": 349.99,
    "LG OLED C2 TV": 1499.00,
    "ASUS ROG Zephyrus G14": 1599.00,
    "JBL Charge 5": 179.99,
    "Kindle Paperwhite": 139.99,
}

# Generar 1500 registros aleatorios
datos = []
inicio_fecha = datetime(2023, 1, 1)
fin_fecha = datetime(2023, 12, 31)

for _ in range(1500):
    producto, precio = random.choice(list(productos.items()))
    fecha = inicio_fecha + timedelta(days=random.randint(0, (fin_fecha - inicio_fecha).days))
    cantidad = random.randint(1, 20)
    datos.append([fecha.strftime("%d/%m/%Y"), producto, cantidad, precio])

# Crear DataFrame y guardar en Excel
df = pd.DataFrame(datos, columns=["Fecha", "Producto", "Cantidad", "Precio Unitario (USD)"])
df.to_excel("ventas_tecnologia.xlsx", index=False)

print("¡Archivo 'ventas_tecnologia.xlsx' generado con éxito!")