import cv2
import numpy as np

def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #CLEANING THE IMAGE using gaussion blur
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    #EXTRACT EDGES
    canny = cv2.Canny(img_blur, 30, 70)

    # binarize the image
    ret ,thresh = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
#40 ABOVE BLOCK AND40 BELLOW WHITE
    return thresh


# initialising web cap
cap = cv2.VideoCapture(0)

while True:
    ret ,frame = cap.read()#ret is boolean value whether the image is captured or not
    cv2.imshow('Live_Sketch', sketch(frame))
    if cv2.waitKey(1) == 9:  # 9 is enter key
        break

cap.release()
cv2.destroyAllWindows()