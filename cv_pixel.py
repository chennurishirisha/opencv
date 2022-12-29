import cv2
import numpy as np
img = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\lion.avif')
img = cv2.resize(img, (1024, 700))
cv2.imshow("lion==", img)


print('shape ==', img.shape)
print('no.of pixels ==', img.size)
print('datatype ==', img.dtype)
print('imagetype ==', type(img))


#access a pixel value by its  row and column coordinates
px = img[520, 580]  #store cordinates in variable
print('the pixel of that co-ordinates ==', px) #we get pixels

#now try to find selected channel  nvalue from cordinates
#the three channel..0..>b, 1..>g, 2..>r# 
# accessing only blue pixel
blue = img[580, 520, 0]
print('the pixel having blue color ==', blue)
grn = img[580, 520, 1]#for green pass 1
print('the pixel having grn color ==', grn)
red = img[580, 520, 2] # for red pass 2

print('the pixel having red color ==', red)

cv2.waitKey(0)
cv2.destroyAllWindows()