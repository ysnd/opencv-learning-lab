import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/home/user/opencv/images/latest.png')
cv.imshow('image', img)

#plt.imshow(img)
#plt.show()
# BGR ro Grayscale
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# BGR to HSV
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)
#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)
#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#hsv to bgr
hsvbgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsvbgr', hsvbgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

