import cv2


#input video
cap = cv2.VideoCapture("video/BNK.mp4")
#read classifier
face_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

# show output video
while(cap.isOpened()):
    check, frame = cap.read()
    if check == True:
         gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #check face
         scaleFactor = 1.1  # ตรวจจาก เคสทดสอบ
         minNeighber = 5  # จำนวนวงที่ตี
         face_detect = face_cascade.detectMultiScale(
             gray_img, scaleFactor, minNeighber)
         #show facedetect
         for (x, y, w, h) in face_detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
            cv2.imshow("Output", frame)

         if cv2.waitKey(1) & 0xFF == ord("q"):
             break
    else:
        break
cap.release()
cv2.destroyAllWindows()
