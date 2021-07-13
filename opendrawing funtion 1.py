import cv2
img = cv2.imread("dale.jpg")
# img =cv2.line(img,(0,0),(255,255),(0,0,255),10)     #เส้นตรง (image , start ,stop,color,ความหนา)
# img =cv2.arrowedLine(img,(20,0),(400,400),(0,255,255),10) #Arrow (image , start ,stop,color,ความหนา)
# img =cv2.rectangle(img,(384,0),(510,128),(0,0,255),5) #สีเหลี่ยม (image ,จุดยอดแรก , จุดยอดอีกฝั่ง , color , ความหนาเส้น)
# img = cv2.circle(img,(447,63),(63),(255,0,0),(1))  #วงกลม(image,start,radian, color, ความหนา if <-1  เป็นวงกลมทึบ)
# img =cv2.putText (img,"Opencv", (10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)  #เส้นตรง 

cv2.imshow("Result", img) #show img output on values
cv2.waitKey(0)
cv2.destroyAllWindows()


