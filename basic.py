import cv2 as cv

img=cv.imread('/home/user/opencv/images/haha.png')
cv.imshow('tes', img)

#convert image warna
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#membuat blur
blur = cv.GaussianBlur(img,  (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#eroded 
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#resize
resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#crop
cropped=img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
