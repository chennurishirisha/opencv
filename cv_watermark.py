import cv2 as cv
import numpy as np


def scale(image, scale_width):
    (image_height, image_width) = image.shape[:2]
    new_height = int(scale_width / image_width * image_height)
    return cv.resize(image, (scale_width, new_height))

watermark = scale(cv.imread(r"C:\Users\shiri\OneDrive\Desktop\watermark.png", cv.IMREAD_UNCHANGED), 200)
watermark = cv.resize(watermark, (600, 100))

(watermark_height, watermark_width) = watermark.shape[:2]

image = scale(cv.imread(r"C:\Users\shiri\OneDrive\Desktop\bestFrdsCats.png"), 800)
(image_height, image_width) = watermark.shape[:2]

image = cv.cvtColor(image, cv.COLOR_BGR2BGRA)
overlay = np.zeros((image_height, image_width, 4), dtype='uint8')
overlay[image_height-watermark_height: image_height, image_width-watermark_width:image_width] = watermark
cv.addWeighted(overlay, 1.0, image, 1.0, 0, image)

while True:
    cv.imshow('overlay', overlay)
    cv.imshow('image', image)
    cv.imshow('watermark', watermark)
    if cv.waitKey(1) == ord('q'):
        break

# cv.imshow('watermark', watermark)
# cv2.waitKey(0)
# cv2.destroyAllWindows()