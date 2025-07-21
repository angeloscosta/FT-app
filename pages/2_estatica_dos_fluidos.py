import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("2. Estática dos Fluidos")
st.markdown("### 2.1 Equação Geral da Estática")

# Inputs interativos
rho = st.slider("Densidade do fluido (kg/m³)", 500, 1500, 1000)
g = 9.81  # aceleração da gravidade

# Cálculo da pressão hidrostática
h = st.number_input("Profundidade (m)", 0.0, 10.0, 1.0)
pressao = rho * g * h

st.latex(f"P = \\rho g h = {pressao:.2f} \\, \\text{{Pa}}")

# Gráfico
h_range = np.linspace(0, 10, 100)
p_range = rho * g * h_range

fig, ax = plt.subplots()
ax.plot(h_range, p_range)
ax.set_xlabel("Profundidade (m)")
ax.set_ylabel("Pressão (Pa)")
st.pyplot(fig)