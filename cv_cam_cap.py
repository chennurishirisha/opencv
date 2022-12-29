import cv2
"""img = cv2.imread('C:\\Users\\shiri\\OneDrive\\Desktop\\byke.jpeg',1)
cv2.imshow('originalimage',img)
cv2.waitKey(0)
cv2.distroyAllWindow()
"""

abc = cv2.VideoCapture(0)

while (True):
    ret_,frame = abc.read()
    cv2.imshow('abc',frame)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break
    abc.release()
cv2.destroyAllWindows()