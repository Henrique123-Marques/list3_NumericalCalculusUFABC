import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cálculo Numérico Q1 2025 - Lista 3", layout="wide")

# Função para o Exercício 6
def exercicio_6():
    # Função exata
    def f_exato(x):
        return (x - 2)**2 / (x + 3)**3

    # Dados tabelados
    x = np.array([0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75])
    f = np.array([0.14815, 0.089213, 0.052478, 0.029630, 0.015625, 0.008215, 0.004010, 0.002100])

    # Parâmetros
    a, b = 0, 1.75
    n = len(x) - 1
    h = (b - a) / n

    # Função para calcular as integrais
    def calcular_integrais():
        # Regra dos Trapézios
        trapezios = (h / 2) * (f[0] + 2 * np.sum(f[1:n]) + f[n])

        # Regra de Simpson composta + trapézio
        n_simpson = 6
        simpson = (h/3) * (f[0] + 4 * (f[1] + f[3] + f[5]) + 2 * (f[2] + f[4]) + f[6])
        trapezio_aux = (h/2) * (f[6] + f[7])
        simpson_soma = simpson + trapezio_aux
        
        return trapezios, simpson_soma

    # Função para criar o gráfico
    def plot_integral(trapezios, simpson_soma):
        x_fine = np.linspace(0, 1.75, 100)
        y_fine = f_exato(x_fine)
        
        fig, ax = plt.subplots(figsize=(6, 3))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        ax.plot(x_fine, y_fine, 'b-', label=r'$f(x) = \frac{(x-2)^2}{(x+3)^3}$')
        ax.scatter(x, f, color='red', label='Pontos tabelados', zorder=5)
        for i in range(n):
            ax.fill_between([x[i], x[i+1]], [f[i], f[i+1]], alpha=0.2, color="green", 
                           label='Trapézios' if i == 0 else "")
        ax.axhline(0, color='black', linestyle='--', alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)
        return fig

    # Interface do Streamlit
    st.title("Integral por Regra dos Trapézios e Simpson no intervalo [0, 1.75]")

    # Abas com ícones
    tab1, tab2, tab3 = st.tabs(["📝 Introdução", "🔍 Metodologia", "📊 Resultado"])

    with tab1:
        st.header("INTRODUÇÃO")
        st.markdown("""
        ### Exercício 6:
        Calcule a integral de uma função $f(x) = (x-2)^2/(x+3)^3$ no intervalo $[0, 1.75]$ utilizando os valores tabelados abaixo:
        
        $x: 0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75$\n
        $f(x): 1.4815×10⁻¹, 8.9213×10⁻², 5.2478×10⁻², 2.9630×10⁻², 1.5625×10⁻², 8.2150×10⁻³, 4.0100×10⁻³, 2.1000×10⁻³$
        
        Compare os resultados obtidos pela **Regra dos Trapézios** e pela **Regra de Simpson**.
        
        ### Objetivo:
        Resolver numericamente a integral da função utilizando métodos de integração numérica (Trapézios e Simpson) e comparar os resultados. Apresentar os resultados graficamente e discutir as diferenças entre os métodos.
        """)

    with tab2:
        st.header("METODOLOGIA")
        st.markdown("""  
        #### 1. Regra dos Trapézios
        **Breve Explicação**: A Regra dos Trapézios aproxima a integral dividindo a área sob a curva em trapézios, somando suas áreas para estimar o valor total da integral.
        """)
        st.latex(r"""
        \int_a^b f(x) \, dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]
        """)
        st.markdown("""
        onde $h = (b-a)/n$ é o tamanho do intervalo, e $x_i$ são os pontos tabelados.
        
        #### 2. Regra de Simpson
        **Breve Explicação**: A Regra de Simpson usa polinômios quadráticos para aproximar a função em grupos de dois subintervalos, proporcionando maior precisão que a Regra dos Trapézios.
        """)
        st.latex(r"""
        \int_a^b f(x) \, dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1,3,\dots}^{n-1} f(x_i) + 2 \sum_{i=2,4,\dots}^{n-2} f(x_i) + f(x_n) \right]
        """)
        st.markdown("""
        onde $h = (b-a)/n$ é o tamanho do intervalo, e $x_i$ são os pontos tabelados. O primeiro somatório inclui os pontos com índices ímpares ($i=1,3,\dots,n-1$), e o segundo inclui os pontos com índices pares ($i=2,4,\dots,n-2$). Como o intervalo [0, 1.75] contém 8 pontos (7 subintervalos), aplicamos a Regra de Simpson até $x = 1.5$ (6 subintervalos) e usamos a Regra dos Trapézios para o último subintervalo [1.5, 1.75].
        
        ### Implementação
        - **Dados**: Utilizamos os pontos tabelados fornecidos.
        - **Cálculo**: Aplicamos as fórmulas acima para calcular as integrais.
        - **Gráfico**: Plotamos a função exata $f(x) = (x-2)^2/(x+3)^3$, os pontos tabelados e os trapézios para visualização.
        """)

    with tab3:
        st.header("RESULTADO")
        
        if st.button("Executar Exercício 6"):
            trapezios, simpson_soma = calcular_integrais()
            st.markdown("""
            - **Regra dos Trapézios**: {:.6f}
            - **Regra de Simpson (composta + trapézio)**: {:.6f}
            
            ### Gráfico
            """.format(trapezios, simpson_soma))
            
            fig = plot_integral(trapezios, simpson_soma)
            st.pyplot(fig)
            
            st.markdown("""
            ### Código dos Métodos
            Abaixo, o código Python usado para calcular as integrais pelos métodos dos Trapézios e de Simpson, exibido em colunas para melhor organização:
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Regra dos Trapézios**")
                st.code("""
# Regra dos Trapézios
trapezios = (h / 2) * (f[0] + 2 * np.sum(f[1:n]) + f[n])
                """, language="python")
                st.markdown("""
                **Explicação Detalhada**:
                - **Parâmetro $h$ **: Calculado como $h = (b-a)/n = (1.75-0)/7 = 0.25$, onde $n = 7$ é o número de subintervalos.
                - **Soma dos pontos intermediários**: A função `np.sum(f[1:n])` soma os valores de $f(x_i)$ para $i=1$ até $i=6$ (excluindo os extremos).
                - **Multiplicação por 2**: Os pontos intermediários são multiplicados por 2, conforme a fórmula.
                - **Extremos**: $f(x_0) = f(0)$ e $f(x_n) = f(1.75)$ são somados.
                - Fator $h/2$: O resultado é multiplicado por $0.25/2 = 0.125$ para obter a integral aproximada.
                """)
            
            with col2:
                st.markdown("**Regra de Simpson**")
                st.code("""
# Regra de Simpson composta + trapézio
n_simpson = 6
simpson = (h/3) * (f[0] + 4 * (f[1] + f[3] + f[5]) + 2 * (f[2] + f[4]) + f[6])
trapezio_aux = (h/2) * (f[6] + f[7])
simpson_soma = simpson + trapezio_aux
                """, language="python")
                st.markdown("""
                **Explicação Detalhada**:
                - **Simpson até $x=1.5$**: Usa 6 subintervalos ($n=6$). O fator $h/3 = 0.25/3 = 0.08333$ multiplica a soma:
                  - $f(x_0) = f(0)$ e $f(x_6) = f(1.5)$ com peso 1.
                  - Pontos ímpares $f(x_1), f(x_3), f(x_5)$ com peso 4.
                  - Pontos pares $f(x_2), f(x_4)$ com peso 2.
                - **Trapézio auxiliar**: Para o intervalo $[1.5, 1.75]$, calcula $h/2$ com $f(1.5) + f(1.75)$.
                - **Soma final**: Combina o resultado de Simpson com o trapézio auxiliar para cobrir todo o intervalo $[0, 1.75]$.
                """)
            
            st.markdown("""
            ### Discussão
            - **Precisão**: A Regra de Simpson geralmente é mais precisa que a Regra dos Trapézios, pois usa polinômios de segundo grau, enquanto os trapézios usam aproximações lineares. No entanto, como usamos Simpson composta apenas até $x = 1.5$ e um trapézio para o último intervalo, a diferença pode ser menos significativa.
            - **Erro**: A função $f(x) = (x-2)^2/(x+3)^3$ é suave no intervalo [0, 1.75], o que favorece ambos os métodos. A Regra de Simpson tem erro de ordem $O(h^4)$, enquanto a dos Trapézios tem erro de ordem $O(h^2)$.
            - **Comparação**: Os resultados são próximos, mas a Regra de Simpson tende a ser mais próxima do valor exato devido à sua maior ordem de precisão.
            
            ### Referências
            XAI. Grok. Disponível em: <https://x.ai/grok>.  
            Henrique123-Marques. Repositório do Projeto. Disponível em: <https://github.com/Henrique123-Marques/list3_NumericalCalculusUFABC>. \n
            FREITAS. Raphael de Oliveira. CORRÊA. Rejane Izabel Lima. VAZ. Patrícia Machado Sebajos. Cálculo Numérico. Editora SAGAH. 2019.
            """)

# Função para o Exercício 9
def exercicio_9():
    # Função da EDO
    def f(x, y):
        return -2 * x * y ** 2

    # Solução exata
    def y_exato(x):
        return 1 / (1 + x ** 2)

    # Parâmetros
    a, b = 0, 1
    h = 0.1
    n = int((b - a) / h)
    x = np.arange(a, b + h, h)

    # Função para calcular as soluções
    def calcular_solucoes():
        y_euler = np.zeros(n + 1)
        y_rk2 = np.zeros(n + 1)
        y_euler[0] = 1.0
        y_rk2[0] = 1.0

        for i in range(n):
            y_euler[i + 1] = y_euler[i] + h * f(x[i], y_euler[i])

        for i in range(n):
            k1 = f(x[i], y_rk2[i])
            k2 = f(x[i] + h, y_rk2[i] + h * k1)
            y_rk2[i + 1] = y_rk2[i] + h * k2
        
        y_ex = y_exato(x)
        return y_euler, y_rk2, y_ex

    # Função para criar o gráfico
    def plot_solucoes(y_euler, y_rk2, y_ex):
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        ax.plot(x, y_euler, 'g-o', label='Solução numérica (Euler)', markersize=5)
        ax.plot(x, y_rk2, 'b-o', label='Solução numérica (RK2)', markersize=5)
        ax.plot(x, y_ex, 'r--', label=r'Solução exata: $y = \frac{1}{1 + x^2}$')
        ax.scatter(x, y_euler, color='green', zorder=5)
        ax.scatter(x, y_rk2, color='blue', zorder=5)
        ax.set_xlabel('x')
        ax.set_ylabel('y(x)')
        #ax.set_title("Solução da EDO $y' = -2xy^2$, $y(0) = 1$, por Euler e RK2 ($h = 0.1$)")
        ax.legend()
        ax.grid(True)
        return fig

    # Interface do Streamlit
    st.title("Solução Numérica de EDO no Intervalo [0, 1]")

    # Abas com ícones
    tab1, tab2, tab3 = st.tabs(["📝 Introdução", "🔍 Metodologia", "📊 Resultado"])

    with tab1:
        st.header("INTRODUÇÃO")
        st.markdown("""
        ### Exercício 9:
        Compare graficamente as soluções obtidas pelos métodos de Euler e Runge-Kutta de ordem 2 (RK2) com a solução exata $y(x) = 1/(1 + x^2)$ para a equação diferencial ordinária (EDO) $y' = -2xy^2$, com condição inicial $y(0) = 1$, no intervalo $[0, 1]$. Comente as diferenças observadas.

        ### Objetivo:
        Resolver numericamente a EDO utilizando os métodos de Euler e RK2 com passo $h = 0.1$, comparar as soluções numéricas com a solução exata, apresentar os resultados graficamente e discutir as diferenças entre os métodos.
        """)

    with tab2:
        st.header("METODOLOGIA")
        st.markdown("""
        #### 1. Método de Euler
        **Breve Explicação**: O método de Euler é um método numérico de primeira ordem que aproxima a solução da EDO usando a tangente em cada ponto para prever o próximo valor.
        """)
        st.latex(r"""
        y_{i+1} = y_i + h \cdot f(x_i, y_i)
        """)
        st.markdown("""
        onde $h$ é o tamanho do passo, $f(x_i, y_i)$ é a derivada dada pela EDO ($f(x, y) = -2xy^2$), e $(x_i, y_i)$ são os pontos calculados.

        #### 2. Método de Runge-Kutta de Ordem 2 (RK2)
        **Breve Explicação**: O método RK2 é um método de segunda ordem que melhora a precisão do Euler ao usar dois cálculos de inclinação por passo, combinando-os para uma melhor aproximação.
        """)
        st.latex(r"""
        \begin{align*}
        k_1 &= f(x_i, y_i), \\
        k_2 &= f(x_i + h, y_i + h \cdot k_1), \\
        y_{i+1} &= y_i + h \cdot k_2
        \end{align*}
        """)
        st.markdown("""
        onde $k_1$ é a inclinação no início do intervalo, e $k_2$ é a inclinação no ponto final estimado, proporcionando uma aproximação mais precisa.

        ### Implementação
        - **Dados**: Intervalo $[0, 1]$, passo $h = 0.1$, condição inicial $y(0) = 1$.
        - **Cálculo**: Aplicamos os métodos de Euler e RK2 para calcular $y(x)$ em 11 pontos ($x = 0, 0.1, \ldots, 1.0$).
        - **Gráfico**: Plotamos as soluções numéricas (Euler e RK2) e a solução exata $y(x) = 1/(1 + x^2)$ para comparação visual.
        """)

    with tab3:
        st.header("RESULTADO")
        st.markdown("""
        ###
        Clique no botão abaixo para executar o cálculo e visualizar os resultados e o gráfico.
        """)
        
        if st.button("Calcular e Mostrar Gráfico"):
            y_euler, y_rk2, y_ex = calcular_solucoes()
            
            # Tabela de resultados
            st.markdown("**Tabela de Resultados**")
            st.markdown("""
            | x   | y_Euler | y_RK2 | y_Exata | Erro_Euler | Erro_RK2 |
            |-----|---------|-------|---------|------------|----------|
            """)
            for xi, ye, yr, yex in zip(x, y_euler, y_rk2, y_ex):
                st.markdown(f"| {xi:.1f} | {ye:.6f} | {yr:.6f} | {yex:.6f} | {abs(ye - yex):.6f} | {abs(yr - yex):.6f} |")
            
            # Gráfico
            st.markdown("### Gráfico")
            fig = plot_solucoes(y_euler, y_rk2, y_ex)
            st.pyplot(fig)
            
            # Código dos métodos
            st.markdown("""
            ### Código dos Métodos
            Abaixo, o código Python usado para calcular as soluções pelos métodos de Euler e RK2, exibido em colunas para melhor organização:
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Método de Euler**")
                st.code("""
# Método de Euler
y_euler = np.zeros(n + 1)
y_euler[0] = 1.0
for i in range(n):
    y_euler[i + 1] = y_euler[i] + h * f(x[i], y_euler[i])
                """, language="python")
                st.markdown("""
                **Explicação Detalhada**:
                - **Inicialização**: Define $y_0 = 1$ para $x_0 = 0$.
                - **Iteração**: Para cada $i$ de 0 a $n-1$ ($n=10$):
                  - Calcula $f(x_i, y_i) = -2 x_i y_i^2$.
                  - Atualiza $y_{i+1} = y_i + h \cdot f(x_i, y_i)$, onde $h = 0.1$.
                - **Exemplo para $i=0$**: $x_0 = 0$, $y_0 = 1$, $f(0, 1) = -2 \cdot 0 \cdot 1^2 = 0$, então $y_1 = 1 + 0.1 \cdot 0 = 1$.
                - Repete para todos os 10 passos, gerando 11 pontos.
                """)
            
            with col2:
                st.markdown("**Método de Runge-Kutta de Ordem 2 (RK2)**")
                st.code("""
# Método de Runge-Kutta de ordem 2 (RK2)
y_rk2 = np.zeros(n + 1)
y_rk2[0] = 1.0
for i in range(n):
    k1 = f(x[i], y_rk2[i])
    k2 = f(x[i] + h, y_rk2[i] + h * k1)
    y_rk2[i + 1] = y_rk2[i] + h * k2
                """, language="python")
                st.markdown("""
                **Explicação Detalhada**:
                - **Inicialização**: Define $y_0 = 1$ para $x_0 = 0$.
                - **Iteração**: Para cada $i$ de 0 a $n-1$ ($n=10$):
                  - Calcula $k_1 = f(x_i, y_i) = -2 x_i y_i^2$.
                  - Calcula $k_2 = f(x_i + h, y_i + h \cdot k_1)$, avaliando a EDO no ponto estimado $(x_i + 0.1, y_i + 0.1 \cdot k_1)$.
                  - Atualiza $y_{i+1} = y_i + h \cdot k_2$, onde $h = 0.1$.
                - **Exemplo para $i=0$**: $x_0 = 0$, $y_0 = 1$, $k_1 = f(0, 1) = 0$, $k_2 = f(0.1, 1 + 0.1 \cdot 0) = f(0.1, 1) = -2 \cdot 0.1 \cdot 1^2 = -0.2$, então $y_1 = 1 + 0.1 \cdot (-0.2) = 0.98$.
                - Repete para todos os 10 passos, gerando 11 pontos.
                """)
            
            st.markdown("""
            ### Discussão
            - **Precisão**: O método RK2 é mais preciso que o Euler, pois usa duas inclinações por passo, resultando em erro de ordem $O(h^2)$ contra $O(h)$ do Euler. A tabela mostra que os erros do RK2 são consistentemente menores.
            - **Comportamento**: No gráfico, a solução do RK2 segue a solução exata mais de perto, enquanto o Euler diverge ligeiramente, especialmente em $x$ maiores.
            - **Aplicação**: Para EDOs com soluções suaves, como $y(x) = 1/(1 + x^2)$, o RK2 é preferível devido à sua maior precisão com o mesmo passo $h = 0.1$.

            ### Referências
            XAI. Grok. Disponível em: <https://x.ai/grok>.  
            Henrique123-Marques. Repositório do Projeto. Disponível em: <https://github.com/Henrique123-Marques/list3_NumericalCalculusUFABC>.\n
            BURDEN. Richard L. FAIRES. J. Douglas. Numerical Analysis. Ninth Edition.
            """)

# Main app logic
def main():
    st.sidebar.title("Cálculo Numérico Q1 2025 - Lista 3")
    page = st.sidebar.selectbox("Selecione o Exercício", ["Exercício 6", "Exercício 9"])

    if page == "Exercício 6":
        exercicio_6()
    elif page == "Exercício 9":
        exercicio_9()

if __name__ == "__main__":
    main()