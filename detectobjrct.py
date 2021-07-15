import cv2
import numpy
while True:
    img =cv2.imread("image/ball2d.jpg")
    img = cv2.resize(img,(400,400))
    #ช่วงของสี
    lower= numpy.array([5,111,10])
    upper= numpy.array([124,255,133])
    #mask position green
    mask = cv2.inRange(img,lower,upper)
    #แทนที่ mask ด้วยสีต้นแบบ 
    result = cv2.bitwise_and(img,img,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
    cv2.imshow("mask",mask)
    cv2.imshow("Original",img)
    cv2.imshow("result",result)
cv2.destroyAllWindows()