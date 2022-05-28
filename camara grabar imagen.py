#! /bin/python3.9


#importo libreria opencv
import cv2

#creo un objeto "VideoCapture" al cual le paso el indice de la camara.
captura = cv2.VideoCapture(0) #iniciar la captura

#VideoWriter => permite pasar 4 argumentos
#   *Nombre del Video
#   *codec del video => *'XVID' este es el que se encuentra en la documentacion
#   *fps
#   *tamaño del video

 
salida = cv2.VideoWriter("VideoSalida.mp4",cv2.VideoWriter_fourcc(*'XVID'), \
        60.0,(640,480))

#Leer la imagen a cada momento
while (captura.isOpened()):

    #devuelve dos elemento True or False
    ret,imagen = captura.read()
    
    #si tenemos imagen
    if ret == True:
    
        #Que vamos a mostrar => imagen
        cv2.imshow("video",imagen)
        #incluyo en la salida la imagen que la camara
        salida.write(imagen)
        #opencv dice que usemos & 0xFF cuando usamos maquina de 64bits
        if cv2.waitKey(1) & 0xFF == ord('s'): #la tecla "s" detiene el programa

            break

#finalizamos la captura
captura.release()
#Finalizar la grabacion
salida.release()
#para cerrar cualquier ventana que puedo quedar abierta
cv2.destroyAllWindows()
