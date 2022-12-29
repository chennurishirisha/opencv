# mark  text on image
import numpy as np
import cv2
img = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\byke.jpeg')
img = cv2.resize(img,(600,700))
font = cv2.FONT_HERSHEY_COMPLEX
#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
# yellow = cv2.LINE_4, red = cv2.LINE_AA, and green = cv2.LINE_8. 
img = cv2.putText(img,'BYKE',(250,600),font,4,
                  (250,0,0),2,cv2.LINE_AA)  #red color text


img = cv2.putText(img,'BYKE',(25,100),font,4,
                  (125,0,125),10,cv2.LINE_4)  #yellow color taxt

img = cv2.putText(img,'BYKE',(150,300),font,4,
                  (0,56,250),5,cv2.LINE_8)  #green color text

cv2.imshow('rest',img)
cv2.waitKey(0)
cv2.destroyAllWindows()