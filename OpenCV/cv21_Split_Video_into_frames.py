import cv2 as cv
import sys
cap = cv.VideoCapture("OpenCV/Resources/video1.mp4")

if (cap.isOpened()== False):
    print('video not found')

frame_num = 0

while(1):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"OpenCV/Resources/frames/frame_{frame_num}.jpg",frame)
    else:
        break
    frame_num = frame_num+1

cap.release()
cv.destroyAllWindows()
 