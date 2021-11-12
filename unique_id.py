import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('00026.png')
print(np.unique(img))
print(img.shape)

plt.imshow(img[...,0])
plt.show()
plt.imshow(img[...,1])
plt.show()
plt.imshow(img[...,2])
plt.show()