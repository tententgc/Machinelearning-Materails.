import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/noise.png")
# kernel = np.ones((3,3),np.float32)/9

convo = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convo1 = cv2.filter2D(img, -1, np.ones((5, 5), np.float32)/25)


titles = ['original', 'convolution 3x3', 'convolution 3x3']
images = [img,convo,convo1]

for i in range (len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
