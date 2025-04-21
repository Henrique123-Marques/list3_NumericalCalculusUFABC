import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Cálculo de Integral Numérica", layout="wide")

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
    
    fig, ax = plt.subplots(figsize=(6, 3))  # Reduzido de (10, 6) para (8, 5)
    
    # Definir fundo adaptativo (mesmo fundo do Streamlit)
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
    #ax.set_title(f'Integral de f(x) de 0 a 1.75\nTrapézios: {trapezios:.6f}, Simpson: {simpson_soma:.6f}')
    ax.legend()
    ax.grid(True)
    return fig

# Interface do Streamlit
st.title("Cálculo Numérico Q1 2025 - Lista 3")

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
    
    ### Objetivo
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
            - **Extremos**: $f(x_0) = f(0) e f(x_n) = f(1.75)$ são somados.
            - Fator $h/2$: O resultado é multiplicado por $0.25/2 = 0.125$ para obter a integral aproximada.
            """)
        
        with col2:
            st.markdown("**Regra de Simpson**")
            st.code("""
# Regra  Regra de Simpson composta + trapézio
n_simpson = 6
simpson = (h/3) * (f[0] + 4 * (f[1] + f[3] + f[5]) + 2 * (f[2] + f[4]) + f[6])
trapezio_aux = (h/2) * (f[6] + f[7])
simpson_soma = simpson + trapezio_aux
            """, language="python")
            st.markdown("""
            **Explicação Detalhada**:
            - **Simpson até $x=1.5$: Usa 6 subintervalos $n=6$. O fator $h/3 = 0.25/3 = 0.08333$ multiplica a soma:
              - $f(x_0) = f(0) e f(x_6) = f(1.5)$ com peso 1.
              - Pontos ímpares $f(x_1), f(x_3), f(x_5)$ com peso 4.
              - Pontos pares $(f(x_2), f(x_4)$ com peso 2.
            - **Trapézio auxiliar**: Para o intervalo $[1.5, 1.75]$, calcula $h/2$ com $f(1.5) + f(1.75)$.
            - **Soma final**: Combina o resultado de Simpson com o trapézio auxiliar para cobrir todo o intervalo $[0, 1.75]$s.
            """)
        
        st.markdown("""
        ### Discussão
        - **Precisão**: A Regra de Simpson geralmente é mais precisa que a Regra dos Trapézios, pois usa polinômios de segundo grau, enquanto os trapézios usam aproximações lineares. No entanto, como usamos Simpson composta apenas até $x = 1.5$ e um trapézio para o último intervalo, a diferença pode ser menos significativa.
        - **Erro**: A função $f(x) = (x-2)^2/(x+3)^3$ é suave no intervalo [0, 1.75], o que favorece ambos os métodos. A Regra de Simpson tem erro de ordem $O(h^4)$, enquanto a dos Trapézios tem erro de ordem $O(h^2)$.
        - **Comparação**: Os resultados são próximos, mas a Regra de Simpson tende a ser mais próxima do valor exato devido à sua maior ordem de precisão.
        
        ### Referências
        XAI. Grok. Disponível em: <https://x.ai/grok>. Acesso em: 21 abr. 2025.  
        Henrique123-Marques. Repositório do Projeto. Disponível em: <https://github.com/Henrique123-Marques/list3_NumericalCalculusUFABC>. Acesso em: 21 abr. 2025.
        """)