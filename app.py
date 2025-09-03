import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("🚗 Análisis de Anuncios de Vehículos")

# Leer dataset (debe estar en la misma carpeta que app.py)
car_data = pd.read_csv("vehicles_us.csv")

# Botón para histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el kilometraje de los vehículos")
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del Kilometraje",
        labels={"odometer": "Kilometraje (millas)", "count": "Cantidad de vehículos"}
    )
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre Kilometraje y Precio")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.5,
        title="Relación entre Kilometraje y Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio en USD"}
    )
    st.plotly_chart(fig, use_container_width=True)

