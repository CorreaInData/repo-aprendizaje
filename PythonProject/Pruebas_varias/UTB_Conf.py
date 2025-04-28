import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame simple
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
# Mostrar el DataFrame
print("DataFrame:\n", df)
# Crear un gráfico de línea
plt.plot(df['A'], df['B'])
plt.xlabel('A')
plt.ylabel('B')
plt.tle('Gráfico de Línea')
plt.show()