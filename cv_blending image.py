# image blending with trackbars
import cv2 
import numpy as np
img1 = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\IranMan.jpg')
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\thor.jpeg')
img2 = cv2.resize(img2,(500,700))
cv2.imshow('THOR',img1)
cv2.imshow('IRANMAN',img2)

def blend(x):
    pass
img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win') #create track bar windows
cv2.createTrackbar('alpha','win',1,100,blend)

switch = '0 : OFF\n 1 : ON'  #create switch for invoke the trackbars
cv2.createTrackbar(switch,'win',0,1,blend) #create track bar for switch

while True:
    s = cv2.getTrackbarPos(switch,'win')
    a = cv2.getTrackPos('alpha','win')
    n =  float(a/100)
    print(n)
    if s ==  0:
        dst =img[:]
    else:
        dst = cv.addweighted(img1,1-n,img2,n,0)


cv2.waitKey(0)
cv2.destroyAllWindows()
