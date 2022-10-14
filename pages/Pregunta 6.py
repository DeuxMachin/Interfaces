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

#Cargamos los valores que se encuentran en npy
data = np.load("cheby.npy")
#Cargamos los valores de la matriz para otorgar los ejes x e y
x=data[0]
y=data[1]

#Se realizara el "grado"
deg = len(x)-1

#Se crea una matriz que sera del rango de x y deg sacara el angulo del arreglo  1x1
A=pol.chebyshev.chebvander(x,deg)

#Daremos el coeficiente a trabajar y los variables de ordenada
c=linalg.solve(A,y)

resultado= pol.Chebyshev(c)
#Diremos que el inicio sera el valor minimo, el valor maximo sera la pausa y la cantidad
xx=np.linspace(x.min(),x.max(),100)

#Mostrarmos el grafico
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