import cv2
img = cv2.imread("dale.jpg")
def clickposition(event,x,y,flask,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text=str(x)+","+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",img)



#show img 
cv2.imshow("Output",img)
cv2.setMouseCallback("Output", clickposition)
cv2.waitKey(0)
cv2.destroyAllWindows()
