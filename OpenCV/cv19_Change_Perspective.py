import cv2 as cv
import numpy as np
img = cv.imread("OpenCV/Resources/3.png")

#Finding width and height
print(img.shape)
height = 1376
width = 1036
#width,height = 1036,1376 


#Defining Points
point1 = np.float32([[237,600],[749,638],[48,955],[823,963]])


# Setting required starting and ending points to the start of processed image i.e 0,0  and ending  point of processed image (max width and height)
point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(point1,point2)

#creating output image
out_img = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("Original image",img)
cv.imshow("transformed image",out_img)
cv.waitKey(0)
cv.destroyAllWindows() 