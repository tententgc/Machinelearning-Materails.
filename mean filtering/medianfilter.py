import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/noise.png")

#filter 2d original 
filter2d= cv2.filter2D(img, -1, np.ones((5, 5), np.float32)/25)
#blur
mean = cv2.blur(img,(5,5))
median  = cv2.medianBlur(img,5)

titles = ['original', 'filter 2d original','maan' ,'meadian']
images = [img,filter2d,mean,median]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
