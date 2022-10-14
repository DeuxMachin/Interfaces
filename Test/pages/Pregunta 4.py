import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 4')
st.write("Dada la señal signal.npy aplique los filtros Median y Wiener para obtener el siguiente gráfico. Investigue sobre el módulos scipy.signal.")

imagen= Image.open('test/Pregu4.png')
st.image(imagen, caption='Imagen Cuarta problematica')
st.write("##")


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
import numpy as np
from matplotlib import pyplot as pt
from scipy import signal


señal= np.load('signal.npy')

t=np.linspace(0,len(señal),100)

#Encotramos la media
T_Media=signal.medfilt(señal,25)
T_wiener = signal.wiener(señal)

pt.title("Filtrar señales")
pt.plot(t,señal,label="Señal Original")
pt.plot(T_Media,label="Filtro Media")
pt.plot(t,T_wiener,label="Filtro Wiener")
pt.xlabel("Tiempo(s)")
pt.ylabel("Señal")
pt.legend()
pt.show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('test/Preg4.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
