import cv2 as cv
import numpy as np
# Reading Image
img = cv.imread("OpenCV/Resources/2.jpg")

#Image Resizing
resized_img = cv.resize(img,(300,500))

#Gray Scaling
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Black and Wight
(thresh, b_w) = cv.threshold(gray_img,127,255,cv.THRESH_BINARY)

#Blurred Image
blurred = cv.GaussianBlur(img,(7,7),0)

#Edge Detection
edge_img = cv.Canny(img,48,48)

# Thickness of Lines (Image Dilation)
mat_kernel = np.ones((3,3), np.uint8)   # matrix of 3x3 with every element 1
dilated_image = cv.dilate(edge_img,mat_kernel,iterations=1)

# Make Thinner Image
ero_img = cv.erode(edge_img,mat_kernel,iterations=1)

#Cropping with Numpy
img2 = cv.imread("OpenCV/Resources/2.jpg")
#get shape of Image img i.e (2208,1242,3) 
print('the size of resized image is:',resized_img.shape) 
cropped_img = resized_img[0:300,0:200]



#Displaying Image
cv.imshow("MyImage",img)
cv.imshow('Resized Image',resized_img)
cv.imshow("MyImage_gray",gray_img)
cv.imshow("MyImage_black_White",b_w)
cv.imshow("MyImage_Blurred",blurred)
cv.imshow("MyImage_edge",edge_img)
cv.imshow("MyImage_dilated",dilated_image)
cv.imshow("MyImage_Erosion",ero_img)
cv.imshow('Cropped Image',cropped_img)


cv.waitKey(0)
cv.destroyAllWindows()