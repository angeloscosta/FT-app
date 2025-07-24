import streamlit as st
import lista_de_paginas as paginas

st.set_page_config(page_title="Portfolio de Fenômenos de Transporte", layout="wide")

def menu():
    # lista da items do menu
    lista = {
        "Sobre": [
            paginas.inicio
        ],
        "Sumário": [
            paginas.introducao,
            paginas.estatica_dos_fluidos,
        ],
    }

    # Criação do menu de navegação
    navegacao = st.navigation(lista, position="top", expanded=False)
    return navegacao

menu().run()


# Adicione os demais capítulos seguindo o mesmo padrão...