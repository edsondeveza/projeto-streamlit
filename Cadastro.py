import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {data_nasc}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False
        

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="💾"
)


st.title("Cadastro de clientes")
st.divider()


nome = st.text_input("Digite o nome do cliente ",
                     key="nome_cliente", 
                     max_chars=30)


dt_nasc = st.date_input("Data nascimento: ",
                     key="dt_nasc",
                     format="DD/MM/YYYY")


tipo = st.selectbox("Tipo do cliente",
                    ["Pessoa Física", "Pessoa Jurídica", "MEI"],
                    key="tipo_cliente")


btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastro com sucesso!",
                   icon="👍🏼")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="👎🏼")
        



