import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise de Veículos", layout="wide")

st.title("🚗 Análise de Veículos")

# carregar dados
df = pd.read_csv("vehicles_us.csv")

st.subheader("Prévia dos dados")
st.dataframe(df.head())

# filtro simples
if "type" in df.columns:
    tipos = df["type"].dropna().unique()
    tipo_selecionado = st.selectbox("Filtrar tipo de veículo", tipos)

    df_filtrado = df[df["type"] == tipo_selecionado]
else:
    df_filtrado = df

# gráfico 1 - preço
st.subheader("Distribuição de preços")
fig1 = px.histogram(df_filtrado, x="price", nbins=50)
st.plotly_chart(fig1)

# gráfico 2 - preço por ano
if "model_year" in df.columns:
    st.subheader("Preço por ano do modelo")
    fig2 = px.scatter(df_filtrado, x="model_year", y="price", color="condition")
    st.plotly_chart(fig2)

# gráfico 3 - odômetro vs preço
if "odometer" in df.columns:
    st.subheader("Quilometragem vs Preço")
    fig3 = px.scatter(df_filtrado, x="odometer", y="price", color="type")
    st.plotly_chart(fig3)
    
