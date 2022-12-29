import cv2
import numpy as np
def get_contour_area(contours):
    all_areas = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

image = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\parents.jpeg')
original_image = image
cv2.imshow('original image',image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('NO.OF CONTOURS = '+str(len(contours)))
print('Contour area before sorting')
print(get_contour_area(contours))
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
print('Contour area after sorting')
print(get_contour_area(sorted_contours))

for c in sorted_contours:

    cv2.drawContours(original_image , [c], -1, (0, 255, 255),3)
    cv2.imshow('Contours By Area', original_image)
    cv2.waitKey()




#cv2.waitKey()
cv2.destroyAllWindows()