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
#Se genera un arreglo con la tendencia 
t = np.linspace(0,5,100)
#Se genera un arreglo de numeros aleatorios, de largo 100
x=t +np.random.normal(size=100)
#Se remueve la tendencia lienal del arreglo anterior 
y=signal.detrend(x,type='linear')

#Se genera el grafico con la señal con y sin tendencia.
pt.figure()
pt.plot(t,x,'tab:blue',label='Sin tendencia')
pt.plot(t,y,'tab:orange',label='Tendencia')
pt.legend(prop={'size':10}, loc='upper left')
pt.show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('Preg5.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
