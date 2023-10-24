 # ADVERTENCIA SI DA ERROR REVISAR QUE TODAS LAS LIBRERÍAS QUE SE UTILIZAN VISUAL LAS RECONOCE. SINO, SE INSTALAN.
# TODO EL CODIGO SE BASA EN CASOS DONDE LAS VARIABLES SON ARRAYS EN CASO DE SER PANDAS SE CAMBIARÍAN LA ESTRUCTURA.

# Cual es la mejor libería para hacer modelos lineales (regresiones lineales)

# Principalmente existen dos Scikit-learn y Statsmodels. Siendo esta la más completa

# Un ejemplo de la utilización y resultados que ofrece la primera:

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos que queremos introducir (ejemplo)
mtros_cuadrados = np.array([[7,5,5,6,7,8,4]]).T
precios = np.array([[1800, 1600, 1500, 1000,5555,23555,1244]]).T

#regresor lineal
modelo = LinearRegression()
modelo.fit(mtros_cuadrados, precios) #datos que queremos meter en la grafica

# Predecir salida

valores_a_predecir = np.array([[50,60,55,80,120,130,145,150]]).T
y_predichos = modelo.predict(valores_a_predecir)

#Mostrar resultados por pantalla

print("Intercept:", modelo.intercept_)
print("Coeficiente de determinación R^2:", modelo.score(mtros_cuadrados, precios))
print("Coeficiente:", list(zip(mtros_cuadrados, modelo.coef_.flatten(), )))
print("y_predichos:\n\n",y_predichos)

# Calcular el error RMSE en el conjunto de prueba (en este caso son los datos originales)

predicciones = modelo.predict(mtros_cuadrados)
rmse = mean_squared_error(y_true=precios, y_pred=predicciones, squared=False)
print(f"\nEl error (RMSE) en el conjunto de prueba es: {rmse}\n\n")

################## En el caso de la segunda librería (Statsmodels) #################

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

#Creamos las variables predictora (X) y la resultado (Y)

X = np.array([[7, 5, 5, 6, 7, 8, 4, 5, 5, 5]]).T
Y = np.array([[1800, 1600, 1500, 1000, 5555, 23555, 1244, 1700, 1600, 1650]]).T

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=1234,
    shuffle=True
)

# Creación del modelo utilizando matrices como en scikitlearn

X_train = sm.add_constant(X_train, prepend=True)
modelo = sm.OLS(endog=y_train, exog=X_train,)
modelo = modelo.fit()
print(modelo.summary())

#################### CONCLUSIÓN #############################

# El primer método es más básico y nos ofrece menos información pero sirve para cualquier n. Sin embargo,
# en el caso de Statsmodels, es más completo pero nos interasará para aquellos casos donde la longitud 
# de las variables sean superior a 20 (ver la advertencia cuando se ejecuta el código en el principio de la tabla)
