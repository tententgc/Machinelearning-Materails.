import cv2
cap = cv2.VideoCapture("BNK.mp4")
# while (True):
while (cap.isOpened()):  # ถ้า video เปิดใช้งานได้จะเปิดได้
    check, frame = cap.read()
    if check == True:
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):  # put Q to exit
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
