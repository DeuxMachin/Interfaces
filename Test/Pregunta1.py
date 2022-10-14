import streamlit as st
import pandas as pd
from PIL import Image


def main():
    st.title('Pregunta 1')

    st.subheader("Dada la siguiente figura obtenga los momentos invariantes de Hu (H1-H7) y la Tabla Resumen. ""\n"
     "Programe un script en Python que obtenga los Hu(i=1..7) de cada una de las vocales. Puede utilizar CV2.")
    imagen= Image.open('test/vocales.png')
    st.image(imagen, caption='Imagen de primera problematica')
    st.write("##")
    TablaOrigen=[{'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E': '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''},
                        {'Momentos de Hu de la letra A': '', 'Momentos de Hu de la letra E':  '', 'Momentos de Hu de la letra I': '','Momentos de Hu de la letra O':'','Momentos de Hu de la letra U':''}]
    Show=pd.DataFrame(TablaOrigen,index= ('Log(H_1)','Log(H_2)','Log(H_3)','Log(H_4)','Log(H_5)','Log(H_6)','Log(H_7)'))
    st.table(Show)
   
    st.write("##")
    st.write('¿ Qué conclusión obtiene al analizar la Tabla Resumen? Explique claramente y con detalle')

    st.write("")

    mostrar=['Ocultar Codigo', 'Mostrar Codigo']
    page = st.radio ('Codigo',mostrar)
    if page == 'Mostrar Codigo':
        codigo = '''
img = Image.open('vocales.png')
#Abrimos la imagen a la que queremos realizar los momentos de Hu y cortar las vocales
#Generamos un borde para la vocal A para cortar en la imagen (Izq,arriba,der,abajo)
borderA = (0,0,430,0)

#Creamos la variable para general la nueva imagen cortada, con el comando ImageOps.crop(Imagen a cortar, borde que se le quiere cortar)
imgA = ImageOps.crop(img, borderA)
#Mostramos la imagen cortada
#imgA.show()
#Se guarda bajo el nombre "ImgA.png"
imgA.save("ImgA.png")

#Se repite el proceso con todas las vocales
borderE = (125,0,310,0)

imgE = ImageOps.crop(img, borderE)
#imgE.show()
imgE.save("ImgE.png")

borderI = (230,0,230,0)

imgI = ImageOps.crop(img,borderI)
#imgI.show()
imgI.save("ImgI.png")

borderO = (320,0,125,0)

imgO = ImageOps.crop(img,borderO)
#imgO.show()
imgO.save("ImgO.png")

borderU = (435,0,0,0)

imgU = ImageOps.crop(img,borderU)
#imgU.show()
imgU.save("ImgU.png")

#Imagen A
#Con OpenCV se crea la variable y se lee la imagen en binario para que solo se detecte el blanco y negro
imA= cv2.imread('ImgA.png',cv2.THRESH_BINARY)

#Se calculan los momentos normales de la imagen anteriormente leida
momentosA = cv2.moments(imA)

#Y con los momentos normales se calculan los momentos de Hu de la imagen
huMomentosA = cv2.HuMoments(momentosA)

#print(huMomentosA)
#Ya que los numeros no son tan comparables asi, se le aplica una escala en logaritmo al momento para que sea mas entendible
for i in range(0,7):
    #El nuevo momento se reemplaza por la escala que se ve a continuacion 
    huMomentosA[i] = -1* math.copysign(1.0, huMomentosA[i]) * math.log10(abs(huMomentosA[i]))
    #Se muestra en pantalla el nuevo numero
    print("Momento de Hu A",i+1,":",huMomentosA[i])

#Imagen E
#Se repite el mismo proceso con las siguientes vocales
imE= cv2.imread('ImgE.png',cv2.THRESH_BINARY)

momentosE = cv2.moments(imE)

huMomentosE = cv2.HuMoments(momentosE)

#print(huMomentosE)

for i in range(0,7):
    huMomentosE[i] = -1* math.copysign(1.0, huMomentosE[i]) * math.log10(abs(huMomentosE[i]))
    print("Momento de Hu E",i+1,":",huMomentosE[i])

    #Imagen I 
imI= cv2.imread('ImgI.png',cv2.THRESH_BINARY)

momentosI = cv2.moments(imI)

huMomentosI = cv2.HuMoments(momentosI)

#print(huMomentosI)

for i in range(0,7):
    huMomentosI[i] = -1* math.copysign(1.0, huMomentosI[i]) * math.log10(abs(huMomentosI[i]))
    print("Momento de Hu I",i+1,":",huMomentosI[i])


#Imagen O
imO= cv2.imread('ImgO.png',cv2.THRESH_BINARY)

momentosO = cv2.moments(imE)

huMomentosO = cv2.HuMoments(momentosO)

#print(huMomentosO)

for i in range(0,7):
    huMomentosO[i] = -1* math.copysign(1.0, huMomentosO[i]) * math.log10(abs(huMomentosO[i]))
    print("Momento de Hu O",i+1,":",huMomentosO[i])


#Imagen U
imU= cv2.imread('ImgU.png',cv2.THRESH_BINARY)

momentosU = cv2.moments(imU)

            huMomentosU = cv2.HuMoments(momentosU)

#hprint(huMomentosU)

for i in range(0,7):
    huMomentosU[i] = -1*math.copysign(1.0, huMomentosU[i]) * math.log10(abs(huMomentosU[i]))
    print("Momento de Hu U",i+1,":",huMomentosU[i])'''
        st.code(codigo, language='python')
    
    cambio=['Ocultar Resultados', 'Mostrar Resultados']
    MostrarCode = st.radio ('Resultado',cambio)
    if MostrarCode == 'Mostrar Resultados':
        datos=[{'Momentos de Hu de la letra A': 2.7679626, 'Momentos de Hu de la letra E': 2.84808283, 'Momentos de Hu de la letra I': 2.91830764,'Momentos de Hu de la letra O':2.84808283,'Momentos de Hu de la letra U':2.76521999},
                        {'Momentos de Hu de la letra A': 6.78407225, 'Momentos de Hu de la letra E': 6.82375956, 'Momentos de Hu de la letra I': 7.91617743,'Momentos de Hu de la letra O':6.82375956,'Momentos de Hu de la letra U':6.78077338},
                        {'Momentos de Hu de la letra A': 10.22545715, 'Momentos de Hu de la letra E': 11.05653333, 'Momentos de Hu de la letra I': 11.538809,'Momentos de Hu de la letra O':11.05653333,'Momentos de Hu de la letra U':10.92319622},
                        {'Momentos de Hu de la letra A': 9.81212627, 'Momentos de Hu de la letra E': 11.2058251, 'Momentos de Hu de la letra I': 11.45488346,'Momentos de Hu de la letra O':11.2058251,'Momentos de Hu de la letra U':9.98910525},
                        {'Momentos de Hu de la letra A': 19.83516113, 'Momentos de Hu de la letra E': 22.38383557, 'Momentos de Hu de la letra I': -23.95872575,'Momentos de Hu de la letra O':22.38383557,'Momentos de Hu de la letra U':20.53051627},
                        {'Momentos de Hu de la letra A': 13.28852683, 'Momentos de Hu de la letra E': -15.88342446, 'Momentos de Hu de la letra I': 15.81286175,'Momentos de Hu de la letra O':-15.88342446,'Momentos de Hu de la letra U':14.0089053},
                        {'Momentos de Hu de la letra A': -20.68756955, 'Momentos de Hu de la letra E': -22.6931085, 'Momentos de Hu de la letra I': -22.95384257,'Momentos de Hu de la letra O':-22.6931085,'Momentos de Hu de la letra U':-20.68949684}]
        df=pd.DataFrame(datos,index= ('Log(H_1)','Log(H_2)','Log(H_3)','Log(H_4)','Log(H_5)','Log(H_6)','Log(H_7)'))
        st.table(df)
if __name__ == '__main__':

    main()
   