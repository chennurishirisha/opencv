# creating image border
# with the help of cv2.copyMakeBorder() function.
#it take parameters like (img,border_width(4-sides),border_height)
#boder width = top,bottom,right,left


import cv2
import numpy as np
img = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\thor.jpeg')
img = cv2.resize(img,(1000,600))
# creating image boder
brdr = cv2.copyMakeBorder(img,10,10,20,20,
                          cv2.BORDER_CONSTANT,value = [25,0,255])
cv2.waitKey(0)
cv2.destroyAllWindows()