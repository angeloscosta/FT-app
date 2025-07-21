import streamlit as st

st.title("1.1 Conceitos e Definições")
st.markdown("""
    ### Propriedades em um Ponto de Fluido
    - **Massa específica ($\\rho$)**: 
        $$ \\rho = \\lim_{\\Delta V \\to 0} \\frac{\\Delta m}{\\Delta V} $$
    - **Tensão num ponto**: Tensor de tensões de Cauchy.
""")

# Subseção (pode linkar para outra página)
st.page_link("pages/1.1.1_Propriedades_em_um_ponto.py", label="▶️ Detalhes sobre Propriedades")