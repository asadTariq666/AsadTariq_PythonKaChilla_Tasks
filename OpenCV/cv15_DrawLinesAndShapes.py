import cv2 as cv
import numpy as np
from pyparsing import col

# Draw Canvas
img1 = np.zeros((600,600))  # Black image (0)
img2 = np.ones((600,600))   # White image (1)

# Print sizes
print('size of black image is: ', img1.shape)
print('size of white image is: ', img2.shape)

#print(img1)

# Adding colors to the image

colored_img = np.zeros((600,600,3), np.uint8) # color channel addition

# Coloring whole image
colored_img[:] = 55,100,200 # [:] means whole image

# Coloring part of image
colored_img[100:500,100:500] = 190,100,200 

#Adding line
cv.line(colored_img,(200,100),(400,500), (200,0,0),10)
cv.line(colored_img,(400,500),(00,100), (0,100,90),10)

#Adding Rectangles
cv.rectangle(colored_img,(50,200),(300,400),(20,00,200),4)
cv.rectangle(colored_img,(150,150),(250,250),(0,00,2),cv.FILLED)

# Adding Circles
cv.circle(colored_img,(300,300),100,(255,0,0),5)
cv.circle(colored_img,(300,300),30,(255,255,255),cv.FILLED)

# Adding text

cv.putText(colored_img,'Practice session', (200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,255),3)
cv.putText(colored_img,'next line', (200,550),cv.FONT_HERSHEY_DUPLEX,1,(255,255,255),3)
# cv.imshow('Black Image',img1)
# cv.imshow('White Image',img2)
cv.imshow('Colored Image',colored_img)




cv.waitKey(0)
cv.destroyAllWindows()