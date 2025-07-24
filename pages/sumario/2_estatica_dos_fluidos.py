import streamlit as st
import numpy as np
import pandas as pd

# Título do capítulo
st.title("2. Estática dos Fluidos")

# Descrição do capítulo
st.write("Este capítulo aborda os princípios da estática dos fluidos...")

# Seção 2.1: Equação Geral da Estática
st.subheader("2.1 Equação Geral da Estática")

tab1, tab2, tab3 = st.tabs(["Teoria", "Exemplo", "Resolver"])

# Tab 1
tab1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

# Tab 2
tab2.write("Exemplo de cálculo da pressão hidrostática em um fluido incompressível...")

# Tab 3
tab3.subheader("Gráfico do Matplotlib")

def coletar_dados(tab):
    rho = tab.number_input("Densidade do fluido ($\\mathrm{kg/m^3}$)", 0, None, 1000)
    g = tab.number_input("Gravidade ($\\mathrm{m/s^2}$)", 0.0, None, 9.8)
    h = tab.number_input("Profundidade ($\\mathrm{m}$)", 0.0, None, 1.0)
    return rho, g, h

rho, g, h = coletar_dados(tab3)
def calcular_pressao(rho, g, h):
    """Calcula a pressão hidrostática."""
    pressao = rho * g * h
    return pressao
 
pressao = calcular_pressao(rho, g, h)

# Gráfico com Streamlit line_chart
h_range = np.linspace(0, 10, 100)
p_range = rho * g * h_range
df = pd.DataFrame({"Profundidade (m)": h_range, "Pressão (Pa)": p_range})
tab3.latex(f"P = \\rho g h = {pressao:.2f} \\, \\text{{Pa}}")
tab3.line_chart(df.set_index("Profundidade (m)"))
