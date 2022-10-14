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
from PIL import ImageOps

#Abrimos la imagen para cortar las figuras
img = Image.open('figuras.png')
#Generamos los border a cortar(izq,arriba,der,abajo)
border1 = (4,6,766,5)
#Se corta la imagen
img1= ImageOps.crop(img,border1)
#Se guarda bajo el nombre "Fig1.png"
img1.save("Fig1.png")


#Se repite el proceso con todas las figuras
border2 = (242,5,503,20)
img2= ImageOps.crop(img,border2)
img2.save("Fig2.png")


border3 = (504,23,264,30)
img3 = ImageOps.crop(img,border3)
img3.save("Fig3.png")


border4 = (733,20,8,26)
img4 = ImageOps.crop(img,border4)
img4.save("Fig4.png")

#Se reajusta el tamaño de la imagen
img1.resize((116,116)).save("Fig1_r.png")
img2.resize((116,116)).save("Fig2_r.png")
img3.resize((116,116)).save("Fig3_r.png")
img4.resize((116,116)).save("Fig4_r.png")

#Iniciamos pygame
py.init()
#Seteamos el tamano de la pantalla 
Screen= py.display.set_mode((759,185))
#Cargamos imagenes y se utiliza convert_alpha() para mantener la transparencia detras de la imagen
fig_1=py.image.load("Fig1_r.png").convert_alpha()
fig_2=py.image.load("Fig2_r.png").convert_alpha()
fig_3=py.image.load("Fig3_r.png").convert_alpha()
fig_4=py.image.load("Fig4_r.png").convert_alpha()

#Cargamos la plantilla en la pantalla
background=py.image.load("plantilla.png")

#Rotamos las imagenes los grados que salen en la segunda variable
rotar_1=py.transform.rotate(fig_1,80)
rotar_2=py.transform.rotate(fig_2,99)
rotar_3=py.transform.rotate(fig_3,51)
rotar_4=py.transform.rotate(fig_4,112)

#Cargamos todas las imagenes en sus respectivas posiciones
Screen.blit(background,(0,0))
Screen.blit(rotar_1,(9,19))
Screen.blit(rotar_2,(202,20))
Screen.blit(rotar_3,(379,12))
Screen.blit(rotar_4,(599,13))

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
