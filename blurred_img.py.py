## image blurred
import cv2
import numpy as np
image = cv2.imread(
images = cv2.resize(image, (560,480))
#kernel = np.ones((3,3) , np.float32) / 9
# for burred image
"""
cv2.imshow('original image', image)
cv2.waitKey()
blurred = cv2.filter2D(image, -1, kernel)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey()
cv2.destroyAllWindows()
"""

#more blurrering image
"""
cv2.imshow('original image', image)
cv2.waitKey()
kernel = np.ones((7,7), np.float32) / 49
blurred = cv2.filter2D(image, -1, kernel)
cv2.imshow('blurred image', blurred)
cv2.waitKey()
cv2.destroyAllWindows()
"""

# blurred image technique

cv2.imshow('original IMage',images)
cv2.waitKey()

img = cv2.blur(images, (3,3))
cv2.imshow('Blur',img)
cv2.waitKey()


img1 = cv2.GaussianBlur(images, (7,7), 0)
cv2.imshow('GaussianBlur' , img1)
cv2.waitKey()

img2 = cv2.medianBlur(images,5)
cv2.imshow('GaussianBlur',img2)
cv2.waitKey()

img3 = cv2.bilateralFilter(images, 9 , 75 ,75)
cv2.imshow('Biateral Filter',img3)
cv2.waitKey()
cv2.destroyAllWindows()