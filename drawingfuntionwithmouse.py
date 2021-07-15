from _typeshed import SupportsDivMod
import cv2
img = cv2.imread("dale.jpg") 


def clickposition(event, x, y, flask, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pass


#show img
cv2.imshow("Output", img)
cv2.setMouseCallback("Output", clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()
