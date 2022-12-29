import cv2
import numpy as np

image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\parents.jpeg')
cv2.imshow('originalimage', image)
cv2.waitKey()

blank_image = np.zeros((image.shape[0], image.shape[1],3))
original_image = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Edged Image', edges)
cv2.waitKey()
edges = cv2.Canny(gray, 50, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('NO.OF CONTOURS = '+str(len(contours)))

cv2.drawContours(blank_image, contours, -1, (0, 255, 255), 3)
cv2.imshow('Blank_image Contours',blank_image)
cv2.waitKey()

cv2.drawContours(original_image, contours, -1, (0, 255, 255),3)
cv2.imshow('original_image contours', original_image)
cv2.waitKey()

cv2.destroyAllWindows()