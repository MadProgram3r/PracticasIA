import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Creamos datos sintéticos
torch.manual_seed(42)  # Fijamos la semilla aleatoria para reproducibilidad
X = torch.randn(100, 1)  # 100 muestras con 1 característica cada una
y = 3 * X + 2 + torch.randn(100, 1) * 0.1  # Modelo verdadero: y = 3*X + 2 + ruido

# Definimos el modelo de regresión lineal
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # Capa lineal con 1 entrada y 1 salida

    def forward(self, x):
        return self.linear(x)

# Instanciamos el modelo
model = LinearRegression()

# Definimos la función de costo (error cuadrático medio)
criterion = nn.MSELoss()

# Definimos el optimizador (Descenso de Gradiente)
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Entrenamos el modelo
num_epochs = 100
losses = []
for epoch in range(num_epochs):
    # Paso de forward: computamos la predicción y el costo
    y_pred = model(X)
    loss = criterion(y_pred, y)
    losses.append(loss.item())

    # Paso de backward: computamos los gradientes y actualizamos los parámetros
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Imprimimos la pérdida cada 10 épocas
    if (epoch+1) % 10 == 0:
        print(f'Época [{epoch+1}/{num_epochs}], Pérdida: {loss.item():.4f}')

# Visualizamos la evolución de la pérdida durante el entrenamiento
plt.plot(losses)
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.title('Evolución de la Pérdida durante el Entrenamiento')
plt.show()

# Visualizamos la regresión lineal resultante
plt.scatter(X.numpy(), y.numpy(), label='Datos')
plt.plot(X.numpy(), model(X).detach().numpy(), color='red', linewidth=3, label='Regresión Lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal Resultante')
plt.legend()
plt.show()

