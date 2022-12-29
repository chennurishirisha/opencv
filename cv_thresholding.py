import cv2
import numpy as np

image = cv2.imread(r'C:/Users/shiri/OneDrive/Desktop/sun_image.jpeg')
cv2.waitKey()

#the values below 127 goes to 0 (block),everythimg above goes to 255 (white)
_,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshould image', thresh1)
cv2.waitKey()

# values below 127 go to 255 and values above 127 go to 0
_,thresh2 = cv2.threshold(image , 127, 225, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh' , thresh2)
cv2.waitKey()

# values above 127 are truncated (held) at 127(the 255 argument is unused)
_, thresh3 = cv2.threshold(image , 127 , 255, cv2.THRESH_TRUNC)
cv2.imshow('thresh_trunc' , thresh3)
cv2.waitKey()
cv2.destroyAllWindows()

#values below 127 go to 0 above are unchanged
_,thresh4 = cv2.threshold(image , 127 , 255, cv2.THRESH_TOZERO)

cv2.imshow('thresh_toZero' , thresh4)


# reverse of above ,below 127 is unchaged above 127 goes to 0
_,thresh5 = cv2.threshold(image , 127 , 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('thresh_toZero_inv' , thresh5)


cv2.waitKey()
cv2.destroyAllWindows()