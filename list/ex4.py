'''EX4: Seja f(x) = (x − 2)^2 / (x + 3)^3
Estime A = integral definida de 0 a 1 de f(x)dx pela regra dos trapézios e pela regra de Simpson usando os valores tabelados:

x: 0.00, 0.25, 0.50, 0.75, 1.00
f(x): 1.4815 × 10^−1, 8.9213 × 10^−2, 5.2478 × 10^−2, 2.9630 × 10^−2, 1.5625 × 10^−2'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
f = np.array([0.14815, 0.089213, 0.052478, 0.029630, 0.015625])

#Parametros
h = 0.25
n = len(x) - 1 #n de intervalos = 4

#R. Trapezios
trapezios = (h/2) * (f[0] * 2 * np.sum(f[1:n]) + f[n])
#R. de Simpson
simpson = (h/3) * (f[0] + 4 * (f[1] + f[3]) + 2 * f[2] + f[n])

print(f'Integral pela regra dos trapezios: {trapezios:.4f}')
print(f'Integral pela regra de Simpson: {simpson:.4f}')