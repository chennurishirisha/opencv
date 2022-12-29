import cv2
import numpy as np
image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\thor.jpeg', 0)# take 'gray' scale image only.
cv2.imshow('Original image', image)

cv2.waitKey()

## extract sobel edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow('sobel_x', sobel_x)
cv2.waitKey()

cv2.imshow('sobel_y', sobel_y)
cv2.waitKey()

# join the x,y_directions by using bitwise or
sobel_OR = cv2.bitwise_or(sobel_x , sobel_y)
cv2.imshow('Sobel_OR' , sobel_OR)
cv2.waitKey()

## extract laplocation edges:

laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('laplacian_image' , laplacian)
cv2.waitKey()

## extract canny edges
#popular edges detection technique
# then we to provide two values: thresold1 and thresold2. Any gradient values larger than thresold2
# is considered to be an edge. Any value below threshold1 is considered not to be on edge.
#the values b.w threshold1 and 2  are either classified as edges or non edggs non edges based on how their
#intensities are connected,in this case, any gradient values below 60 are considerd non_edges

canny1 = cv2.Canny(image ,60, 120)
cv2.imshow('canny_edge_image',canny1)
cv2.waitKey()


canny2 = cv2.Canny(image ,60, 170)
cv2.imshow('canny_edge_image',canny2)
cv2.waitKey()

canny3 = cv2.Canny(image ,160, 200)
cv2.imshow('canny_edge_image',canny3)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.destroyAllWindows()