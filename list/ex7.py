'''EX7: Considere a EDO y′(x) = −2x*y^2, com y(0) = 1. Estime a solução numérica no intervalo [0, 1] usando o 
método de Euler com h = 0,1.'''

import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
	return -2 * x * y**2

#parametros usados
a, b =0, 1
h = 0.1
n = int((b - a)/ h)
x = np.arange(a, b + h, h)
y = np.zeros(n + 1)
y[0] = 1.0

#Metodo de Euler
for i in range(n):
	y[i + 1] = y[i] + h * f(x[i], y[i])

#Resultados
print(f'Solução numérica pelo método de Euler com h = 0.1')
print("x\t\ty(x)")
print('-' * 20)
for xi, yi in zip(x, y):
	print(f'{xi:.1f}\t\t{yi:.6f}')

#grafico da solucao
plt.figure(figsize=(8,6))
plt.plot(x, y, 'b-o', label='Solução numérica (Euler)')
plt.scatter(x, y, color='red', zorder=5)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Solução da EDO y' = -2x y², y(0) = 1, pelo método de Euler (h = 0.1)")
plt.legend()
plt.grid(True)
plt.show()