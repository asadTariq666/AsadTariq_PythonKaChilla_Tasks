import cv2 as cv
import sys
img = cv.imread("OpenCV/Resources/1.jpeg")
cv.imshow("MyImage",img)
cv.waitKey(0)
cv.destroyAllWindows()