# DESCENSO DE GRADIENTE
El descenso de gradiente es un algoritmo de optimización que se usa comúnmente para entrenar modelos de machine learning y redes neuronales.  Los datos de entrenamiento ayudan a que estos modelos aprendan con el tiempo, y la función de costo dentro del descenso de gradiente actúa específicamente como un barómetro, midiendo su precisión con cada iteración de actualizaciones de parámetros. Hasta que la función sea cercana o igual a cero, el modelo continuará ajustando sus parámetros para producir la menor cantidad de errores posible.

El algoritmo de descenso de gradiente se comporta de manera similar a la pendiente de una línea, el punto de partida es solo un punto arbitrario para que podamos evaluar el rendimiento. Desde ese punto de partida, encontraremos la derivada (o pendiente), y desde allí, podemos usar una recta tangente para observar la inclinación de la pendiente. La pendiente informará las actualizaciones de los parámetros, es decir, los pesos y el sesgo. La pendiente en el punto de partida será más pronunciada, pero a medida que se generen nuevos parámetros, la pendiente debe reducirse gradualmente hasta alcanzar el punto más bajo de la curva, conocido como punto de convergencia.

El objetivo del descenso de gradiente es minimizar la función de costo, o el error entre la "y" real y su valor pronosticado. Para hacer esto, se necesitan dos puntos de datos: una dirección y una tasa de aprendizaje. Estos factores determinan los cálculos de derivadas parciales de iteraciones futuras, lo que le permite llegar gradualmente al mínimo local o global.

* **Índice de aprendizaje:** es el tamaño de los pasos que se dan para alcanzar el mínimo. Suele ser un valor pequeño y se evalúa y actualiza en función del comportamiento de la función de costos. Los índices de aprendizaje altos dan como resultado pasos más grandes, pero existe el riesgo de exceder el mínimo. Por el contrario, los índices de aprendizaje bajos generan tamaños de paso más pequeños. Si bien tiene la ventaja de una mayor precisión, el número de iteraciones compromete la eficiencia general, ya que esto requiere más tiempo y cálculos para alcanzar el mínimo.  
* **La función de costo:** Mide la diferencia, o error, entre la "y" real y la "y" pronosticada en su posición actual. Esto mejora la eficacia del modelo de machine learning, ya que proporciona información al modelo para que pueda ajustar los parámetros para minimizar el error y encontrar el mínimo local o global. Repite continuamente, moviéndose a lo largo de la dirección de descenso más pronunciado (o el gradiente negativo) hasta que la función de costo se acerca o llega a cero.

![](/Optimizacion_Operaciones/Formula.JPG)

![](/Optimizacion_Operaciones/Taza_aprendizaje.png)

> La tasa de aprendizaje de la izquierda es excesiva, por lo que la función no encuentra el punto óptimo. En el caso de la derecha, como los pasos son muy pequeños, es muy probable que el algoritmo acierte, aunque de forma muy lenta.

![](/Optimizacion_Operaciones/Codigo1.JPG)

![](/Optimizacion_Operaciones/Codigo2.JPG)

- Creamos datos sintéticos donde la variable dependiente y es una función lineal de la variable independiente X.
- Definimos un modelo de regresión lineal simple.
- Utilizamos el error cuadrático medio como función de costo.
- Utilizamos el Descenso de Gradiente Estocástico (SGD) como optimizador para actualizar los parámetros del modelo.
- Iteramos a través de un número fijo de épocas (iteraciones), realizando pasos de forward y backward en cada iteración.
- Visualizamos la evolución de la pérdida durante el entrenamiento y la regresión lineal resultante.

![](/Optimizacion_Operaciones/Resultado1.JPG)

Se puede ver como la perdida se reduce conforme aumenta la epoca.

![](/Optimizacion_Operaciones/Resultado2.JPG)

Podemos ver como la regresión lineal es muy parecida a la verdadera.

![](/Optimizacion_Operaciones/Resultado3.JPG)

Al aumentar las epocas a 200 el resultado es mas preciso.