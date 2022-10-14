import streamlit as st
import pandas as pd
from PIL import Image

st.title('Pregunta 2')
st.write("Coloque cada una las siguientes imágenes en la posición señalada dentro de la plantilla de salida. Debe redimensionar y rotar las figuras. Programe un script en Python + Pygame + PIL")

imagen= Image.open('Imagen.png')
st.image(imagen, caption='Imagen de Segunda problematica')
st.write("##")
imagen2=Image.open('plantilla.png')
st.image(imagen2, caption='Donde colocar imagenes')


mostrar=['Ocultar Codigo', 'Mostrar Codigo']
page = st.radio ('Codigo',mostrar)
if page == 'Mostrar Codigo':
    codigo = ''' 
import pygame as py
from pygame.locals import *
import sys
from PIL import Image 

#Abriremos las imagenes y luego les cambiamos el tamaño
def RotIm(fig,nom):
    fig = Image.open(fig).resize((116,116))
    fig.save(nom+".png")
RotIm("Figura1.png","Fig1_py")
RotIm("Figura2.png","Fig2_py")
RotIm("Figura3.png","Fig3_py")
RotIm("Figura4.png","Fig4_py")

#Iniciamos pygame
py.init()
#Seteamos el tamano de la pantalla 
Screen= py.display.set_mode((759,185))
#Cargamos imagenes y separa canales pero mantiene los canales alpha
fig_1=py.image.load("Fig1_py.png")
fig_2=py.image.load("Fig2_py.png")
fig_3=py.image.load("Fig3_py.png")
fig_4=py.image.load("Fig4_py.png")

#Cargamos la plantilla en la pantalla
background=py.image.load("plantilla.png")

#Rotamos las imagenes los grados que salen en la segunda variable
rotar_1=py.transform.rotate(fig_1,80)
rotar_2=py.transform.rotate(fig_2,100)
rotar_3=py.transform.rotate(fig_3,50)
rotar_4=py.transform.rotate(fig_4,112)

#Cargamos todas las imagenes en sus respectivas posiciones
Screen.blit(background,(0,0))
Screen.blit(rotar_1,(10,20))
Screen.blit(rotar_2,(204,18))
Screen.blit(rotar_3,(380,12))
Screen.blit(rotar_4,(600,13))

py.display.flip()
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()'''
    st.code(codigo, language='python')
cambio=['Ocultar Resultados', 'Mostrar Resultados']
MostrarReusltado = st.radio ('Resultado',cambio)
if MostrarReusltado == 'Mostrar Resultados':
    
    imagenRes= Image.open('Resultado2.png')
    st.image(imagenRes, caption='Resultado')
    st.write("##")
