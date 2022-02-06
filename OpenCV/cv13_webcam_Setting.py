import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

#Setting Brightness - Key for brightness is 10. (50 = 50% brightness)
cap.set(10,100)

#Setting width and Height (Keys = 3:4)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)


#Converting actual video in  grayscale
while(1):
    (ret,frame) = cap.read()
    if ret == True:
        cap.set
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
cv.destroyAllWindows()

