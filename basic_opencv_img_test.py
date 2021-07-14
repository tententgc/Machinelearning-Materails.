import cv2
img = cv2.imread("dale.jpg", 1) 
img_resize = cv2.resize(img,(400,200))
print(type(img.ndim))
print(img) 
cv2.imshow("Show result", img_resize)
cv2.waitKey(0) 
cv2.destroyAllWindows()
cv2.imwrite('result.png', img)
