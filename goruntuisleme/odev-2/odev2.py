import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (True):
    ret, video = kamera.read()
    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    lower=np.array([155, 0, 0])
    upper=np.array([185, 255, 255])

    mask=cv2.inRange(hsv,lower,upper)
    son=cv2.bitwise_and(video, video, mask=mask)
    son=cv2.cvtColor(son, cv2.COLOR_BGR2GRAY)
    ret, son = cv2.threshold(son,5,255,cv2.THRESH_BINARY)

    cv2.imshow("cam", video)
    cv2.imshow("son",son)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()