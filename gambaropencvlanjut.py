import cv2 as cv
import numpy as np

img = cv.imread('/home/wray/opencv/images/2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thres = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thres, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Gambar semua contours
cv.drawContours(img, contours, -1, (0,255,0), 2)

# Hitung luas dan keliling contour pertama
cnt = contours[0]
area = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt, closed=True)
print(f"Luas: {area}, Keliling: {perimeter}")

cv.imshow('Contours', img)

orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

result = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
cv.imshow('Feature Matching', result)

cv.waitKey(0)
