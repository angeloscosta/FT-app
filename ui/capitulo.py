import streamlit as st

# Interface genérica dos capítulos
def cabecalho(title, description):
    """
    Renderiza um capítulo com título, descrição e seções.

    Args:
        title (str): Título do capítulo.
        description (str): Descrição do capítulo.
        sections (list): Lista de seções, cada uma contendo título e conteúdo.
    """
    st.title(title)
    st.write(description)

def seccao(subtitulo, teoria_fn, exercicio_fn, resolver_fn):
    st.subheader(subtitulo)
    tabs = st.tabs(["Teoria", "Exercício", "Resolver"])
    with tabs[0]:
        teoria_fn(tabs[0])
    with tabs[1]:
        exercicio_fn(tabs[1])
    with tabs[2]:
        resolver_fn(tabs[2])