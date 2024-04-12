import cv2 as cv2
from PIL import Image, ImageFilter
import numpy as np

image_path = "AD_Confianca.png"
image  = cv2.imread(image_path)
image = cv2.resize(image, (400, 400))

#Converter para binária
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(image, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255,cv2.THRESH_BINARY_INV)
resultado = np.vstack([
np.hstack([suave, bin]),
np.hstack([binI, cv2.bitwise_and(image, image, mask = binI)])
])
cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

