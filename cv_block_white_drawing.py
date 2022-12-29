import cv2
import numpy as np

#img = np.zeros([512,512,3],np.uint8)*255  #for block screen
img = np.ones ([512,512,3],np.uint8)*255  # for white color
# here line accept 5 parameter (img,starting,ending,color,thickkness)
img = cv2.line(img,(0,0),(200,200),(245,7,31),5)# color format BGR

#arrowed line accept also accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img,(0,152),(255,255),(255,0,125),10)

# rectangle accept parameter (img,start_co,end_co,colot,thickness)
img = cv2.rectangle(img,(384,10),(510,128),(128,0,255),5)#(5..>-1)then the sruare is totally filled

# circle-accept(img star-co,radious,color,thickness)
img = cv2.circle(img,(447,125),63,(214,255,0),5)

font = cv2.FONT_HERSHEY_COMPLEX
#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)

img = cv2.putText(img,'BYKE',(20,500),font,4,
                  (0,125,125),5,cv2.LINE_AA)

# ellipse-accept(img,startt_cor,(length,height),color,thickness)

img = cv2.ellipse(img,(400,600),(100,50),125,130,360,155,5)

cv2.imshow('rest',img)
cv2.waitKey(0)
cv2.destroyAllWindows()