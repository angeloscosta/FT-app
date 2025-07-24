import streamlit as st

# Sobre
inicio = st.Page(
    "pages/bem-vindo.py",
    title="Bem-vindo"
)

# Sumário
introducao = st.Page(
    "pages/sumario/1_introducao.py",
    title="1. Introdução"
)
estatica_dos_fluidos = st.Page(
    "pages/sumario/2_estatica_dos_fluidos.py",
    title="2. Estática dos Fluidos"
)