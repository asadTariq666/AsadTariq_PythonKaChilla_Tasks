
#step1 - Import Libraries
import cv2 as cv
import numpy as np

#Step2 - Read frames from Camera
cap = cv.VideoCapture(0) # webcam number 1
if(cap.isOpened()==False):
    print('there is an error')

# read until the end
#Step3 - Display frame by frame
while(cap.isOpened()):
    #capture Frame by frame
    ret, frame =cap.read()

# Step4 - Changing in to grayscale
    gray =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh, b_w) = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    if ret == True:
        cv.imshow('Original',frame)
        cv.imshow('GrayScaled',gray)
        cv.imshow('Black and white',b_w)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break  
    else:
        break 

# Step5 - Release and close windows
cap.release()
cv.destroyAllWindows()
 