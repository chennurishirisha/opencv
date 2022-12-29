import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'C:\Python\Lib\site-packages\cv2\data\\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(r'C:\Python\Lib\site-packages\cv2\data\\haarcascade_eye.xml')

image = cv2.imread(r'C:\\Users\\shiri\\OneDrive\\Desktop\\parents.jpeg')
cv2.imshow('original image',  image)
cv2.waitKey()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces == ():
    print('no faces found')
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 128), 2)
    cv2.imshow('face detection', image)
    cv2.waitKey()

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,45,198), 2)
        cv2.imshow('face detection',image)

        cv2.waitKey()

cv2.destroyAllWindows()




























cv2.destroyAllWindows()
