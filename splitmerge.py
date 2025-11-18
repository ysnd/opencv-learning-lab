import cv2 as cv
import numpy as np

img=cv.imread('/home/user/opencv/images/latest.png')
cv.imshow('Tes', img)

blank=np.zeros(img.shape[:2], dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Biru', blue)
cv.imshow('Hijau',green)
cv.imshow('Merah',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('Merged image', merged)

cv.waitKey(0)
