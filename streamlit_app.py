import streamlit as st

st.title("Biblioteca de Fenômenos de Transporte")
st.write(
    "Portfólio da unidade curricular (UC) **Fenômenos de Transporte** do curso Bacharelado Interdisciplinar em Ciência e Tecnologia da **UNIFESP** campus São José dos Campos."
    " Ementa disponível em [Ementário](https://unifesp.br/campus/sjc/catalogo-de-disciplinas/ementario-ucs/)."
)
st.write(
    "Este portfólio busca resumir os conceitos aprendidos em aula e aplica-los para resolver problemas simples, auxiliando futuros alunos a conferir seus resultados."
)
st.write(
    "Feito por **Ângelo Soares Costa**, aluno desta UC em 2025-1, usando o conteúdo da apostila da **Profa. Dra. Marina Oliveira de Souza Dias**."
)

st.set_page_config(page_title="Biblioteca de Fenômenos de Transporte", layout="wide")

# Sumário com todos os capítulos
st.title("Sumário")
tab1, tab2 = st.tabs(["Introdução", "Estática dos Fluidos"])

with tab1:
    st.header("1. Introdução")
    with st.expander("1.1 Conceitos e Definições"):
        st.expander("1.1.1 Propriedades em um Ponto")
with tab2:
    st.header("2. Estática dos Fluidos")
    with st.expander("2. Estática dos Fluidos"):
        st.expander ("2.1 Equação Geral da Estática")

# Adicione os demais capítulos seguindo o mesmo padrão...