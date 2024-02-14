import numpy as np

#1 Crear la matriz original
A = np.array([[3,3,3],
     [12,21,22],
     [43,12,11]])

#2 Realizar la descomposición SVD, con ayuda de numpy
U, s, V = np.linalg.svd(A)

#3 Definir el número de componentes principales a mantener
k = 2

#4 Reducir la matriz utilizando solo los primeros k componentes principales
Ak = np.dot(U[:, :k], np.dot(np.diag(s[:k]), V[:k, :]))

#5 Mostrar los resultados
print("Matriz original:")
print(A)
print("Matriz reducida:")
print(Ak)
print("Valores singulares:")
print(s)

