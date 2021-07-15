import cv2
import numpy
img = cv2.imread("dale.jpg")


def clickposition(event, x, y, flask, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        img_color = numpy.zeros([300,300,3],numpy.uint8)
        img_color[:] =[blue,green,red]
        cv2.imshow("Result",img_color)

#show img
cv2.imshow("Output", img)
cv2.setMouseCallback("Output", clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()
