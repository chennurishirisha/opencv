# break video into multiple images and store in a folder

import cv2
vidcap = cv2.VideoCapture('c:\\user\\shiri\\download\\work.avi')
ret,image = vidcap.read()
count = 0
while True:
    if ret == True:
        cv2.imwrite('c:\\user\\shiri\\download\\imgN%d.jpg'%count,image)
        
        
        cv2.imshow('res',image)
        count += 1
        if cv2.waitKey(1)& 0xFF ==ord('q'):
            break
        cv2.destroyAllWindows()

vidcap.release()
cv2.destoyAllWindows()
                                             
            