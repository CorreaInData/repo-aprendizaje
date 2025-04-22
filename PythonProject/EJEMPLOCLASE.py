import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Cargamos los datos
data = pd.read_csv('loan.csv')

# Identificar valores faltantes
print(data.isnull().sum())

# Importar valores faltantes
imputer = SimpleImputer(strategy='mean')
data_imputed = imputer.fit_transform(data)

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Estandarización
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data_imputed)

# Normalización Min-Max
scaler = MinMaxScaler()
data_minmax = scaler.fit_transform(data_imputed)

# Normalización por rango intercuartilico
scaler = RobustScaler()
data_robust = scaler.fit_transform(data_imputed)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

# Preparación de los datos
x_train, x_test, y_train, y_test = train_test_split(data_robust, target, test_size=0.2, random_state=42)

# Regresión lineal
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

# Regresión logística
logistic_model = LogisticRegression()
logistic_model.fit(x_train, y_train)

# Evaluaciín de los modelos
print("Regresión lineal R-cuadrado:", linear_model.score(x_test, y_test))
print("Regresión lógistica precisión:", logistic_model.score(x_test, y_test))
