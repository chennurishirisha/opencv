# image blending
# here we use two important functions cv2.add(),cv2.addWeight
#Blending means additions of two images
#if younwant to belnd two images then both have same size
import cv2
import numpy as np
img1 = cv2.imread('c:\\Users\\shiri\\OneDrive\\Desktop\\thor.jpeg')
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\IranMan.jpg')

img2 = cv2.resize(img2,(500,700))
cv2.imshow('thor ==',img1)
cv2.imshow('bro_thor==',img2)
#blending
"""rsult1 = cv2.add(img2,img1)  # numpy addition in this we get module 
cv2.imshow('result ==',rsult)
"""

#result2 = cv2.addweighted(img1,wt1,img2,wt2,gama_val)
result2 = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.waitKey(0)
cv2.destroyAllWindows()


#blending
#rsult = img2+img1  # numpy addition in this we get module 

