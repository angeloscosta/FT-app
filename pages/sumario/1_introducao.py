import streamlit as st

from ui.capitulo import cabecalho, seccao

cabecalho(
    title="1. Introdução",
    description="Este capítulo fornece uma visão geral dos conceitos fundamentais da mecânica dos fluidos..."
)

def seccao_1_1():
    def teoria(tab):
        tab.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    def exemplo(tab):
        tab.write("Exemplo de cálculo de exercício ...")

    def resolucao(tab):
        tab.subheader("Gráfico da Resolução")
        # Aqui você pode adicionar lógica para coletar dados e plotar gráficos
        tab.write("Gráfico de exemplo...")

    seccao(
        subtitulo="1.1 Propriedades dos Fluidos",
        teoria_fn=teoria,
        exercicio_fn=exemplo,
        resolver_fn=resolucao
    )
    
seccao_1_1()

# Subseção (pode linkar para outra página)
# st.page_link("pages/1.1.1_Propriedades_em_um_ponto.py", label="▶️ Detalhes sobre Propriedades")