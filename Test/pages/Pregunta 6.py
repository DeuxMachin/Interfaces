import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 6')
st.write(" Obtenga la Interpolación de Chebyshev desde cheby.npy. ¿Qué conclusiones obtiene? ¿Escriba el polinomio con sus coeficientes? ")

imagen= Image.open('Pregu6.png')
st.image(imagen, caption='Imagenes Sexta problematica')
st.write("##")


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
import numpy as np
from numpy.linalg import linalg
import numpy.polynomial as pol
import matplotlib.pyplot as pt

data = np.load("cheby.npy")

x=data[0]
y=data[1]

deg = len(x)-1

A=pol.chebyshev.chebvander(x,deg)
c=linalg.solve(A,y)
resultado= pol.Chebyshev(c)
xx=np.linspace(x.min(),x.max(),100)

pt.plot(xx,resultado(xx),'r',label='Interpolacion Chebychev')
pt.scatter(x,y,label='Puntos de datos')
pt.ylabel('F(x)')
pt.xlabel('T(s)')
pt.legend()
pt.show()'''
    st.code(codigo, language='python')

cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('Preg6.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")