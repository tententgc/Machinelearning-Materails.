import cv2
gray_img = cv2.imread("image/gradient.png") 
thersh,result = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thersh, result1 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
thersh, result2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thersh, result3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thersh, result4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("original",gray_img)
cv2.imshow("binary",result)
cv2.imshow("binary_INV",result1)
cv2.imshow("binary_TRUNC",result2)
cv2.imshow("binary_Tozero",result3)
cv2.imshow("binary_TozeoINV",result4)

cv2.waitKey(0)
cv2.destroyAllWindows()
