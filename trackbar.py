#การสร้าง trackbar
import cv2
import numpy as np

img =np.zeros((400,400,3),np.uint8)
cv2.namedWindow("color trackbar")

def display(value):
    pass

#create trackbar slider
cv2.createTrackbar("B","color trackbar",0,255,display)
cv2.createTrackbar("G","color trackbar",0,255,display)
cv2.createTrackbar("R","color trackbar",0,255,display)

while True:
    cv2.imshow("color trackbar",img)
    if cv2.waitKey(1)& 0xFF == ord("q"):
        break

    blue =cv2.getTrackbarPos("B","color trackbar")
    green =cv2.getTrackbarPos("G","color trackbar")
    red =cv2.getTrackbarPos("R","color trackbar")
    img[:]= [blue,green,red]

cv2.destroyAllWindows()