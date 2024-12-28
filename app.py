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
La alimentación juega un papel clave en la prevención y manejo de diversas enfermedades crónicas, como la diabetes, la hipertensión y las enfermedades cardiovasculares. Este trabajo analiza un conjunto de datos que recopila información sobre los hábitos alimenticios y características físicas de personas que padecen estas condiciones. A través de distintas hipótesis, se busca explorar cómo factores como el nivel de actividad física, las preferencias dietéticas y el consumo de nutrientes influyen en la aparición y progresión de estas enfermedades.
""")

# Sección 2: Datos iniciales
st.header("Problematica")
st.write(""" 
La mala alimentación es un problema que afecta a la sociedad en general. 
Puede llevar a diversas enfermedades crónicas como la obesidad, diabetes, enfermedades cardiovasculares y ciertos tipos de cáncer. 
Además, afecta el rendimiento académico y laboral, y puede tener un impacto negativo en la salud mental.
""")
st.image("imagen1.jpg", caption="" )



st.header("La Vida Moderna")
st.write("""
Hoy en día, los niveles de actividad física de las personas son considerablemente bajos. 
El estilo de vida moderno, caracterizado por largas horas de trabajo sedentario y el uso excesivo de dispositivos electrónicos, 
ha llevado a un aumento del sedentarismo. Esta falta de actividad física contribuye a diversos problemas de salud, 
incluyendo la obesidad, enfermedades cardiovasculares y una disminución en el bienestar general.
""")
st.image("imagen2.webp")

st.header("Actividad de los pacientes")

st.image("grafico1.png", caption="Mi Gráfico PN" )

st.header("Enfermedades relacionadas al sedentarismo")


st.image("grafico2.png", caption="Mi Gráfico PNG" )

st.header("Diferencia Calórica y Problemas de Salud")
st.write("""
La diferencia calórica en la dieta de los pacientes puede tener un impacto significativo en su salud. 
Un exceso de calorías puede llevar a un aumento de peso y obesidad, lo que a su vez incrementa el riesgo de desarrollar enfermedades crónicas 
como la diabetes tipo 2, enfermedades cardiovasculares y ciertos tipos de cáncer. Por otro lado, una ingesta calórica insuficiente puede 
resultar en desnutrición, pérdida de masa muscular y un sistema inmunológico debilitado. Mantener un equilibrio calórico adecuado es esencial 
para la salud y el bienestar general.
""")
st.image("grafico5.png", caption="Mi Gráfico PNG" )
st.image("grafico6.png", caption="Mi Gráfico PNG" )

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

