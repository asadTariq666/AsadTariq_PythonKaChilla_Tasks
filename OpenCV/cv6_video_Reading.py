import cv2 as cv
import sys
cap = cv.VideoCapture("OpenCV/Resources/video1.mp4")

if (cap.isOpened()== False):
    print('video not found')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 
cap.release()

cv.destroyAllWindows()
