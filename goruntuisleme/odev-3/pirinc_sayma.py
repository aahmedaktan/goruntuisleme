import cv2
import numpy as np

resim=cv2.imread("sayma.jpeg")
resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
ret, gri_foto=cv2.threshold(resim,150,255,0)

sayma,hierarchy=cv2.findContours(gri_foto,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(sayma))

cv2.imshow("orijinal",resim)
cv2.imshow("gri",gri_foto)
cv2.waitKey()

