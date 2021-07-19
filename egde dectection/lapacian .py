import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/currency.jpg",0)
lap =cv2.Laplacian(img,-1)
cv2.imshow("ori",img)
cv2.imshow("lap",lap)
cv2.waitKey(0)
cv2.destroyAllWindows()