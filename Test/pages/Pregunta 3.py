import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 3')
st.write("Aplique Least Square Polymonial mediante poly1d() y polyfit(). Utilice f1.npy y f2.npy para obtener el siguiente gráfico. Utilice x = np.arange(start=1,stop=50,step=1).")

imagen= Image.open('test/Pregu3.png')
st.image(imagen, caption='Imagen Tercera problematica')
st.write("##")


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
from matplotlib.pyplot import figure
import numpy as np
from numpy.lib.polynomial import polyval
from pylab import *
#Cargamos con numpy los archivos npy
recorrido = np.load("f1.npy")
recorrido2 = np.load("f2.npy")

#valores del eje x
x= np.arange(start=1,stop=50,step=1)
#z sera el valor recorrido sera el eje 'y' y los numeros son los grados
z= np.polyfit(x,recorrido,1)
z2=np.polyfit(x,recorrido2,2)

figure()
plot(x,recorrido,'oy')
plot(x,recorrido2,'o')
plot(x,polyval(z,x),'-')
plot(x,polyval(z2,x),'-')
show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('test/Preg3.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
