import cv2
cap = cv2.VideoCapture("BNK.mp4")
# while (True):
while (cap.isOpened()): #ถ้า video เปิดใช้งานได้จะเปิดได้
    check, frame = cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #exchage RGB to gray scale 
    if check==True:
        cv2.imshow('frame',gray) #showvideo grayscal  if gray  is framge it is RGB video because it has a real video
        if (cv2.waitKey(1) & 0xFF == ord('q')): #put Q to exit
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
