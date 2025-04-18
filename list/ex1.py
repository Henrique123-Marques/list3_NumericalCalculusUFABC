'''EX1 - Encontre a raiz da função y(x) dada pelos pontos abaixo. Use interpolação de
Lagrange sobre (a) três e (b) quatro pontos consecutivos.

x: 0, 0.5, 1, 1.5, 2, 2.5, 3
y(x) 1.8421, 2.4694, 2.4921, 1.9047, 0.8509, -0.4112, -1.5727'''

import numpy as np
from scipy.interpolate import lagrange
from scipy.optimize import root
import matplotlib.pyplot as plt

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
y = np.array([1.8421, 2.4694, 2.4921, 1.9047, 0.8509, -0.4112, -1.5727])

# Função para interpolação de Lagrange e encontrar raiz
def lagrange_interpolation(x_data, y_data, x_eval):
    poly = lagrange(x_data, y_data)
    return poly(x_eval)

# (a) Interpolação com 3 pontos consecutivos (x = 1.5, 2, 2.5)
x_3 = x[3:6]  # [1.5, 2, 2.5]
y_3 = y[3:6]  # [1.9047, 0.8509, -0.4112]
poly_3 = lagrange(x_3, y_3)

#raiz para 3 pontos
def func_3(x):
    return poly_3(x)

root_3 = root(func_3, 2.25)  # Chute inicial entre 2 e 2.5
x_root_3 = root_3.x[0]
y_root_3 = poly_3(x_root_3)

# (b) Interpolação com 4 pontos consecutivos (x = 1, 1.5, 2, 2.5)
x_4 = x[2:6]  # [1, 1.5, 2, 2.5]
y_4 = y[2:6]  # [2.4921, 1.9047, 0.8509, -0.4112]
poly_4 = lagrange(x_4, y_4)

#raiz para 4 pontos
def func_4(x):
    return poly_4(x)

root_4 = root(func_4, 2.25)  # Chute entre 2 e 2.5
x_root_4 = root_4.x[0]
y_root_4 = poly_4(x_root_4)

# Plotagem
x_fine = np.linspace(1, 3, 100) 
y_3_fine = lagrange_interpolation(x_3, y_3, x_fine)
y_4_fine = lagrange_interpolation(x_4, y_4, x_fine)

plt.figure(figsize=(10, 6))
# Pontos originais
plt.scatter(x, y, color='black', label='Pontos fornecidos', zorder=5)
# Interpolação de 3 pontos
plt.plot(x_fine, y_3_fine, 'b-', label='Lagrange (3 pontos)')
plt.scatter(x_root_3, y_root_3, color='blue', label=f'Raiz (3 pontos): x ≈ {x_root_3:.4f}', zorder=5)
# Interpolação de 4 pontos
plt.plot(x_fine, y_4_fine, 'r-', label='Lagrange (4 pontos)')
plt.scatter(x_root_4, y_root_4, color='red', label=f'Raiz (4 pontos): x ≈ {x_root_4:.4f}', zorder=5)
# Linha y = 0
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Interpolação de Lagrange e Raízes')
plt.legend()
plt.grid(True)
plt.show()

print(f"Raiz com 3 pontos (x = 1.5, 2, 2.5): x ≈ {x_root_3:.4f}")
print(f"Raiz com 4 pontos (x = 1, 1.5, 2, 2.5): x ≈ {x_root_4:.4f}")