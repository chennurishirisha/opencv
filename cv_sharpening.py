import cv2
import numpy as np
image = cv2.imread(r"C:\\Users\\shiri\\OneDrive\\Desktop\\bestFrdsCats.png")
image = cv2.resize(image,(560,540))
sharpening_kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
cv2.imshow('original image', image)
cv2.waitKey()
sharpen = cv2.filter2D(image, -1 ,sharpening_kernel)
cv2.imshow('Sharpen Image',sharpen)
cv2.waitKey()
cv2.destroyAllWindows()