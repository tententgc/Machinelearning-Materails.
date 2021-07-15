import cv2

img = cv2.imread("image/girl.jpg")
#reafikke classifier 
face_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")
gray_img  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#จำแนกใบหน้า 
scaleFactor = 1.1 #ตรวจจาก เคสทดสอบ
minNeighber = 3 #จำนวนวงที่ตี
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

#แสดงตำแหน่งเจอใหหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
cv2.imshow("original",img)
cv2.waitKey()
cv2.destroyAllWindows()
