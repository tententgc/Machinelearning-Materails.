import cv2
img = cv2.imread("image/blackpink.jpg")

# read cascade
face_cascade = cv2.CascadeClassifier("detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("detect/haarcascade_eye_tree_eyeglasses.xml")

#exchage rgb to gray
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)
eye_detect = eye_cascade.detectMultiScale(gray_img, 1.1, 4)
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    for (ex, ey, ew, eh) in eye_detect:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 5)

cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()
