import cv2 as cv
import sys
img = cv.imread("OpenCV/Resources/2.jpg")
img = cv.resize(img,(400,300))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("MyImage",img)
cv.imshow("MyImage_gray",gray_img)
cv.imwrite('OpenCV/Resources/2_gray_new.png',gray_img)
cv.waitKey(0)
cv.destroyAllWindows()