import cv2
def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture("BNK.mp4")
while True:
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')): #put Q to exit
        break
cap.release()
cv2.destroyAllWindows()
