import cv2
import numpy as np

image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\housedrawing.jpeg')
cv2.imshow('House Image', image)
cv2.waitKey()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 58), 3)
    cv2.imshow('contour Image', image)
    cv2.waitKey(0)

#cvv2.approxPolyDp(contour,Approximation Accuracy, Closed)
for c in contours:
    accuracy = cv2.arcLength(c, True) * 0.03
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 45, 65), 3)
    cv2.waitKey()



cv2.destroyAllWindows()