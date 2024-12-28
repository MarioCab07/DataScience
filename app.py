import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Configuración básica
st.set_page_config(page_title="Análisis de Datos", layout="wide")

# Título de la app
st.title("📊 Salud Alimenticia")

# Sección 1: Introducción
st.header("1. Introducción")
st.write("""
En esta presentación exploraremos el análisis de datos relacionados con [tema del análisis].
Nuestro objetivo es extraer insights clave y comunicar los resultados de manera efectiva.
""")

# Sección 2: Datos iniciales
st.header("2. Datos y Exploración")
st.image("grafico1.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico2.png", caption="Mi Gráfico PNG", use_column_width=True)

st.image("grafico3.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico4.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico5.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico6.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico7.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico8.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico10.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico11.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico12.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico13.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico14.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico15.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico16.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico17.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico18.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico19.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico20.png", caption="Mi Gráfico PNG", use_column_width=True)
st.image("grafico21.png", caption="Mi Gráfico PNG", use_column_width=True)

 # Muestra los primeros 10 datos

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
