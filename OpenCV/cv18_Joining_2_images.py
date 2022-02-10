import cv2 as cv
import numpy as np
img = cv.imread("OpenCV/Resources/1.jpeg")
img2 = cv.imread("OpenCV/Resources/2.jpg")
# Stacking same Image

#1- Horizontal stacking
hor_img = np.hstack((img,img))

#2- Vertical stacking
ver_img = np.vstack((img,img))

#Stacking Images of Different sizes

#Vertical 
def vconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv.vconcat(im_list_resize)

im_v_resize = vconcat_resize_min([img, img2])


#Horizontal
def hconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv.hconcat(im_list_resize)

im_h_resize = hconcat_resize_min([img, img2])

print(img.shape, img2.shape,im_v_resize.shape,im_h_resize.shape)


#ver_img = np.vstack((img,img2))

cv.imshow("Vertical different images",im_v_resize)
cv.imshow("Horizontal different images",im_h_resize)
#cv.imshow("MyImage2",img2)

# cv.imshow("Horizontal",hor_img)
# cv.imshow("Vertical",ver_img)

cv.waitKey(0)
cv.destroyAllWindows() 