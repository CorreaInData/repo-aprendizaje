import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_tecnologia.csv")

# Renombre de columnas para una mejor escritura
df.rename(columns={'Fecha': 'fecha', 'Producto': 'producto', 'Cantidad': 'cantidad','Precio Unitario (USD)': 'precio_unitario'}, inplace=True)

# Cambia el tipo de dato en la columna data de object (cadena en pandas) a datatime
df['fecha'] = pd.to_datetime(df['fecha']) 

# Calcula los ingresos totales por venta
df['ingresos_totales'] = df['precio_unitario'] * df['cantidad']


# 1. Mes con mayores ventas
df['mes'] = df['fecha'].dt.month
ventas_por_mes = df.groupby('mes')['ingresos_totales'].sum() # Agrupa con base a ['mes'] los valores de ['ingresos_totales'] y los suma .sum()
mes_max_ventas = ventas_por_mes.idxmax()
print(f"El mes con mayores ventas es: {mes_max_ventas}")

# 2. Productos más vendidos en términos de cantidad total
productos_vendidos = df.groupby('producto')['cantidad'].sum() # Agrupa con base a ['producto'] los valores de ['cantidad'] y los suma .sum()
producto_mas_vendido = productos_vendidos.idxmax()
print(f"El producto más vendido en términos de cantidad total es: {producto_mas_vendido}")

# 3. Precio promedio de los productos vendidos
precio_promedio = df['precio_unitario'].mean()
print(f"El precio promedio de los productos vendidos es: {precio_promedio}")

# 4. Gráfico de líneas de ventas a lo largo del año
df_fecha = df.groupby('fecha')['ingresos_totales'].sum() # Agrupa los ['ingresos_totales'] con base a la ['fecha']
plt.figure(figsize=(12, 6)) # Indica la medida del gráfico
plt.plot(df_fecha.index, df_fecha.values) # Determina eje x (fecha) y eje y (ingresos por fecha)
plt.title('Tendencia de ventas a lo largo del año') # Indica titulo del gráfico
plt.xlabel('Fecha') # Nombra al eje x
plt.ylabel('Ingresos totales') # Nombra al eje y
plt.show() # Muestra el gráfico

# 5. Gráfico de barras de ventas por producto
ventas_por_producto = df.groupby('producto')['ingresos_totales'].sum() # Agrupa los ['ingresos_totales'] con base al ['producto'] 
plt.figure(figsize=(10, 6)) # Indica la medida del gráfico
plt.bar(ventas_por_producto.index, ventas_por_producto.values) # Determina eje x (producto) y eje y (ingresos por producto) 
plt.xticks(rotation=45) # Rota el eje x para una mejor lectura
plt.title('Ventas totales por producto')  # Indica titulo del gráfico
plt.xlabel('Producto') # Nombra al eje x
plt.ylabel('Ingresos totales')# Nombra al eje y
plt.show() # Muestra el gráfico

#print(df.info())