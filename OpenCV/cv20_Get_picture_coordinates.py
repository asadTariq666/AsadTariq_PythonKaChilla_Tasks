import cv2 as cv
import numpy as np
from sympy import Q

# Define function to get coordinates
def find_coordinates(event,x,y, flags, params):

     #event = left muse click
    if(event ==cv.EVENT_FLAG_LBUTTON):
        print(x ,'', y )
        font = cv.FONT_ITALIC
        cv.putText(img,str(x)+ ',' + str(y),(x,y), font ,1, (255,0,0),1)

        # show text on image
        cv.imshow("image",img)
    
    # event = Right click to get color
    if(event==cv.EVENT_FLAG_RBUTTON):
        print(x ,'', y )
        font = cv.FONT_ITALIC

        # Definig colors from image
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img,str(b)+ ',' + str(g)+',' + str(r) ,(x,y), font ,1, (255,0,0),2)
        cv.imshow("image",img)


# Final function to read and Display
if __name__== "__main__":
    
    #reading image
    img = cv.imread("OpenCV/Resources/2.jpg",1)

    #Display image
    cv.imshow("image",img)

    #Setting callback function
    cv.setMouseCallback("image",find_coordinates)

    cv.waitKey(0)
    cv.destroyAllWindows()  
