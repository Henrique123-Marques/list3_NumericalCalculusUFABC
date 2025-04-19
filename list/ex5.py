'''EX5: Utilize a fórmula teórica do erro da regra dos trapézios para estimar o erro
cometido ao calcular a integral da questão anterior.'''
import numpy as np

a,b = 0,1
n = 4
h = (b-a)/n

def f_double_prime(x):
	return (2 * x**2 - 48 * x + 138) / (x + 3)**5

#Analisar Segunda derivada de f(x) no intervalo [0,1]
x_valores = np.linspace(0,1,100)
f_double_prime_valores = np.abs(f_double_prime(x_valores))
max_f_double_prime = np.max(f_double_prime_valores)

#estimativa erro
trapezio_erro = ((b - a) * h**2 / 12) * max_f_double_prime

print(f'Maximo de f´´(x) em [0,1]: {max_f_double_prime:.6f}')
print(f'Estimativa de erro pela regra dos trapezios: {trapezio_erro:.6f}')