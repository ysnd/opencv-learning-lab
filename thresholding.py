import cv2 as cv

img=cv.imread('/home/user/opencv/images/haha.png')
cv.imshow('Tes', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple thresholdinhg
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('SimpleThreshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('SimpleThreshold Inverse', thresh_inv)

#adaptive Thresholding
adap_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('AdaptiveThresholding', adap_thresh)


cv.waitKey(0)
