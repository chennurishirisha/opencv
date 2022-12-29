import cv2 as cv
import numpy as np
import glob
import os

logo =cv.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\watermark1.png')
h_logo, w_logo,_ = logo.shape
print(h_logo,w_logo)
images_path= glob.glob(r'C:/Users/shiri/OneDrive/Desktop/*.*')


print("Adding watermark")

for img_path in images_path:
    img = cv.imread(img_path)
    h_img, w_img, _ = img.shape
    print(h_img, w_img)
    center_x = int(w_img / 2)
    center_y = int(h_img / 2)
    top_y = center_y + int(h_logo / 2)
    left_x = center_x + int(w_logo / 2)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo


    #roi
    roi = img[top_y:bottom_y, left_x:right_x]

    # Add the logo to the roi
    result = cv.addWeighted(roi, 1, logo, 0.3, 0)
    #replace the Roi on the image

    img[top_y:bottom_y, left_x:right_x] = result

    #get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite('D:/cv/logo_' + filename, img)
print('watermark added to all the images')




"""

#!pip install python-resize-image
import cv2
from resize_image import *
image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\bestFrdsCats.png')
image = resizing_image(image, 0.6)
watermark = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\watermark1.png')
image_height,image_width = image.shape[:2]
watermark_height,watermark_width = watermark.shape[:2]
cx, cy = int(image_width/2), int(image_height/2)

left_x = cx - int(watermark_width/2)
right_x = left_x + watermark_width
top_y = cy - int(watermark_height/2)
bottom_y = top_y + watermark_height

roi = image[top_y: bottom_y, left_x: right_x]
addWeightedImage = cv2.addWeighted(roi, 1, watermark, 0.2, 0)
image[top_y: bottom_y, left_x:right_x] = addWeightedImage
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

