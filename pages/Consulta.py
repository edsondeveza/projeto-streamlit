import streamlit as st
import pandas as pd

df = pd.read_csv("clientes.csv")

st.title("Clientes cadastrados")
st.divider()

st.dataframe(df)