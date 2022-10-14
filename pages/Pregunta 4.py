import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 4')
st.write("Dada la señal signal.npy aplique los filtros Median y Wiener para obtener el siguiente gráfico. Investigue sobre el módulos scipy.signal.")

imagen= Image.open('Pregu4.png')
st.image(imagen, caption='Imagen Cuarta problematica')
st.write("##")


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
import numpy as np
from matplotlib import pyplot as pt
from scipy import signal

#Se crea un arreglo con los 100 datos de la señal en la variable creada a continuación
señal= np.load('signal.npy')

#Genera el vector de la señal sin filtros, el cual se usara en el eje x.
t=np.linspace(0,len(señal),100)
#Encotramos la media de los datos de los vecinos.
T_Media=signal.medfilt(señal,3)
#Se filtra la señal con el filtro de wiener.
T_wiener = signal.wiener(señal)

#Se crea el gráfico bajo el nombre filtrar señales.
pt.title("Filtrar señales")
#Se genera la linea de la señal normal.
pt.plot(t,señal,label="Señal Original")
#Se genera la linea de la señal con el filtro de Media.
pt.plot(t,T_Media,label="Filtro Media")
#Se genera la linea de la señal con el filtro de Wiener.
pt.plot(t,T_wiener,label="Filtro Wiener")
#Se nombra al eje x con tiempo
pt.xlabel("Tiempo(s)")
#Se nombra al ehe y con señal
pt.ylabel("Señal")
pt.legend()
pt.show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('Preg4.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
