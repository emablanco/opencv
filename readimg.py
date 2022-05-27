import cv2

#"PATH DE LA IMAGEN", (0 = a gris). Por defecto 1,  muestra a color)
imagen = cv2.imread('wallpapers.png',0)

#nombre de la visualizacion
cv2.imshow('Prueba de imagen', imagen)

#Guardar IMAGEN
cv2.imwrite("test.png",imagen)

#tiempo de visualizacion(milisegundos)
cv2.waitKey(1000)

#cerrar las ventanas abiertas durante el proceso
cv2.destroyAllWindows()
