import cv2
img = cv2.imread("dale.jpg",0)#อ่านค่า
#สามารภเขียนได้ 2 แบบ cv2.IMREAD_COLOR หรือ 1  ,cv2.IMREAD_GRAYSCALE  หรือ 0 , cv2.IMREAD_UNCHANGED หรือ -1 
img_resize = cv2.resize(img, (400, 200)) #resize img กว้าง * ยาวว

print(type(img.ndim)) #ตรวจสอบ type array
print(img) #ปริ้น rgb hex
cv2.imshow("Show result",img)#show inmage on windows
cv2.waitKey(0) #ถ้าใส้ delay=5000  5 วินนาทีจะปิดเอง
#delat millisec 
cv2.destroyAllWindows()
#destroy ถ้าคลิกอะไรสักอย่างอย่างนึงหาย
cv2.imwrite('result.png',img)
#write file in this program to export
