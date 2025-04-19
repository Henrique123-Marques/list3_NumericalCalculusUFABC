'''Ex6: Calcule novamente a integral anterior, agora no intervalo de [0, 1,75]. Compare
os resultados da regra dos trapézios e de Simpson. Use os valores tabelados:

x: 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75
f(x): 1.4815*10^-1, 8.9213 * 10^-2, 5.2478*10^-2, 2.9630*10^-2, 1.5625*10^-2, 8.2150*10^-3, 4.0100*10^-3, 2.1000*10^-3'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75])
f = np.array([0.14815, 0.089213, 0.052478, 0.029630, 0.015625, 0.008215, 0.004010, 0.002100])

def f_exato(x):
	return (x - 2)**2 / (x + 3)**3

#parametros usados
a, b = 0, 1.75
n = len(x) - 1
h = (b - a) / n

#R. Trapezios
trapezios = (h / 2) * (f[0] + 2 * np.sum(f[1:n]) + f[n])

#Separando a regra de simpson (composta ate x=1.5 + trapezio)
n_simpson = 6
simpson = (h/3) * (f[0] + 4 * (f[1] + f[3] +f[5]) + 2 * (f[2] + f[4]) + f[6])
trapezio_aux = (h/2) * (f[6] + f[7])
simpson_soma = simpson + trapezio_aux

#Pontos para a curva
x_fine = np.linspace(0, 1.75, 100)
y_fine = f_exato(x_fine)

plt.figure(figsize=(10,6))
plt.plot(x_fine, y_fine, 'b-', label='f(x) = (x-2)^2/(x+3)^3')
plt.scatter(x,f, color='red', label='Pontos tabelados', zorder=5)

#plote dos trapezios
for i in range(n):
	plt.fill_between([x[i], x[i+1]], [f[i], f[i+1]], alpha=0.2, color="green", label='Trapezios' if i == 0 else "")

#eixos e detalhes
plt.axhline(0, color ='black', linestyle='--', alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integral de f(x) de 0 a 1.75\nTrapézios: {trapezios:.6f}, Simpson: {}simpson_total:.6f')
plt.legend()
plt.grid(True)
plt.show()

print(f'Integral pela regra dos trapezios: {trapezios:.6f}')
print(f'Intregral pela regra de Simpson: {simpson_total:.6f}')