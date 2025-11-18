import cv2 as cv
import numpy as np


img=cv.imread('/home/wray/opencv/images/tes.png')
cv.imshow('haha', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255,-1)
cv.imshow('circle', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255,-1)
cv.imshow('Kotak', rectangle)

aneh=cv.bitwise_and(circle,rectangle)
cv.imshow("aneh", aneh)

masked = cv.bitwise_and(img,img,mask=aneh)
cv.imshow('Masked Image', masked)

cv.waitKey(0)
