import cv2 as cv
import sys
cap = cv.VideoCapture("OpenCV/Resources/video1.mp4")

# writing Format, video writer object and file Output
frame_width =int(cap.get(3))  # 4:3
frame_height =int(cap.get(4)) # 4:3
out = cv.VideoWriter('OpenCV/Resources/video1_gray2.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, (frame_width,frame_height),isColor=False)
out2 = cv.VideoWriter('OpenCV/Resources/video1_BW2.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, (frame_width,frame_height),isColor=False)
while(1):
    (ret,frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, b_w) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    if ret == True:
        out.write(grayframe)
        out2.write(b_w)
        #cv.imshow('video',b_w)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
out.release()
out2.release()
cv.destroyAllWindows()

