#Descomposicion de matrices
El algoritmo de Descomposición en Valores Singulares (DVS) es una aproximación a la descomposición de una matriz, lo cual nos ayuda en la reducción de una matriz cuadrada a cualquier otro tipo de matriz.
![Formula](https://miro.medium.com/v2/resize:fit:286/format:webp/0*eRpo9q5zMToD52Tl)
Sabiendo esto, volviendo a la fórmula, notamos entonces que M sería la matriz m x n que deseamos descomponer, U es la matriz singular izquierda que contiene a los vectores propios de la matriz.
Para un entendimiento simple de la función de cada matriz, podemos decir que las matrices U y V* causan una rotación en la matriz, mientras que la matriz Sigma ocasiona un escalamiento.

K se refiere al número de componentes principales que se mantienen al realizar la reducción de dimensionalidad, al truncar k valores singulares, estamos seleccionando los k componentes principales más significativos para la reconstrucción de la matriz, k determina cuánta información se conserva en la matriz reducida

![](/Descomposición%20de%20Matrices/Codigo.jpg)

Primero se tiene que crear la matriz que se quiere reducir, despues con la ayuda de numpy calculamos U,s y V.

Regresando estos resultados:
![](/Descomposición%20de%20Matrices/Resultado.JPG)
Como se puede ver la matriz fue reducida, con valores muy similares a la original.