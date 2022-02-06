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
    if ret == True:
        cv.imshow('Frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

# Step4 - Release and close windows
cap.release()
cv.destroyAllWindows()
