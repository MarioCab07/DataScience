import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Configuración básica
st.set_page_config(page_title="Análisis de Datos", layout="wide")

# Título de la app
st.title("📊 Narrativa de Datos")

# Sección 1: Introducción
st.header("1. Introducción")
st.write("""
En esta presentación exploraremos el análisis de datos relacionados con [tema del análisis].
Nuestro objetivo es extraer insights clave y comunicar los resultados de manera efectiva.
""")

# Sección 2: Datos iniciales
st.header("2. Datos y Exploración")
uploaded_file = st.file_uploader("Carga tu dataset en formato CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data.head(10))  # Muestra los primeros 10 datos

# Sección 3: Visualizaciones clave
st.header("3. Visualizaciones")
if uploaded_file:
    st.write("Explora las distribuciones:")
    st.bar_chart(data['columna'])  # Reemplaza 'columna' con una existente en tu dataset

    st.write("Relación entre variables:")
    fig, ax = plt.subplots()
    ax.scatter(data['columna_x'], data['columna_y'])  # Reemplaza con tus columnas
    st.pyplot(fig)

# Sección 4: Conclusiones
st.header("4. Conclusiones")
st.write("""
En este análisis hemos destacado los puntos clave relacionados con:
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]
""")
