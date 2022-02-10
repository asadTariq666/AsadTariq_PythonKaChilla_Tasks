import cv2 as cv
import numpy as np
#Creating cascade to detect face
face_cascade = cv.CascadeClassifier('OpenCV/Resources/haarcascade_frontalface_default.xml')
img = cv.imread("OpenCV/Resources/2.jpg")

#converting in to grayscale
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#face detection
faces = face_cascade.detectMultiScale(gray_img,1.1,4)

#Draw Rectangle
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

print(img.shape) #(2208, 1242, 3)
#dividing in 2 images
#img =cv.resize(img,(621,1104))
print(img.shape) #(2208, 1242, 3)
cv.imwrite("OpenCV/Resources/face.jpg",img)

cv.imshow("MyImage",img)  
cv.waitKey(0)
cv.destroyAllWindows()