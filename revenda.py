import streamlit as st
import pandas as pd
import plotly.express as px

st.header("📊 Análise de Veículos")

df = pd.read_csv("vehicles_us.csv")

# botão 1 - histograma
if st.button("Mostrar histograma de quilometragem"):
    st.write("Histograma da quilometragem")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# botão 2 - gráfico de dispersão
if st.button("Mostrar gráfico de dispersão"):
    st.write("Preço vs Quilometragem")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)