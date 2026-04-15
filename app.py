import streamlit as st
import pandas as pd

st.title("Análise de Veículos")

df = pd.DataFrame({
    "carro": ["Gol", "Civic", "Uno"],
    "ano": [2010, 2018, 2005],
    "preço": [20000, 60000, 12000]
})

st.write(df)