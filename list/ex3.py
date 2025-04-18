'''Com os mesmos dados da questão 2, encontre um modelo exponencial
y = a*e^bx que se ajuste melhor aos dados, utilizando mínimos quadrados.'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#Dados da qustao 2 (anterior)
x_data = np.array([-1,2,4])
y_data = np.array([-32,1,3])

#Soma dos quadrados, funcao de erro
def error(params, x, y):
	a, b = params
	y_pred = a * np.exp(b*x)
	return np.sum((y - y_pred)**2)

#Chute inicial para a e b
chute_inicial = [1, 0.5]
#minimizar erro
resultado = minimize(error, chute_inicial, args=(x_data, y_data), method="Nelder-Mead")
#parametros melhorados 
a,b = resultado.x

#Modelo exponencial
def y(x):
	return a * np.exp(b*x)

print(f'Modelo ajustado: y = {a:.4f} e^{b:.4f}x')
print('Verificando')
for x, y_true in zip(x_data, y_data):
	y_pred = y(x)
	print(f'x = {x}, y_dado = {y_true}, y_predito = {y_pred:.4f}')

#Grafico
x_plot = np.linspace(-2,5,100)
y_plot = y(x_plot)

plt.figure(figsize=(8,6))
plt.scatter(x_data, y_data, color='green', label='Pontos dados:', zorder=5)
plt.plot(x_plot, y_plot, 'b-', label=f'y = {a:.4f} e^{b:.4f}x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste exponencial por minimos quadrados')
plt.legend()
plt.grid(True)
plt.show()



