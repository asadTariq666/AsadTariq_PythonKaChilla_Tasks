import cv2 as cv
import sys
img = cv.imread("OpenCV/Resources/1.jpeg")
img = cv.resize(img,(400,300))
cv.imshow("MyImage",img)
cv.waitKey(0)
cv.destroyAllWindows()