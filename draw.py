import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#paint the image a certain colour
blank[:] = 0,27,0
cv.imshow('Green', blank)

#membuat kotak
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

#menggambar bulat
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('bulat', blank)
#membuat garis
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Garis', blank)

cv.putText(blank, 'Hello, nama saya polly', (5,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)


