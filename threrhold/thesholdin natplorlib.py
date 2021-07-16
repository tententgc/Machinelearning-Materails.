#show threshold in matplotlib
import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread("image/gradient.png")

thersh, r1= cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
thersh, r2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
thersh, r3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thersh, r4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thersh, r5 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)

images = [gray_img,r1,r2,r3,r4,r5]
titles =["Original","binary","Binary_INV","Thresh_TRUNC","tozero","tozero_INV"]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
