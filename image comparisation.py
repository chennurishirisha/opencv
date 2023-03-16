import cv2
import numpy as np

original = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\varshu.jpg')

duplicate = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\varshu original.jpg')
if original.shape == duplicate.shape:
    print('the images are same size and channels')
    difference =  cv2.subtract(original , duplicate)
    b, g, r =  cv2.split(difference)

    if cv2.countNonZero(b) == 0 and  cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
      print('the images are completely Equal')
else:
   print('the images are not equal')


