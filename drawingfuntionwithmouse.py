import cv2
import numpy
img = cv2.imread("image/dale.jpg")
# img =numpy.zeros([400,400,3])
point = []
#function clickmouse
def clickposition(event, x, y, flask, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4)
        point.append((x,y))
        if len(point)>=2:
            cv2.line(img,point[-2],point[-1],(255,255,255),5)
        cv2.imshow("Output",img)


#show img
cv2.imshow("Output", img)
cv2.setMouseCallback("Output", clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()
