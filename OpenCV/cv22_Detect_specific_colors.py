import cv2 as cv
import numpy as np

# # Reading Image
# img = cv.imread("OpenCV/Resources/2.jpg")

# # Convert in HSV (Hue, Saturation, value)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#print(img.shape)


# sliders

def slider():
    pass
path = "OpenCV/Resources/2.jpg"

cv.namedWindow("Bars")
cv.resizeWindow("Bars",2208,1242)

#Hue
cv.createTrackbar("Hue Min","Bars",0,179,slider)
cv.createTrackbar("Hue Max","Bars",179,179,slider)
#Saturation
cv.createTrackbar("Saturation Min","Bars",0,255,slider)
cv.createTrackbar("Saturation Max","Bars",255,255,slider)
#Value
cv.createTrackbar("Value Min","Bars",0,255,slider)
cv.createTrackbar("Value Max","Bars",255,255,slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

hue_min = cv.getTrackbarPos("Hue min","Bars")


while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min","Bars")
    hue_max = cv.getTrackbarPos("Hue Max","Bars")
    sat_min = cv.getTrackbarPos("Saturation Min","Bars")
    sat_max = cv.getTrackbarPos("Saturation Max","Bars")
    val_min = cv.getTrackbarPos("Value Min","Bars")
    val_max = cv.getTrackbarPos("Value Max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    #Reflect changes in image
    lower =np.array([hue_min,sat_min,val_min])
    upper =np.array([hue_max,sat_max,val_max])
    mask_img =cv.inRange(hsv_img,lower,upper)
    out_img =cv.bitwise_and(img,img,mask=mask_img)

    cv.imshow("Original",img)
    cv.imshow("HSV",hsv_img)
    cv.imshow('masked',mask_img)
    cv.imshow('final',out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()
     

 