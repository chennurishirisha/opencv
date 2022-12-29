##  split()and merge( )operation
import cv2
import numpy as np
# read on image

img = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\pikachu.png')

print('shape ==',img.shape) # returna a tuple of number of rows and no. of columns
print('no.of pixels ==',img.size) # return total number of pixels
print('datatype ==',img.dtype) # returns image datatype is 
print('Imagetype ==',type(img))


#now try to split an image
#split  -return  3 channel of ur image which is blue,green,red
print(cv2.split(img))


b,g,r = cv2.split(img)
"""
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.imshow('original',img)
"""
#now if you want to mix the channels then use merge

mr1 = cv2.merge((r,g,b))
cv2.imshow('rgb',mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow('gbr',mr2)
cv2.imshow('orginal',img)



#cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


