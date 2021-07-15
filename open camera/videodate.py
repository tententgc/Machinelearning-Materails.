import cv2
import datetime 
cap = cv2.VideoCapture("BNK.mp4")
while (cap.isOpened()): 
    check, frame = cap.read()
    if check == True:
        currentdate = str(datetime.datetime.now())
        cv2.putText(frame,currentdate, (10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),cv2.LINE_4)
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
