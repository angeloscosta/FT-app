import streamlit as st
import numpy as np
import pandas as pd

# Geral
def plotar_line_chart(tab, x_data, y_data, x_label, y_label):
    """
    Plota um gráfico de linha genérico no Streamlit.

    Args:
        tab: Aba do Streamlit onde o gráfico será exibido.
        x_data: Dados do eixo x (array-like).
        y_data: Dados do eixo y (array-like).
        x_label: Rótulo do eixo x (str).
        y_label: Rótulo do eixo y (str).
    """
    df = pd.DataFrame({x_label: x_data, y_label: y_data})
    tab.line_chart(df.set_index(x_label))

# 1. Introdução

# 2. Estática dos Fluidos
def coletar_dados_pressao(tab):
    rho = tab.number_input("Densidade do fluido ($\\mathrm{kg/m^3}$)", 0, None, 1000)
    g = tab.number_input("Gravidade ($\\mathrm{m/s^2}$)", 0.0, None, 9.8)
    h = tab.number_input("Profundidade ($\\mathrm{m}$)", 0.0, None, 1.0)
    return rho, g, h
def calcular_pressao(rho, g, h):
    """Calcula a pressão hidrostática."""
    pressao = rho * g * h
    return pressao