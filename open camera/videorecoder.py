import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480))
# while (True):
while (cap.isOpened()): #ถ้า video เปิดใช้งานได้จะเปิดได้
    check, frame= cap.read() #exchage RGB to gray scale 
    if check==True:
        cv2.imshow('frame',frame) #showvideo grayscal  if gray  is framge it is RGB video because it has a real video
        result.write(frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')): #put Q to exit
            break
    else:
        break
result.release()
cap.release()
cv2.destroyAllWindows()
