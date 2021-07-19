import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/currency.jpg",0)
sobelx = cv2.Sobel(img,-1,1,0)
sobely = cv2.Sobel(img,-1,0,1)
sobelix = cv2.Sobel(img,-1,1,0)
sobelxy =cv2.bitwise_or(sobelx,sobely)
images =[img,sobelx,sobely,sobelxy]
titles =["output","sobelx","sobely","sobelxy"]
for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])    
    plt.xticks([]), plt.yticks([])
plt.show()
