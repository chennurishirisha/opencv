# contours are continuous lines or curves that bound or cover the full boundary of an object in an image
import cv2
import numpy as np
#image = cv2.imread(r'C:/Users/shiri/OneDrive/Desktop/parents.jpeg')
image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\parents.jpeg')
cv2.imshow('originalimage', image)
cv2.waitKey()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 30 , 200)
cv2.imshow('edges image', edges)
cv2.waitKey()

contours, hierachy = cv2.findContours(edges , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny edges after contouring', edges)
cv2.waitKey()
print('Total no of contours are' + str(len(contours)))
cv2.drawContours(image , contours,  -1, (255, 0, 255), 4)

cv2.imshow('contours', image)
cv2.waitKey()



cv2.destroyAllWindows()
