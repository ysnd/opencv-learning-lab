import cv2 as cv

img=cv.imread('/home/user/opencv/images/latest.png')
cv.imshow('Tes', img)

#bluring averaging
average=cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

#Gaussian Blur
gaus=cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaus', gaus)

#Median Blur
med=cv.medianBlur(img, 3)
cv.imshow('MedianBlur', med)

#Bilateral Blur
bila=cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bila)

cv.waitKey(0)
