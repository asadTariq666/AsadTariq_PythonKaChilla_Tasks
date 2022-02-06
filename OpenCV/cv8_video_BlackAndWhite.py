import cv2 as cv
import sys
cap = cv.VideoCapture("OpenCV/Resources/video1.mp4")

while(1):
    (ret,frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, b_w) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    if ret == True:
        cv.imshow('video',b_w)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
cv.destroyAllWindows()
