import streamlit as st
import numpy as np
import pandas as pd

# Local
import metodos_matematicos as resolver
import ui.ui_capitulo as ui


ui.cabecalho(
    title="2. Estática dos Fluidos",
    description="Este capítulo aborda os princípios da estática dos fluidos...")

def teoria(tab):
    tab.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

def exemplo(tab):
    tab.write("Exemplo de cálculo de exercício ...")

def resolucao(tab):
    tab.subheader("Gráfico da Resolução")
    rho, g, h = resolver.coletar_dados_pressao(tab)
    pressao = resolver.calcular_pressao(rho, g, h)
    tab.latex(f"P = \\rho g h = {pressao:.2f} \\, \\text{{Pa}}")
    x_label = "Profundidade (m)"
    x_range = np.linspace(0, 10, 100)
    y_label = "Pressão (Pa)"
    y_range = rho * g * x_range
    resolver.plotar_line_chart(tab, x_range, y_range, x_label, y_label)

ui.corpo(
    subtitulo="2.1 Equação Geral da Estática",
    teoria_fn=teoria,
    exercicio_fn=exemplo,
    resolver_fn=resolucao
)
