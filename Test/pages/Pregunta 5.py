import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 5')
st.write("Separe la tendencia de la señal. Obtenga un gráfico similar. Complete el código. ")

imagen= Image.open('Pregu5.png')
st.image(imagen, caption='Imagenes Quinta problematica')
st.write("##")


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
import numpy as np
from matplotlib import pyplot as pt
from scipy import signal

tendencia = np.linspace(0,10,100)
x=tendencia +np.random.normal(size=100)
y=signal.detrend(x,type='linear')
pt.figure()
pt.plot(tendencia,x,'tab:blue',label='Sin tendencia')
pt.plot(tendencia,y,'tab:red',label='Tendencia')
pt.legend(prop={'size':10}, loc='upper left')
pt.show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('Preg5.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
