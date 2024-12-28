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
st.header("Problematica")
st.write(""" 
La mala alimentación es un problema que afecta a la sociedad en general. 
Puede llevar a diversas enfermedades crónicas como la obesidad, diabetes, enfermedades cardiovasculares y ciertos tipos de cáncer. 
Además, afecta el rendimiento académico y laboral, y puede tener un impacto negativo en la salud mental.
""")
st.image("imagen1.jpg", caption="Mi Gráfico PNG" )



st.header("La Vida Moderna")
st.write("""
Hoy en día, los niveles de actividad física de las personas son considerablemente bajos. 
El estilo de vida moderno, caracterizado por largas horas de trabajo sedentario y el uso excesivo de dispositivos electrónicos, 
ha llevado a un aumento del sedentarismo. Esta falta de actividad física contribuye a diversos problemas de salud, 
incluyendo la obesidad, enfermedades cardiovasculares y una disminución en el bienestar general.
""")
st.image("imagen2.webp")

st.image("grafico1.png", caption="Mi Gráfico PNG" )
st.image("grafico2.png", caption="Mi Gráfico PNG" )

st.image("grafico3.png", caption="Mi Gráfico PNG" )
st.image("grafico4.png", caption="Mi Gráfico PNG" )
st.image("grafico5.png", caption="Mi Gráfico PNG" )
st.image("grafico6.png", caption="Mi Gráfico PNG" )
st.image("grafico7.png", caption="Mi Gráfico PNG" )
st.image("grafico8.png", caption="Mi Gráfico PNG" )
st.image("grafico10.png", caption="Mi Gráfico PNG" )
st.image("grafico11.png", caption="Mi Gráfico PNG" )
st.image("grafico12.png", caption="Mi Gráfico PNG" )
st.image("grafico13.png", caption="Mi Gráfico PNG" )
st.image("grafico14.png", caption="Mi Gráfico PNG" )
st.image("grafico15.png", caption="Mi Gráfico PNG" )
st.image("grafico16.png", caption="Mi Gráfico PNG" )
st.image("grafico17.png", caption="Mi Gráfico PNG" )
st.image("grafico18.png", caption="Mi Gráfico PNG" )
st.image("grafico19.png", caption="Mi Gráfico PNG" )
st.image("grafico20.png", caption="Mi Gráfico PNG" )
st.image("grafico21.png", caption="Mi Gráfico PNG" )

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
