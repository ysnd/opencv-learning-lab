import cv2 as cv
import numpy as np

img=cv.imread('/home/wray/opencv/images/latest.png')
cv.imshow('haha', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Laplacion
lap = cv.Laplacian (gray, cv.CV_64F)
lap= np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx=cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely= cv.Sobel(gray, cv.CV_64F, 0, 1)
combine=cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('Combine',combine)

canny= cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)

cv.waitKey(0)
