'''EX8; Resolva novamente a EDO da questão anterior usando o método de Runge-
Kutta de 2a ordem (RK2) com h = 0,1.'''

import numpy as np
import matplotlib.pyplot as plt

# Função que define a EDO: y' = -2x * y^2
def f(x, y):
    return -2 * x * y**2

# Solução exata para comparação
def y_exact(x):
    return 1 / (x**2 + 1)

# Parâmetros
a, b = 0, 1  # Intervalo [0, 1]
h = 0.1      # Tamanho do passo
n = int((b - a) / h)  # Número de passos
x = np.arange(a, b + h, h)  # Pontos x: 0, 0.1, ..., 1.0
y = np.zeros(n + 1)  # Array para armazenar y
y[0] = 1.0   # Condição inicial: y(0) = 1

# Método de Runge-Kutta de 2ª ordem (RK2)
for i in range(n):
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h, y[i] + h * k1)
    y[i + 1] = y[i] + h * k2

# Calcular solução exata
y_ex = y_exact(x)

# Exibir resultados
print("Solução numérica pelo método de Runge-Kutta de 2ª ordem (h = 0.1):")
print("x\t\ty_RK2\t\ty_exata\t\tErro")
print("-" * 50)
for xi, yi, ye in zip(x, y, y_ex):
    print(f"{xi:.1f}\t\t{yi:.6f}\t{ye:.6f}\t{abs(yi - ye):.6f}")

# Plotar a solução
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-o', label='Solução numérica (RK2)')
plt.plot(x, y_ex, 'r--', label='Solução exata: y = 1/(x² + 1)')
plt.scatter(x, y, color='blue', zorder=5)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Solução da EDO y' = -2x y², y(0) = 1, pelo método RK2 (h = 0.1)")
plt.legend()
plt.grid(True)
plt.show()