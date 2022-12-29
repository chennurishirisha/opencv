import cv2
import numpy as np
#face_cascade.load('haarcascade_frontalface_default.xml')
face_classifier = cv2.CascadeClassifier(r'C:\Python\Lib\site-packages\cv2\data\\haarcascade_frontalface_default.xml')
image = cv2.imread(r'C:\\Users\\shiri\\Desktop\\art_picture.jpeg')

cv2.imshow('Oiginal Image', image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces == ():
    print('no faces found')
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 128), 2)
    cv2.imshow('face detection', image)
    cv2.waitKey()
    cv2.destroyAllWindows()