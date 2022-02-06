import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

# writing Format, video writer object and file Output
frame_width =int(cap.get(3))  # 4:3
frame_height =int(cap.get(4)) # 4:3
#Saving actual video
out = cv.VideoWriter('OpenCV/Resources/webcam_video.avi', cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
out2 = cv.VideoWriter('OpenCV/Resources/webcam_video2.avi', cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height), isColor=False)
#Converting actual video in  grayscale
while(1):
    (ret,frame) = cap.read()
    gray =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(frame)
        out2.write(gray)
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
out.release()
out2.release()

cv.destroyAllWindows()

