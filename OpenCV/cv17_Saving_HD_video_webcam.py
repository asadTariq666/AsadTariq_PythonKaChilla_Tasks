#step1 - Import Libraries
import cv2 as cv
import numpy as np

#Step2 - Read frames from Camera
cap = cv.VideoCapture(0) # webcam number 1
if(cap.isOpened()==False):
    print('there is an error')

#Setting Resolution Function
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640.0)
    cap.set(4, 480.0)

def make_320p():
    cap.set(3, 320)
    cap.set(4, 240)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


#Calling Resolution Function
make_720p()
#change_res(1280, 720)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640.0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480.0)
#Changing frames per second
cap.set(cv.CAP_PROP_FPS, 40)

#Printing Resolution and FPS
print(cap.get(cv.CAP_PROP_FPS))
print(cap.get(3))
print(cap.get(4))


# writing Format, video writer object and file Output
frame_width =int(cap.get(3))  # 4:3
frame_height =int(cap.get(4)) # 4:3
#Saving actual video
out = cv.VideoWriter('OpenCV/Resources/webcam_video.avi', cv.VideoWriter_fourcc('M','J','P','G'),30, (frame_width,frame_height))
# read until the end
#Step3 - Display frame by frame
while(cap.isOpened()):
    #capture Frame by frame
    ret, frame =cap.read()
    if ret == True:
        out.write(frame)
        cv.imshow('Frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

# Step4 - Release and close windows
cap.release()
cv.destroyAllWindows()