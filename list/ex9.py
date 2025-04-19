'''EX9: Compare graficamente as soluções obtidas por Euler e RK2 com a solução exata y(x) = 1/(1 + x^2). Comente as diferenças observadas.'''
import numpy as np
import matplotlib.pyplot as plt

#funcao EDO definida
def f(x,y):
	return -2 * x * y ** 2

#Solucao exata para comparar
def y_exato(x):
	return 1/ (x ** 2 + 1)

#parametros usados
a, b = 0, 1
h = 0.1 #tamanho do passo
n = int((b-a) / h)
x = np.arange(a, b + h, h)
y = np.zeros(n + 1)
y[0] = 1.0

#metodo de Runge-Kutta de ordem 2 (RK2)
for i in range(n):
 	k1 = f(x[i], y[i])
 	k2 = f(x[i] + h, y[i] + h * k1)
 	y[i + 1] = y[i] + h * k2
#solucao exata
y_ex = y_exato(x)

#resultado
print("Solução numérica pelo método de Runge-Kutta de 2ª ordem (h = 0.1):")
print("x\t\ty_RK2\t\ty_exata\t\tErro")
print("-" * 50)
for xi, yi, ye in zip(x, y, y_ex):
    print(f"{xi:.1f}\t\t{yi:.6f}\t{ye:.6f}\t{abs(yi - ye):.6f}")

#Grafico
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












