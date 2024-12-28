import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Configuración básica
st.set_page_config(page_title="Análisis de Datos", layout="wide")

# Título de la app
st.title("📊 Salud Alimenticia")

# Sección 1: Introducción
st.header("Introducción")
st.write("""
La alimentación juega un papel clave en la prevención y manejo de diversas enfermedades crónicas, como la diabetes, la hipertensión y las enfermedades cardiovasculares. Este trabajo analiza un conjunto de datos que recopila información sobre los hábitos alimenticios y características físicas de personas que padecen estas condiciones. A través de distintas hipótesis, se busca explorar cómo factores como el nivel de actividad física, las preferencias dietéticas y el consumo de nutrientes influyen en la aparición y progresión de estas enfermedades.
""")

# Sección 2: Datos iniciales
st.header("Problemática")
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

st.image("grafico1.png", caption=" " )

st.header("Enfermedades relacionadas al sedentarismo")


st.image("grafico2.png", caption=" " )

st.header("Diferencia Calórica y Problemas de Salud")
st.write("""
La diferencia calórica en la dieta de los pacientes puede tener un impacto significativo en su salud. 
Un exceso de calorías puede llevar a un aumento de peso y obesidad, lo que a su vez incrementa el riesgo de desarrollar enfermedades crónicas 
como la diabetes tipo 2, enfermedades cardiovasculares y ciertos tipos de cáncer. Por otro lado, una ingesta calórica insuficiente puede 
resultar en desnutrición, pérdida de masa muscular y un sistema inmunológico debilitado. Mantener un equilibrio calórico adecuado es esencial 
para la salud y el bienestar general.
""")
st.image("grafico5.png", caption=" " )
st.image("grafico6.png", caption=" " )

st.header("Restricción proteica y daño renal crónico")
st.write("""
El consumo excesivo de proteínas puede sobrecargar los riñones, ya que estos órganos son responsables de filtrar los desechos producidos por el metabolismo de las proteínas. A largo plazo, esta sobrecarga puede llevar a un deterioro de la función renal y eventualmente a enfermedades renales crónicas. Por otro lado, una ingesta insuficiente de proteínas puede resultar en desnutrición y pérdida de masa muscular, lo que también puede afectar negativamente la salud renal. Es crucial mantener un equilibrio adecuado en el consumo de proteínas para preservar la salud de los riñones.
""")

st.image("grafico8.png", caption=" " )

st.write("""
Problemas Renales""")
st.image("grafico9.png", caption=" " )


st.header("El peligro de la azucar")
st.write("""
El consumo excesivo de azúcar está asociado con una serie de problemas de salud. Entre ellos se incluyen la obesidad, la diabetes tipo 2, enfermedades cardiovasculares y caries dentales. El azúcar en exceso puede llevar a un aumento de peso significativo, lo que incrementa el riesgo de desarrollar enfermedades crónicas. Además, el consumo elevado de azúcar puede causar picos de glucosa en sangre, lo que a largo plazo puede resultar en resistencia a la insulina y diabetes. También se ha relacionado con un mayor riesgo de enfermedades del corazón debido a su impacto negativo en los niveles de colesterol y presión arterial.
""")
st.image("imagen3.webp", caption="Azucar")


st.image("grafico12.png", caption=" " )

st.header("Consumo dependiendo de dieta")
st.image("grafico15.png", caption=" " )


st.header("Un buen aliado como la Fibra")
st.write("""
El consumo de fibra tiene múltiples beneficios para la salud. Ayuda a mantener un sistema digestivo saludable al prevenir el estreñimiento y promover la regularidad intestinal. Además, la fibra puede ayudar a controlar los niveles de azúcar en sangre, lo que es especialmente beneficioso para personas con diabetes. También contribuye a reducir los niveles de colesterol, lo que puede disminuir el riesgo de enfermedades cardiovasculares. Por último, la fibra puede ayudar en el control del peso al proporcionar una sensación de saciedad, lo que puede reducir la ingesta total de calorías.
""")
st.image("imagen4.webp", caption=" " )
st.header("El peso y la fibra")
st.image("grafico17.png", caption=" " )
st.image("grafico18.png", caption=" " )
st.image("grafico19.png", caption=" " )


