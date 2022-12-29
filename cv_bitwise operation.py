# bitwise operations includes AND OR XOR NOT
# it is most importtent and use for various purpose like masking
# #And find roi(region of intersect) witch is in complex shape.
import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (150, 100), (200, 250), (255, 255, 255), -1)


img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (10, 10), (170, 190), (255, 255, 255), -1)


cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
#bitwise AND
bitAnd = cv2.bitwise_and(img2, img1)
cv2.imshow('BITWISE AND', bitAnd)

bit_or = cv2.bitwise_or(img2, img1)
cv2.imshow('BITWISE OR', bit_or)

bit_not1 = cv2.bitwise_not(img1)
cv2.imshow('BITWISE NOT1', bit_not1)


bit_xor = cv2.bitwise_xor(img2, img1)
cv2.imshow('BITWISE XOR', bit_xor)

cv2.waitKey(0)

cv2.destroyAllWindows()
