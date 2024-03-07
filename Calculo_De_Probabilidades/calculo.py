from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import math

##Funcion Logistica vectorial
logistica = np.frompyfunc(lambda b0, b1, x:
    1 / (1 + math.exp(-(b0 + b1*x))),
    3,1)

##Datos
edades = [[5],[7],[9],[12],
          [12],[12],[13],[15],
          [20],[25],[26],[30],
          [31],[36],[77],[80]]

##1 es que le gustan, 0 que no
clase = [[1],[1],[1],[0],
         [1],[1],[0],[1],
         [0],[1],[1],[0],
         [0],[1],[0],[0]]

##Sacamos una muestra de los datos
datos_entrena, datos_prueba, clase_entrena, clase_prueba = \
    train_test_split(edades,
                     clase,
                     test_size=0.5)

##Creamos el modelo
modelo = LogisticRegression().fit(datos_entrena,clase_entrena)
np.set_printoptions(suppress=True)
print(modelo.predict(datos_prueba))
print(modelo.predict_proba(datos_prueba))
print(modelo.score(datos_prueba,clase_prueba))
print(modelo.intercept_, modelo.coef_)

##Creamos la grafica
plt.figure(figsize=(8,4))
plt.scatter(np.arange(5,80,0.1),
            logistica(modelo.intercept_, modelo.coef_,
            np.arange(5,80,0.1)))
plt.scatter(datos_prueba, clase_prueba, marker="o", c="Green", s=250, label="Datos prueba")
nuevos_individuos =[40,18,15]
probabilidades = logistica(modelo.intercept_, modelo.coef_, nuevos_individuos)
plt.scatter(nuevos_individuos, probabilidades, marker="*", c="darkred", s=500)
plt.xlabel("Probabilidades de que le gusten los videojuegos", fontsize=13.0)
plt.xlabel("Edades de muestra", fontsize=13.0)
plt.show()