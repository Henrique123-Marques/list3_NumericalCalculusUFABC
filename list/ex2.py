'''EX2 - Achar umn polinomio de grau 2 que satisfaca 
as condicoes: p(-1) = -32, p(2) = 1, p(4) = 3
'''

'''Explicacao breve: O polinomio tem a forma p(x) = a*x^2 + b*x + c, então: 
p(-1) = a*(-1)^2 + b*(-1) + 1 = a*1 + b*(-1) + 1;
p(2) = a*2^2 + b*2 + 1 = a*4 + b*2 + 1;
p(4) = a*4^2 + b*4 + 1 = a*16 + b*4 + 1,

Essas solucoes foram um sistema linear cuja solucao são -32, 1, 3'''
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
	[1,-1,1], [4,2,1], [16,4,1]
	])

B = np.array([-32, 1, 3])

a,b,c = np.linalg.solve(A,B)

print(f'O polinomio é: p(x) = {a:.2f}x^2 + {b:.2f}x + {c:.2f}')

def p(x):
	return a * x**2 + b * x + c

print(f'Veriicando:')
print(f'p(-1) = {p(-1):.2f}')
print(f'p(2) = {p(2):.2f}')
print(f'p(4) = {p(4):.2f}')

#Grafico
x = np.linspace(-2, 5, 100) 
y = p(x)

# Pontos dados
x_pontos = np.array([-1, 2, 4])
y_pontos = np.array([-32, 1, 3])

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label=f'p(x) = {a:.2f}x² + {b:.2f}x + {c:.2f}')  # Polinômio
plt.scatter(x_pontos, y_pontos, color='red', label='Pontos fornecidos', zorder=5)  # Pontos dados
plt.axhline(0, color='black', linestyle='--', alpha=0.3)  # Linha y = 0
plt.axvline(0, color='black', linestyle='--', alpha=0.3)  # Linha x = 0
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Gráfico do Polinômio de Grau 2')
plt.legend()
plt.grid(True)
plt.show()